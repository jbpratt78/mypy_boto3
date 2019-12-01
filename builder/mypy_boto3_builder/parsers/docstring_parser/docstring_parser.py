"""
Botocore docstring parser.
"""
from __future__ import annotations

import re
import textwrap
from typing import Dict, List, Optional, Pattern

from pyparsing import ParseException

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.type_maps.type_map import TYPE_MAP
from mypy_boto3_builder.type_maps.named_type_map import NAMED_TYPE_MAP
from mypy_boto3_builder.type_annotations.type_typed_dict import TypeTypedDict
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type_annotation import TypeAnnotation
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_class import TypeClass
from mypy_boto3_builder.utils.strings import get_class_prefix
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.parsers.docstring_parser.syntax_grammar import SyntaxGrammar
from mypy_boto3_builder.parsers.docstring_parser.type_doc_grammar import TypeDocGrammar
from mypy_boto3_builder.parsers.docstring_parser.type_doc_line import TypeDocLine
from mypy_boto3_builder.parsers.docstring_parser.type_value import TypeValue
from mypy_boto3_builder.utils.strings import get_line_with_indented


class DocstringParser:
    """
    Botocore docstring parser.
    """

    RE_PARAM: Pattern[str] = re.compile("\n:param ")
    RE_RESPONSE_STRUCTURE: Pattern[str] = re.compile(
        r"\*\*Response Structure\*\*(\s*\n)*"
    )

    def __init__(self, prefix: str, arguments: List[Argument]) -> None:
        self.prefix = prefix
        self.logger = get_logger()
        self.arguments_map: Dict[str, Argument] = {
            f"{a.prefix}{a.name}": a for a in arguments
        }

    def _find_argument_or_append(self, name: str) -> Argument:
        if name in self.arguments_map:
            return self.arguments_map[name]

        for key in list(self.arguments_map):
            if key.startswith("*"):
                del self.arguments_map[key]

        self.arguments_map[name] = Argument(
            name, TypeAnnotation.Any(), TypeConstant(None)
        )
        return self.arguments_map[name]

    def _parse_request_syntax(self, input_string: str) -> None:
        """
        Parse type annotations for request arguments.

        Arguments:
            input_string -- Request syntax from dotocore docs.
            prefix -- Prefix for TypedDict classes.

        Returns:
            Mapping of argument name to its type annotation.
        """
        if "**Request Syntax**" not in input_string:
            return

        request_syntax_index = input_string.index("**Request Syntax**")
        while (
            request_syntax_index > 0 and input_string[request_syntax_index - 1] == " "
        ):
            request_syntax_index = request_syntax_index - 1
        request_syntax_string = get_line_with_indented(
            input_string[request_syntax_index:], True
        )

        try:
            match = SyntaxGrammar.request_syntax.parseString(request_syntax_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse request syntax for {self.prefix}")
            self.logger.debug(e)
            return

        argument_groups = match.asDict().get("arguments", [])
        for argument_dict in argument_groups:
            argument_name = argument_dict["name"]
            argument_prefix = self.prefix + get_class_prefix(argument_name)
            argument_value = TypeValue(argument_prefix, argument_dict["value"])
            argument_type = argument_value.get_type()
            argument = self._find_argument_or_append(argument_name)
            argument.type = argument_type

    def _parse_types(self, input_string: str) -> None:
        if ":type " not in input_string:
            return

        type_strings = [i for i in input_string.split("\n") if i.startswith(":type ")]
        for type_string in type_strings:
            TypeDocGrammar.reset()
            try:
                match = TypeDocGrammar.type_definition.parseString(type_string)
            except ParseException as e:
                self.logger.warning(
                    f"Cannot parse type definition {type_string} for {self.prefix}"
                )
                self.logger.debug(e)
                continue

            match_dict = match.asDict()
            argument_name = match_dict["name"]
            argument = self._find_argument_or_append(argument_name)
            argument.type = TYPE_MAP[match_dict["type_name"]]

    def _parse_params(self, input_string: str) -> None:
        if ":param " not in input_string:
            return

        for re_match in self.RE_PARAM.finditer(input_string):
            start_index = re_match.start()
            param_string = get_line_with_indented(input_string[start_index + 1 :])

            TypeDocGrammar.reset()
            try:
                match = TypeDocGrammar.param_definition.parseString(param_string)
            except ParseException as e:
                self.logger.warning(
                    f"Cannot parse param definition {param_string} for {self.prefix}"
                )
                self.logger.debug(e)
                continue

            argument_line = TypeDocLine(**match.asDict())
            if not argument_line.name:
                continue

            argument_name = argument_line.name
            argument = self._find_argument_or_append(argument_name)
            if argument_line.required:
                argument.default = None

            if not argument.type:
                continue

            if isinstance(argument.type, TypeTypedDict):
                argument.type.docstring = argument_line.render()

            self._mark_required_keys(argument.type, argument_line)

    def _mark_required_keys(
        self, type_annotation: FakeAnnotation, argument_line: TypeDocLine
    ) -> None:
        if not argument_line.indented:
            return

        if isinstance(type_annotation, TypeSubscript):
            if not type_annotation.children:
                return
            self._mark_required_keys_subscript(type_annotation, argument_line)

        if isinstance(type_annotation, TypeTypedDict):
            self._mark_required_keys_typed_dict(type_annotation, argument_line)

    def _mark_required_keys_typed_dict(
        self, typed_dict: TypeTypedDict, argument_line: TypeDocLine,
    ) -> None:
        typed_dict.docstring = argument_line.render()
        for line in argument_line.indented:
            if not line.name:
                continue

            attribute = typed_dict.get_attribute(line.name)
            attribute.required = line.required
            if not line.indented:
                continue

            self._mark_required_keys(attribute.type_annotation, line)

    def _mark_required_keys_subscript(
        self, subscript: TypeSubscript, argument_line: TypeDocLine,
    ) -> None:
        child = subscript.children[0]
        for line in argument_line.indented:
            if not line.type_name:
                continue
            self._mark_required_keys(child, line)

    def get_arguments(self, input_string: str) -> List[Argument]:
        input_string = textwrap.dedent(input_string)
        self._parse_types(input_string)
        self._parse_request_syntax(input_string)
        self._parse_params(input_string)

        arguments = list(self.arguments_map.values())
        arguments.sort(key=lambda x: x.default is not None)
        arguments.sort(key=lambda x: x.prefix is not None)
        return arguments

    def _parse_returns(self, input_string: str) -> Optional[FakeAnnotation]:
        if ":return: " not in input_string and ":returns: " not in input_string:
            return None
        TypeDocGrammar.reset()
        try:
            match = next(TypeDocGrammar.returns_definition.scanString(input_string))[0]
        except StopIteration:
            self.logger.warning(f"Cannot parse returns for {self.prefix}")
            return None

        description = match.asDict()["description"]
        if description == "None":
            return TypeConstant(None)

        if "True" in description or "False" in description:
            return TypeClass(bool)

        return None

    def _parse_rtype(self, input_string: str) -> Optional[FakeAnnotation]:
        if ":rtype: " not in input_string:
            return None

        TypeDocGrammar.reset()
        rtype_string = input_string[input_string.index(":rtype: ") :].split("\n", 1)[0]
        try:
            match = TypeDocGrammar.rtype_definition.parseString(rtype_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse rtype for {self.prefix}: {e}")
            return None

        type_name = match.asDict()["type_name"]
        if type_name not in TYPE_MAP:
            self.logger.warning(
                f"Cannot parse rtype value for {self.prefix}: {type_name}"
            )
            return None

        return TYPE_MAP[type_name]

    def _parse_response_syntax(self, input_string: str) -> Optional[FakeAnnotation]:
        if "**Response Syntax**" not in input_string:
            return None

        response_syntax_index = input_string.index("**Response Syntax**")
        while (
            response_syntax_index > 0 and input_string[response_syntax_index - 1] == " "
        ):
            response_syntax_index = response_syntax_index - 1
        response_syntax_string = get_line_with_indented(
            input_string[response_syntax_index:], True
        )

        try:
            match = SyntaxGrammar.response_syntax.parseString(response_syntax_string)
        except ParseException as e:
            self.logger.warning(f"Cannot parse response syntax for {self.prefix}")
            self.logger.debug(e)
            return None

        value = match.asDict()["value"]
        return TypeValue(f"{self.prefix}Response", value).get_type()

    def _get_response_docstring(self, input_string: str) -> str:
        re_match = self.RE_RESPONSE_STRUCTURE.search(input_string)
        if not re_match:
            return ""

        result = get_line_with_indented(input_string[re_match.end() :])
        return result

    def get_return_type(self, input_string: str) -> FakeAnnotation:
        input_string = textwrap.dedent(input_string)
        return_type = self._parse_rtype(input_string)
        if return_type is None:
            returns_return_type = self._parse_returns(input_string)
            if returns_return_type:
                return returns_return_type

            return TypeConstant(None)

        if not return_type.is_dict():
            return return_type

        syntax_return_type = self._parse_response_syntax(input_string)
        if syntax_return_type is None:
            return return_type

        if not isinstance(syntax_return_type, TypeTypedDict):
            return syntax_return_type

        syntax_return_type.docstring = self._get_response_docstring(input_string)
        return syntax_return_type

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
