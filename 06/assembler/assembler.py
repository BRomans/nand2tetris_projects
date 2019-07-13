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
            hack_program = cleanup_commands(parser, hack_program)
            init_labels(symbol_table, parser, hack_program)
            translate_code(symbol_table, parser, hack_program)
            print("*** Assembly Completed ***")


def init_labels(symbol_table, parser, hack_program):
    address_n = 16
    for command in hack_program:
        command_type = parser.command_type(command)
        # print("*** Parsing Command ***\n", command + " " + command_type)
        if command_type == "L_COMMAND":
            command = command.split("(")[1].split(")")[0]
            symbol_table.add_entry(command, address_n + 1)
        else:
            address_n += 1


def translate_code(symbol_table, parser, hack_program):
    address_n = 16
    for command in hack_program:
        command_type = parser.command_type(command)
        # print("*** Parsing Command ***\n", command + " " + command_type)
        if command_type == "A_COMMAND":
            command = command.split("@")[1]
            if not command.isdigit():
                if symbol_table.contains(command):
                    command = int(symbol_table.get_address(command))
                else:
                    symbol_table.add_entry(command, address_n)
        if command_type == "C_COMMAND":
            dest = parser.dest(command)
            comp = parser.comp(command)
            jump = parser.jump(command)

        address_n += 1


def cleanup_commands(parser, hack_program):
    hack_program = parser.cleanup_empty_lines(hack_program)
    hack_program = parser.cleanup_empty_spaces(hack_program)
    hack_program = parser.cleanup_comments(hack_program)
    return hack_program


main()
