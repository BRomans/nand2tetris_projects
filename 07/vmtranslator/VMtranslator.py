import sys
import os

from src.CodeWriter import CodeWriter
from src.Parser import Parser
from src.CommandsTable import CommandsTable


def main():
    commands_table = CommandsTable()
    code_writer = CodeWriter(commands_table)
    for argument in sys.argv[1:]:
        code_writer.set_file(argument)
        parser = Parser(argument, commands_table)
        while parser.has_more_commands():
            parser.advance()
            command_type = parser.command_type()
            argument1 = parser.arg1()
            argument2 = parser.arg2()
            if command_type == "C_ARITHMETIC":
                code_writer.write_arithmetic(argument1)
            if command_type == "C_PUSH":
                code_writer.write_push_pop("C_PUSH", argument1, argument2)
            if command_type == "C_POP":
                code_writer.write_push_pop("C_POP", argument1, argument2)

        code_writer.close()


main()