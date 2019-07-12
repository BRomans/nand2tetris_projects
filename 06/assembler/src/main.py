from src.parser import Parser
from src.code import Code
from src.symbol_table import SymbolTable


def main():
    parser = Parser()
    code = Code()
    symbol_table = SymbolTable()

    parser.has_more_commands()


main()
