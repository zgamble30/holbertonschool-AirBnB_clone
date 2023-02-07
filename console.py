#!/usr/bin/python3
"""console part of our Air BnB clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    """this is the main loop for commands and it always begins with the prompt"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """exits the loop and quits cmd line interpreter upon quit"""
        raise SystemExit

    def do_EOF(self, args):
        """exits loop and quits interpreter for when it is the EOF"""
        raise SystemExit

    def emptyline(self):
        """nothing will be executed for an empty line"""
        pass

    def do_create(self, args):
        """This will create a new BaseModel"""
        if (len(args) == 0):
            print("** class name missing **")
        elif (args in valid_class.keys()):
            x = valid_class[args]()
            x.save()
            print(x.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """shows information"""
        if (len(args) == 0):
            print("** class name missing **")
        elif (args in valid_class.keys()):
            if len(list_args) == 1:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
