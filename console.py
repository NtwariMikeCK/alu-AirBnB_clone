#!/usr/bin/python3
"""
this a custom cli created to work on our airbnb clone project
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        
        # if arg != "BaseModel" and arg != "User":
        if arg not in ("BaseModel", "User"):
            print("** class doesn't exist **")
            return
        
        if arg == "User":
            obj = User()
            obj.save()
            print(obj.id)
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        
        if args[0] not in ("BaseModel", "User"):
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        # Create the key to look up an instance
        key = f"{args[0]}.{args[1]}"
        data = storage.all()
        
        if data is None:
            print("** no data found **")
            return
        # Check if instance is present in storage
        if key not in data:
            print("** no instance found **")
        else:
            print("** Your Data **")
            print(data[key])
                    



    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ('BaseModel', 'User'):
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        # Create the key to remove it
        key = f"{args[0]}.{args[1]}"
        # we need to call storage.delete()
        storage.delete(key)


    def do_all(self, arg):
        """Prints all string representations of all instances
          based or not on class name"""
        if arg and arg not in ("BaseModel", "User"):
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values()])


    def do_update(self, arg):
        """Updates an instance based on class name and id 
        by adding/updating attributes"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in ('BaseModel', 'User'):
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
