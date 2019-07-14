import sys
import os

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
            base = os.path.basename(argument)
            file_name = os.path.splitext(base)[0]
            process_translation(symbol_table, code, parser, hack_program, file_name)
            print("*** Assembly Completed ***")


def init_labels(symbol_table, parser, hack_program):
    address_n = 16
    for command in hack_program:
        command_type = parser.command_type(command)
        # print("*** Parsing Command ***\n", command + " " + command_type)
        if command_type == "L_COMMAND":
            command = command.split("(")[1].split(")")[0]
            symbol_table.add_entry(command, address_n + 1 )
        else:
            address_n += 1


def process_translation(symbol_table, code, parser, hack_program, file_name):
    address_n = 16
    file_output = open("output/" + file_name + ".hack", "w")
    for command in hack_program:
        command_type = parser.command_type(command)
        # print("*** Parsing Command ***\n", command + " " + command_type)
        if command_type == "A_COMMAND":
            command = command.split("@")[1]
            if not command.isdigit():
                if symbol_table.contains(command):
                    command = int(symbol_table.get_address(command))
                    b_address = format(command, "015b")
                    print("Writing A instruction: " + "0" + b_address + "\n")
                    file_output.write("0" + b_address + "\n")
                else:
                    symbol_table.add_entry(command, address_n)
            else:
                command = int(command)
                b_address = format(command, "015b")
                file_output.write("0" + b_address + "\n")

        if command_type == "C_COMMAND":
            dest = parser.dest(command)
            comp = parser.comp(command)
            jump = parser.jump(command)
            b_dest = code.dest(dest)
            b_comp = code.comp(comp)
            b_jump = code.jump(jump)
            print("Writing C instruction: " + "111" +  b_comp + b_dest + b_jump + "\n")
            file_output.write("111" + b_comp + b_dest + b_jump + "\n")

        address_n += 1
    file_output.close()


def cleanup_commands(parser, hack_program):
    hack_program = parser.cleanup_empty_lines(hack_program)
    hack_program = parser.cleanup_empty_spaces(hack_program)
    hack_program = parser.cleanup_comments(hack_program)
    return hack_program


main()
