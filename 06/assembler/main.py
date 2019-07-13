import sys

from src.code import Code
from src.parser import Parser
from src.symbol_table import SymbolTable


def main():

    for argument in sys.argv[1:]:
        parser = Parser(argument)
        code = Code()
        symbol_table = SymbolTable()

        #parser.has_more_commands()


main()
