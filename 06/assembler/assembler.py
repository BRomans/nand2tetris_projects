import sys

from src.code import Code
from src.parser import Parser
from src.symbol_table import SymbolTable


def main():

    for argument in sys.argv[1:]:
        parser = Parser(argument)
        code = Code()
        symbol_table = SymbolTable()
        with open(argument, 'r') as hack_program:
            hack_program = parser.cleanup_empty_lines(hack_program)
            hack_program = parser.cleanup_empty_spaces(hack_program)
            hack_program = parser.cleanup_comments(hack_program)
            for command in hack_program:
                dest = ''
                comp = ''
                jump = ''
                command_type = parser.command_type(command)
                print("*** Parsing Command ***\n", command + " " + command_type)
                if command_type == "C_COMMAND":
                    dest = parser.dest(command)
                    comp = parser.comp(command)
                    jump = parser.jump(command)


main()
