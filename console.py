#!/usr/bin/python3
"""module that contains entry point of the command interpreter"""

import cmd
import shlex
import models

from models.base_model import BaseModel
from models.user import User
from models.artist import Artist
from models.arts import Arts
from models.score import Score
from models import storage
from shlex import split


class ArsualCommand(cmd.Cmd):
    """All the command of the aplication"""
    prompt = "(arsual)"

    errors = {
        "missingClass": "** class name missing **",
        "wrongClass": "** class doesn't exist **",
        "missingID": "** instance id missing **",
        "wrongID": "** no instance found **",
        "missingAttr": "** attribute name missing **",
    }

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Artist': Artist,
               'Score': Score, 'Arts': Arts
    }

    def do_quit(self, arg):
        """
        Exit the program.
            usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program.
            usage: EOF (ctrl+D)
        """
        return True

    def emptyline(self):
        """handles the emptyline"""
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        _args = args.split(" ", 1)
        if not _args[0]:
            print(self.errors["missingClass"])
            return
        elif _args[0] not in ArsualCommand.classes:
            print(self.errors["wrongClass"])
            return
        new_instance = ArsualCommand.classes[_args[0]]()
        if len(_args) > 1:
            _kwargs = dict((x, y)
                           for x, y in (elt.split('=')
                           for elt in _args[1].split(' ')))

            for key, value in _kwargs.items():
                try:
                    getattr(new_instance, key)
                except AttributeError:
                    continue
                if value[0] is "\"":
                    value = value.strip("\"")
                    value = value.replace("_", " ")
                    value = value.replace("\\\"", "\"")
                elif "." in value:
                    value = float(value)
                else:
                    try:
                        value = int(value)
                    except Exception:
                        continue
                setattr(new_instance, key, value)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    print(models.storage.all()[key])
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def do_destroy(self, arg):
        """Delete an Instance"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(arg) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def do_all(self, args):
        """ Shows all objects, or all objects of a class"""
        my_list = []
        if args:
            args = args.split(' ')[0]  # remove possible trailing args
            if args not in ArsualCommand.classes:
                print(self.errors["wrongClass"])
                return
            for k, v in models.storage.all(args).items():
                my_list.append(str(v))
        else:
            for k, v in models.storage.all().items():
                my_list.append(str(v))

        print(my_list)

    def do_update(self, arg):
        """Updates an instance based on the class name"""
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            if len(args) < 2:
                print(self.errors["missingID"])
            else:
                key = args[0] + '.' + args[1]
                if key in models.storage.all().keys():
                    if len(args) < 3:
                        print(self.errors["missingAttr"])
                    else:
                        obj = models.storage.all()[key]
                        try:
                            attr_type = type(getattr(obj, args[2]))
                            args[3] = attr_type(args[3])
                        except Exception:
                            try:
                                args[3] = int(args[3])
                            except Exception:
                                try:
                                    args[3] = float(args[3])
                                except Exception:
                                    pass

                        setattr(obj, args[2], args[3])
                        obj.save()
                else:
                    print(self.errors["wrongID"])
        else:
            print(self.errors["wrongClass"])

    def do_count(self, arg):
        "Usage: count <class name> or <class name>.count()"
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            instances = str(models.storage.all().keys())
            print(instances.count(args[0]))
        else:
            print(self.errors["wrongClass"])


if __name__ == "__main__":
    ArsualCommand().cmdloop()
