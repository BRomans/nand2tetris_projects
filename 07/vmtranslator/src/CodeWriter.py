import os


class CodeWriter:

    def __init__(self):
        self.outputFile = None

    ''' Opens the output file and gets ready to write into it '''
    def set_file(self, output_file):
        print("*** Generating file ***\n", output_file)
        base = os.path.basename(output_file)
        file_name = os.path.splitext(base)[0]
        self.outputFile = open("translator/output/" + file_name + ".asm", "w", encoding='utf-8')

    ''' Writes to the output file the assembly code that implements the given arithmetic command '''
    def write_arithmetic(self, command):
        print("*** Writing arithmetic command ***")
        self.outputFile.write("// " + command)

    ''' Writes to the output file the assembly code that implements the given command, 
        where command is either C_POP or C_PUSH'''
    def write_push_pop(self, command, segment, index):
        print("*** Writing push/pop command ***")
        self.outputFile.write("// " + command + " " + segment + " " + index)

    ''' Closes the output file '''
    def close(self):
        self.outputFile.close()

