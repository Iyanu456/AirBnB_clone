#!/usr/bin/python3
"""Console module"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
import json
import shlex
import importlib
module = importlib.import_module("models")


class HBNBCommand(cmd.Cmd):
    """hbnb command interpreter"""
    __classes = {"BaseModel"}

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """End of file
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """does nothing
        """
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel
        """
        if not args:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = eval(args)()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """Prints the string of an instance based on the class name and id
        """
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
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
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

    def do_all(self, args):
        """Prints the string representation of all instances
        based on or not on the class name
        """
        split_args = shlex.split(args)
        n_list = []
        dict_json = models.storage.all()
        if args:
            if split_args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                for key in models.storage.all():
                    if split_args[0] == key.split('.')[0]:
                        n_list.append(str(dict_json[key]))
                print(n_list)
        else:
            for key in models.storage.all():
                n_list.append(str(models.storage.all()[key]))
            print(n_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
