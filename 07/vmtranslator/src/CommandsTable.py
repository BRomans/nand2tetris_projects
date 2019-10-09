class CommandsTable:

    def __init__(self):
        self.arithmeticTable = {
            "add": "",
            "sub": "",
            "neg": "",
            "eq": "",
            "gt": "",
            "lt": "",
            "and": "",
            "or": "",
            "not": ""
        }

        self.memoryAccessTable = {
            "push": "",
            "pop": ""
        }

    def contains_arithmetic_symbol(self, symbol):
        return symbol in self.arithmeticTable

    def get_arithmetic_symbol(self, symbol):
        return self.arithmeticTable[symbol]

    def get_mem_acc_table(self):
        return self.memoryAccessTable

