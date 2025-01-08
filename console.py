#!/usr/bin/python3
import cmd
"""This is custom CLI designed to handle all our airbnb operations"""


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB objects"""
    prompt = "(hbnb) "  # Custom shell prompt

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    def do_EOF(self, arg):
        """Handles End Of File (Ctrl+D) to exit"""
        print("")
        return True

    def emptyline(self):
        """Does nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
