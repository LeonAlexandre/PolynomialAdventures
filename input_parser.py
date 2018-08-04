###INPUT PARSER METHODS
##Input: User strings

#output: instruction for the main program

#format of string:
# 'command arg1 arg2 ... argN' 
#input_list[0] is the command

class InputString():
    #Input string

    def __init__(self,input_str='none'):
        self.input_str = input_str
        self.input_list = []
        self.command = 'none'
        self.command_list = ['help', #list of all commands available
                            'time', #increments the time
                            'upgrade',
                            'stop',
                            'contribs' #prints the contribution of each polynomial
                            ]

    def update_str(self,input_str):
        self.input_str = input_str

    def create_list(self):
        self.input_list = self.input_str.split()

    def generate_command(self,input_str): #updates self.command
        self.update_str(input_str)
        self.create_list()
        inp = self.input_list #for memory purposes
        argsize = len(inp)
        if inp[0] not in self.command_list:
            self.command = 'unknown'
        elif inp[0] == 'help':
            self.command = 'none'
            self.print_help()
        elif inp[0] == 'time':
            self.command = 'time'
        elif inp[0] == 'stop':
            self.command = 'stop'



    def print_help(self):
        help_str = 'HELP. Lists all commands. for further help, call "command help"'
        help_str += '\ntime: advances time'
        help_str += '\nupgrade: prints upgrade shop. upgrade help for shop help'
        help_str += '\nstop: stop the game'
        help_str += '\ncontribs: prints contributions from each polynomial with current X'
        print(help_str)