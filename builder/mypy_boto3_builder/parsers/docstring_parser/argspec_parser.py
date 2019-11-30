"""
Argspec parser for arguments.
"""
import inspect
from typing import List, Optional
from types import FunctionType


from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_maps.type_map import TYPE_MAP
from mypy_boto3_builder.type_maps.named_type_map import NAMED_TYPE_MAP
from mypy_boto3_builder.type_maps.method_type_map import METHOD_TYPE_MAP


class ArgSpecParser:
    @staticmethod
    def _get_arguments_from_argspec(func: FunctionType) -> List[Argument]:
        arguments: List[Argument] = []
        argspec = inspect.getfullargspec(func)
        for argument_name in argspec.args:
            if argument_name == "factory_self":
                argument_name = "self"
            type_annotation: Optional[TypeAnnotation] = TypeAnnotation.Any()
            if not arguments and argument_name in ("self", "cls"):
                type_annotation = None
            arguments.append(Argument(argument_name, type_annotation))
        if argspec.defaults:
            for index, default_value in enumerate(argspec.defaults):
                argument_index = len(arguments) - len(argspec.defaults) + index
                arguments[argument_index].default = TypeConstant(default_value)

        if argspec.varargs:
            arguments.append(
                Argument(argspec.varargs, TypeAnnotation.Any(), prefix="*")
            )
        for argument_name in argspec.kwonlyargs:
            arguments.append(Argument(argument_name, TypeAnnotation.Any()))
        if argspec.kwonlydefaults:
            for argument_name, default_value in argspec.kwonlydefaults:
                for argument in arguments:
                    if argument.name != argument_name:
                        continue
                    argument.default = TypeConstant(default_value)
                    break
        if argspec.varkw:
            arguments.append(Argument(argspec.varkw, TypeAnnotation.Any(), prefix="**"))
        return arguments

    def get_function_arguments(self, func: FunctionType) -> List[Argument]:
        func_name = func.__name__
        arguments = self._get_arguments_from_argspec(func)

        for argument in arguments:
            method_type = f"{func_name}: {argument.name}"
            if method_type in METHOD_TYPE_MAP:
                argument.type = METHOD_TYPE_MAP[method_type]

        return arguments

    @staticmethod
    def parse_type(type_str: str, name: Optional[str] = None) -> FakeAnnotation:
        if name is not None:
            try:
                return NAMED_TYPE_MAP[f"{name}: {type_str}"].copy()
            except KeyError:
                pass

        try:
            return TYPE_MAP[type_str].copy()
        except KeyError:
            raise ValueError(f"Unknown type: {type_str}")
