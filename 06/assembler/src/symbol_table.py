

class SymbolTable:

    ''' Create a new empty symbol table '''
    def __new__(cls):
        print("Constructor")

    ''' Adds the pair symbol/address to the table '''
    def add_entry(self, symbol, address):
        print("Add Entry test")

    ''' Returns True if the symbol is contained in the table, else False'''
    def contains(self, symbol):
        print("Contains test")
        return True

    ''' Returns the address associated with the symbol '''
    def get_address(self, symbol):
        print("Get Address test")