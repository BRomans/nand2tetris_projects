
class Parser:

    def __init__(self, input_file):
        print("*** Parsing Program ***\n", input_file)
        self.inputFile = open(input_file, 'r')
        self.remainingLines = len(open(input_file, 'r').readlines())
        self.currentCommand = ""

    ''' Returns true if the input has more commands, else false'''
    def has_more_commands(self):
        print("Has More Commands test")
        return self.remainingLines != 0

    ''' Read the next command from input and makes it the current command. 
        Should be called only if has_more_command is true. Initially there
        is no current command.'''
    def advance(self):
        print("Advance test")
        self.currentCommand = self.inputFile.readline()
        self.remainingLines -= 1
        return

    ''' Returns a constant representing the type of the current command.
        C_ARITHMETIC is returned for all the arithmetic/logical commands'''
    def command_type(self):
        return

    ''' Returns the first argument of the current command. In case of 
        C_ARITHMETIC, the command itself is returned. Should not be called 
        if the current command is C_RETURN.'''
    def arg1(self):
        return

    ''' Returns the second argument of the current command. Should be called
            only if the current command is C_PUSH, C_POP, C_FUNCTION or C_CALL'''
    def arg2(self):
        return
