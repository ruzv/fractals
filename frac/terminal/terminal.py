


class terminal:


    terminal_name = ""
    end_season = False
    
    commands = []
    command = ""
    functions = []

    # terminal name (self explanitory)
    def __init__(self, terminal_name):
        self.terminal_name = terminal_name
        self.end_season = False
        self.add_command("exit", self.exit_terminal)
        self.add_command("help", self.help_command)
    
    # commands are a string witout the prams "add 1 2" command: "add"
    # funtion the adres for the function that the command calls
    def add_command(self, command, function):
        self.commands.append(command)
        self.functions.append(function)

    # removes command by its name
    def remove_command(self, command):
        i = self.commands.index(command)
        del self.commands[i]
        del self.functions[i]

    # gets user input. the command
    def get_command(self):
        self.command = input(self.terminal_name+": ")

    # try to call the function asociated with the command name
    # if falis displays error messages
    def execute_command(self):
        args = self.command.split(" ")
        if args[0] in self.commands:
            i = self.commands.index(args[0])
            del args[0]
            try:
                self.functions[i](args)
            except:
                print("invalid command arguments")
                print("try \"help + your command\" for more info about the command")
        else:
            print("invalid command")
            print("try \"help\" for a list of avaible commands")
        self.terminal()

    # the main function 
    def terminal(self):
        while self.end_season == False:
            self.get_command()
            self.execute_command()
        
    # built in commands

    def exit_terminal(self, args):
        self.end_season = True

    def help_command(self, args):
        if args == []:
            file = open("help.txt", "r")
            for i in file:
                print(i)
        else:
            in_file = False
            file = open("help.txt", "r")
            for i in file:
                if i.split(" ")[0] == args[0]:
                    print(i)
                    in_file = True
                    break
            if in_file == False:
                print("command not found")

        

def add(args):
    a = int(args[0])
    b = int(args[1])
    print(a + b)
    return a + b
def sub(args):
    a = int(args[0])
    b = int(args[1])
    print(a - b)
    return a - b



terminal = terminal("compy")
terminal.add_command("add", add)
terminal.add_command("sub", sub)

terminal.terminal()