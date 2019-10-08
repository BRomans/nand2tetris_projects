import re


class Parser:

    def __init__(self, hack_program):
        print("*** Parsing Program ***\n", hack_program)

    ''' Returns true if the input has more commands, else false'''
    def has_more_commands(self):
        print("Has More Commands test")
        return True

    ''' Read the next command from input and makes it the current command'''
    def advance(self):
        print("Advance test")
        return

    ''' Returns the type of the current command - A_COMMAND, C_COMMAND, L_COMMAND '''
    def command_type(self, command):
        try:
            if re.match(r'^@(\S)*', command):
                return "A_COMMAND"
            elif re.match(r'^\((\S*)\)$', command):
                return "L_COMMAND"
            elif re.match(r'^[A-Z=](\S*)(;\S*)?', command) or re.match(r'^(\S*)(;\S*)', command):
                return "C_COMMAND"
            else:
                raise SyntaxError
        except SyntaxError:
            print("*** Unreadable Command ***\n", command)

    ''' Returns the symbol or decimal Xxx of the current command. Only for A and L commands '''
    def symbol(self, command):
        if self.command_type(command) == "A_COMMAND":
            return command.split("@")[1]
        elif self.command_type(command) == "L_COMMAND":
            return command.split("(")[1].split(")")[0]
        else:
            return command

    ''' Returns the dest mnemonic in the current C-command. Only for C commands '''
    def dest(self, command):
        if "=" in command:
            dest = command.split("=")[0]
            return dest
        else:
            return "null"

    ''' Returns the comp mnemonic in the current C-command. Only for C commands '''
    def comp(self, command):
        if "=" in command:
            command_no_dest = command.split("=")[1]
            if ";" in command:
                comp = command_no_dest.split(";")[0]
                return comp
            else:
                return command_no_dest
        else:
            comp = command.split(";")[0]
            return comp

    ''' Returns the jump mnemonic in the current C-command. Only for C commands '''
    def jump(self, command):
        if ";" in command:
            jump = command.split(";")[1]
            return jump
        else:
            return "null"

    ''' Removes empty lines from the Hack program '''
    def cleanup_empty_lines(self, hack_program):
        hack_program_filtered = list()
        for line in hack_program:
            if not re.match(r'^\s*$', line):
                hack_program_filtered.append(line)
        return hack_program_filtered

    ''' Removes empty spaces between characters from the Hack program '''
    def cleanup_empty_spaces(self, hack_program):
        hack_program_filtered = list()
        for line in hack_program:
            line = line.replace(" ", "")
            line = line.strip()
            hack_program_filtered.append(line)
        return hack_program_filtered

    ''' Removes inline comments from the Hack program '''
    def cleanup_comments(self, hack_program):
        hack_program_filtered = list()
        for line in hack_program:
            if not line.startswith("//"):
                no_comments = line.split("//")[0]
                hack_program_filtered.append(no_comments)
        return hack_program_filtered

