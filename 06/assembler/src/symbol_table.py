

class SymbolTable:

    table = dict()

    ''' Create a new empty symbol table '''
    def __init__(self):
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