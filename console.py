#!/usr/bin/python3
"""
this a custom cli created to work on our airbnb clone project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This a custom command prompt"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Overrides default behavior to do nothing on an empty line"""
        pass

if __name__=="__main__":
    HBNBCommand().cmdloop()
