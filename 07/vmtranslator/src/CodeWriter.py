
class CodeWriter:

    ''' Opens the output file and gets ready to write into it '''
    def __init__(self, output_file):
        print("*** Generating file ***\n", output_file)

    ''' Writes to the output file the assembly code that implements the given arithmetic command '''
    def write_arithmetic(self, command):
        return

    ''' Writes to the output file thte assembly code that implements the given command, 
        where command is either C_POP or C_PUSH'''
    def write_push_pop(self, command, segment, index):
        return

    ''' Closes the output file '''
    def close(self):
        return

