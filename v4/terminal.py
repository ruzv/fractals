

class terminal:

    terminal_name = ""
    quit_terminal = False

    # the name by who the command is called
    command_names = []
    # the mem adress for the asociated commands name function
    command_functions = []
    # short discription of the command or its parameters
    command_discriptions = []


    def __init__(self, name):
        self.terminal_name = name

        self.add_command("exit", self.exit_terminal, "None")
        self.add_command("cmnd", self.print_commands, "None")
        self.add_command("help", self.command_help, "None||{command}")
        self.add_command("add", add, "int && int")
        self.add_command("sub", sub, "int && int")

    # the function of a commnad must have a parameter (args) even when not used
    def add_command(self, command_name, function, discription):
        self.command_names.append(command_name)
        self.command_functions.append(function)
        self.command_discriptions.append(discription)

    def remove_command(self, command_name):
        try:
            i = self.command_names.index(command_name)
            del self.command_names[i]
            del self.command_functions[i]
            del self.command_discriptions[i]
        except:
            print("unable to remove command. no such command name.")

    # gets the command and its parameters from the user
    def get_command(self):
        command = input(self.terminal_name+": ")
        return command
    
    def execute_command(self, command):
        args = command.split(" ")
        if args[0] in self.command_names:
            c = self.command_names.index(args[0])
            del args[0]
            try:
                self.command_functions[c](args)
            except:
                print("invalid command parameters")
                print("try \"help {your command}\" for help")
        else:
            print("no such command found")
            print("try \"help\" for a list of avaible commands")


    def terminal(self):
        while self.quit_terminal != True:
            command = self.get_command()
            self.execute_command(command)

    # default commands
    def exit_terminal(self, args):
        self.quit_terminal = True

    def print_commands(self, args):
        for i in range(len(self.command_names)):
            print(self.command_names[i], self.command_functions[i])

    def command_help(self, args):
        if len(args) != 0:
            i = self.command_names.index(args[0])
            print(self.command_names[i], self.command_discriptions[i])
        else:
            for i in range(len(self.command_names)):
                print(self.command_names[i], self.command_discriptions[i])

def add(args):
    a = int(args[0])
    b = int(args[1])
    print(a+b)

def sub(args):
    a = int(args[0])
    b = int(args[1])
    print(a-b)

# ter = terminal("comp")
# ter.terminal()