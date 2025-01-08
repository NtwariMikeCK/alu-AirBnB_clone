#!/usr/bin/python3
"""
This module defines a command-line interpreter for the HBNB project.
It allows users to interact with the system using specific commands.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""
    
    prompt = "(hbnb) "  # Custom shell prompt

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    def do_EOF(self, arg):
        """Handles End Of File (Ctrl+D) to exit the interpreter"""
        print()
        return True

    def emptyline(self):
        """Overrides default behavior to do nothing on an empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
