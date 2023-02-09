#!/usr/bin/python3
"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter"""

    prompt = " (hbnb) "

    def do_EOF(self, arg):
        """ End of file"""
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def emptyline(self):
        """ does nothing"""
        pass

    def do_create(self, args):
        """ Creates a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            cls = globals().get(args, None)
            instance = cls()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ Prints the string of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                for key, value  in storage.all().items():
                    if args[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        if not args: 
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if args[1] == value.id:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
