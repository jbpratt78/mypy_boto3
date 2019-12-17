"""
String to type annotation map that find type annotation by method and argument name.
"""
from typing import Dict, Optional

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_maps.typed_dicts import (
    ec2_tag_type,
    s3_copy_source_type,
)


ArgumentTypeMap = Dict[str, FakeAnnotation]
MethodTypeMap = Dict[str, ArgumentTypeMap]
ClassTypeMap = Dict[str, MethodTypeMap]
ServiceTypeMap = Dict[str, ClassTypeMap]


TYPE_MAP: ServiceTypeMap = {
    ServiceNameCatalog.ec2.boto3_name: {
        "*": {
            "create_tags": {
                "Resources": TypeSubscript(Type.List, [Type.Any]),
                "Tags": TypeSubscript(Type.List, [ec2_tag_type]),
                "DryRun": Type.bool,
            },
            "delete_tags": {
                "Resources": TypeSubscript(Type.List, [Type.Any]),
                "Tags": TypeSubscript(Type.List, [ec2_tag_type]),
                "DryRun": Type.bool,
            },
        }
    },
    ServiceNameCatalog.s3.boto3_name: {
        "Client": {
            "copy_object": {
                "CopySource": TypeSubscript(Type.Union, [Type.str, s3_copy_source_type])
            },
            "upload_part_copy": {
                "CopySource": TypeSubscript(Type.Union, [Type.str, s3_copy_source_type])
            },
        },
    },
    ServiceNameCatalog.dynamodb.boto3_name: {
        "Table": {
            "batch_writer": {
                "return": ExternalImport(
                    ImportString("boto3", "dynamodb"), "BatchWriter"
                )
            }
        }
    },
}


def _get_from_method_map(
    method_name: str, argument_name: str, method_type_map: MethodTypeMap,
) -> Optional[FakeAnnotation]:
    if method_name in method_type_map:
        operation_type_map = method_type_map[method_name]
        if argument_name in operation_type_map:
            return operation_type_map[argument_name]

    return None


def _get_from_class_map(
    class_name: str, method_name: str, argument_name: str, class_type_map: ClassTypeMap,
) -> Optional[FakeAnnotation]:
    if class_name in class_type_map:
        result = _get_from_method_map(
            method_name, argument_name, class_type_map[class_name]
        )
        if result:
            return result
    if "*" in class_type_map:
        result = _get_from_method_map(method_name, argument_name, class_type_map["*"])
        if result:
            return result
    return None


def _get_from_service_map(
    service_name: ServiceName,
    class_name: str,
    method_name: str,
    argument_name: str,
    service_type_map: ServiceTypeMap,
) -> Optional[FakeAnnotation]:
    if service_name.boto3_name in service_type_map:
        result = _get_from_class_map(
            class_name,
            method_name,
            argument_name,
            service_type_map[service_name.boto3_name],
        )
        if result:
            return result
    if "*" in service_type_map:
        result = _get_from_class_map(
            class_name, method_name, argument_name, service_type_map["*"]
        )
        if result:
            return result
    return None


def get_method_type_stub(
    service_name: ServiceName, class_name: str, method_name: str, argument_name: str
) -> Optional[FakeAnnotation]:
    return _get_from_service_map(
        service_name, class_name, method_name, argument_name, TYPE_MAP
    )
