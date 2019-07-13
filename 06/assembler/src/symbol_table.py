

class SymbolTable:



    ''' Create a new empty symbol table '''
    def __init__(self):
        self.table = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 16384,
            "KBD": 24576

        }
        print("*** New Symbol Table instance created ***")

    ''' Adds the pair symbol/address to the table '''
    def add_entry(self, symbol, address):
        self.table[symbol] = address
        print("*** Registered symbol {" + symbol + "} with address {" + address + "} ***")

    ''' Returns True if the symbol is contained in the table, else False'''
    def contains(self, symbol):
        if self.table[symbol] is not None:
            return True
        else:
            return False

    ''' Returns the address associated with the symbol '''
    def get_address(self, symbol):
        print("*** Fetching address of symbol {" + symbol + "} ***")
        return self.table[symbol]