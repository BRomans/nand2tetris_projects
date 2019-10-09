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

    def get_arithmetic_table(self):
        return self.arithmeticTable

    def get_mem_acc_table(self):
        return self.memoryAccessTable

