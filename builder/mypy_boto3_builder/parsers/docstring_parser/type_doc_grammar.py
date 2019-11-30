"""
Pyparsing grammar for argument type doc lines.
"""
from pyparsing import (
    Forward,
    SkipTo,
    Literal,
    LineEnd,
    LineStart,
    Word,
    alphanums,
    indentedBlock,
    Optional,
    White,
)


class TypeDocGrammar:
    """
    EOL ::= ["\r"] "\n"
    SOL ::= LINE_START
    line ::= [^EOL]+ EOL
    word ::= alphanums + "_"
    indented_block ::= INDENT (line_indented | any_line)
    line_indented ::= any_line indented_block
    type_definition ::= ":type" [^:]+ ":" [^EOL]+
    rtype_definition ::= ":rtype:" [^EOL]+
    returns_definition ::= (":returns:" | ":return:") [^EOL]+
    param_definition ::= ":param" [^:]+ ":" [^EOL]+ EOL [indented_block]
    response_structure ::= "**Response Structure**" line [indented_block]
    typed_dict_key_line ::= "-" "**" word "**" "*(" word ")" "--*" [^EOL]+ + EOL
    type_line ::= "-" "*(" word ")" "--*" [^EOL]+ + EOL
    any_line ::= typed_dict_key_line | type_line | line
    """

    indent_stack = [1]
    SOL = LineStart().suppress()
    EOL = LineEnd().suppress()
    word = Word(alphanums + "_")
    line = SkipTo(LineEnd()) + EOL
    line_indented = Forward()
    any_line = Forward()
    indented_block = indentedBlock(
        line_indented | any_line, indentStack=indent_stack
    ).setResultsName("indented")
    line_indented <<= any_line + indented_block

    type_definition = (
        SOL
        + Literal(":type")
        + SkipTo(":").setResultsName("name")
        + Literal(":")
        + SkipTo(EOL).setResultsName("type_name")
    )

    rtype_definition = (
        SOL + Literal(":rtype:") + SkipTo(EOL).setResultsName("type_name")
    )

    returns_definition = (
        SOL
        + (Literal(":returns:") | Literal(":return:"))
        + SkipTo(EOL).setResultsName("description")
    )

    param_definition = (
        SOL
        + Literal(":param")
        + SkipTo(":").setResultsName("name")
        + Literal(":")
        + SkipTo(EOL).setResultsName("description")
        + EOL
        + Optional(indented_block)
    )

    response_structure = Literal("**Response Structure**") + line_indented

    typed_dict_key_line = (
        SOL
        + Literal("-")
        + White(ws=" \t")
        + Literal("**")
        + word.setResultsName("name")
        + Literal("**")
        + White(ws=" \t")
        + Literal("*(")
        + word.setResultsName("type_name")
        + Literal(")")
        + White(ws=" \t")
        + Literal("--*")
        + SkipTo(EOL).setResultsName("description")
        + EOL
    )

    type_line = (
        SOL
        + Literal("-")
        + White(ws=" \t")
        + Literal("*(")
        + word.setResultsName("type_name")
        + Literal(")")
        + White(ws=" \t")
        + Literal("--*")
        + SkipTo(EOL).setResultsName("description")
        + EOL
    )

    any_line <<= (typed_dict_key_line | type_line | line).setResultsName("line")

    @classmethod
    def fail_action(
        cls, _input_string: str, _chr_index: int, _source: str, _error: str
    ) -> None:
        return
        # column = col(chr_index, input_string)
        # print(
        #     "fail", column, cls.indent_stack, _error,
        # )
        # if column in cls.indent_stack:
        #     while cls.indent_stack[-1] != column:
        #         cls.indent_stack.pop()

    @classmethod
    def reset(cls) -> None:
        cls.indented_block.setFailAction(cls.fail_action)
        while len(cls.indent_stack) > 1:
            cls.indent_stack.pop()
