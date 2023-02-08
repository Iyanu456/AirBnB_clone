#!/usr/bin/python3
"""Console module"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpretter """

    prompt = " (hbnb) "

    def do_EOF():
        """ End of file """
        return True

    def do_quit(self, arg):
        """ exits the program """
        return True

    def emptyline(self):
        """ do nothing """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
