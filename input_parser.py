###INPUT PARSER METHODS
##Input: User strings

#output: instruction for the main program

#format of string:
# 'command arg1 arg2 ... argN' 
#input_list[0] is the command

class InputString():
    #Input string

    def __init__(self,input_str):
        self.input_str = input_str
        self.input_list = []
        self.command = 'none'
        self.command_list = ['help', #list of all commands available
                            'time',
                            'upgrade'
                            ]

    def create_list(self):
        self.input_list = self.input_str.split()

    def generate_command(self): #updates self.command
        
        inp = self.input_list #for memory purposes
        argsize = len(inp)
        if inp[0] not in self.command_list:
            self.command = 'unknown'
        elif inp[0] == 'help':
            self.command = 'help'
        elif inp[0] == 'time':
            self.command = 'time'

