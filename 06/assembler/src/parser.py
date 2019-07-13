class Parser:

    hack_program = ''

    def __new__(cls, file):
        with open(file, 'r') as file_text:
            hack_program = file_text.read()
            print("Parsing:\n", hack_program)

    ''' Returns true if the input has more commands, else false'''
    def has_more_commands(self):
        print("Has More Commands test")
        return True

    ''' Read the next command from input and makes it the current command'''
    def advance(self):
        print("Advance test")
        return

    ''' Returns the type of the current command - A_COMMAND, C_COMMAND, L_COMMAND '''
    def commandType(self, command):

        print("Command Type test")
        return

    ''' Returns the symbol or decimal Xxx of the current command. Only for A and L commands '''
    def symbol(self):
        print("Symbol test")
        return

    ''' Returns the dest mnemonic in the current C-command. Only for C commands '''
    def dest(self):
        print("Dest test")
        return

    ''' Returns the comp mnemonic in the current C-command. Only for C commands '''
    def comp(self):
        print("Comp test")

    ''' Returns the jump mnemonic in the current C-command. Only for C commands '''
    def jump(self):
        print("Jump test")

