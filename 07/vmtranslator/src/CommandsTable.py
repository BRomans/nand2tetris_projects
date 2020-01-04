class CommandsTable:

    def __init__(self):
        self.arithmeticTable = {
            "add": "D+A",
            "sub": "A-D",
            "neg": "-D",
            "eq": "JEQ",
            "gt": "JGT",
            "lt": "JLT",
            "and": "D&A",
            "or": "D|A",
            "not": "!D"
        }

        self.memoryAccessTable = {
            "constant": "D=A",
            "pop": ""
        }

    def contains_arithmetic_symbol(self, symbol):
        print("*** Fetching value of symbol {" + symbol + "} ***")
        return symbol in self.arithmeticTable

    def get_arithmetic_symbol(self, symbol):
        return self.arithmeticTable[symbol]

    def get_memory_symbol(self, symbol):
        print("*** Fetching value of symbol {" + symbol + "} ***")
        return self.memoryAccessTable[symbol]

    def get_mem_acc_table(self):
        return self.memoryAccessTable

