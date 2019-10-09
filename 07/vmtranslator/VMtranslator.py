import sys
import os

from src.CodeWriter import CodeWriter
from src.Parser import Parser
from src.CommandsTable import CommandsTable

def main():

    argument = sys.argv[1]
    commands_table = CommandsTable
    parser = Parser(argument, commands_table)
    while parser.has_more_commands():
        parser.advance()