"""
Boto3 client parser, produces `structures.Client`.
"""
import inspect

from boto3.session import Session
from botocore.errorfactory import ClientExceptionsFactory
from botocore.exceptions import ClientError

from mypy_boto3_builder.structures.client import Client
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.enums.service_name import ServiceName
from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.parsers.helpers import parse_method, get_public_methods
from mypy_boto3_builder.parsers.boto3_utils import get_boto3_client


def parse_client(session: Session, service_name: ServiceName) -> Client:
    """
    Parse boto3 client to a structure.

    Arguments:
        session -- boto3 session.
        service_name -- Target service name.

    Returns:
        Client structure.
    """
    client = get_boto3_client(session, service_name)
    public_methods = get_public_methods(client)

    # remove methods that will be overriden
    if "get_paginator" in public_methods:
        del public_methods["get_paginator"]
    if "get_waiter" in public_methods:
        del public_methods["get_waiter"]

    methods = [
        parse_method("Client", method_name, method)
        for method_name, method in public_methods.items()
    ]
    result = Client(
        service_name=service_name,
        boto3_client=client,
        docstring=inspect.getdoc(client) or "",
        methods=methods,
    )

    service_model = client.meta.service_model
    client_exceptions = ClientExceptionsFactory().create_client_exceptions(
        service_model
    )
    for exception_class_name in dir(client_exceptions):
        if exception_class_name.startswith("_"):
            continue
        if not exception_class_name[0].isupper():
            continue
        result.exceptions_class.attributes.append(
            Attribute(
                exception_class_name, TypeClass(ClientError, alias="Boto3ClientError")
            )
        )

    result.attributes.append(
        Attribute(
            "exceptions",
            InternalImport(
                name=result.exceptions_class.name,
                module_name=ServiceModuleName.client,
                service_name=service_name,
            ),
        )
    )
    return result
