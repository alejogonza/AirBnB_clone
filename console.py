#!/usr/bin/python3
"""Consola AirBnB"""
import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    punto de entrada para el interprete
    """
    prompt = "(hbnb) "

    a_classes = {"BaseModel", "User", "State", "City",
                 "Amenity", "Place", "Review"}

    def emptyline(self):
        """no espacios"""
        pass

    def do_quit(self, line):
        """salir del programa"""
        return True

    def do_EOF(self, line):
        """salir del programa al final del archivo"""
        return True

    def do_create(self, line):
        """
        crear una nueva instancia y salvarla
        """
        try:
            if not line:
                raise SyntaxError()
            lists = line.split(" ")
            obj = eval("{}()".format(lists[0]))
            obj.save()
            print("{}".format(obj.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        borra la instancia con el nombre de clase y el id
        """
        try:
            if not line:
                raise SyntaxError()
            lists = line.split(" ")
            if lists[0] not in self.a_classes:
                raise NameError()
            if len(lists) < 2:
                raise IndexError()
            obj = storage.all()
            key = lists[0] + '.' + lists[1]
            if key in obj:
                del obj[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        muestra todas las estancias del string
        """
        obj = storage.all()
        lists = []
        if not line:
            for key in obj:
                lists.append(obj[key])
            print(lists)
            return
        try:
            args = line.split(" ")
            if args[0] not in self.a_classes:
                raise NameError()
            for key in obj:
                name = key.split('.')
                if name[0] == args[0]:
                    lists.append(obj[key])
            print(lists)
        except NameError:
            print("** class doesn't exist **")

    def count(self, line):
        """
        cuenta el numero de instancias de una clase
        """
        counter = 0
        try:
            lists = split(line, " ")
            if lists[0] not in self.a_classes:
                raise NameError()
            obj = storage.all()
            for key in obj:
                name = key.split('.')
                if name[0] == lists[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def default(self, line):
        """
        recuperar todas las instancias de una clase
        """
        lists = line.split('.')
        if len(lists) >= 2:
            if lists[1] == "all()":
                self.do_all(lists[0])
            elif lists[1] == "count()":
                self.count(lists[0])
            elif lists[1][:4] == "show":
                self.do_show(self.strip_clean(lists))
            elif lists[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(lists))
            elif lists[1][:6] == "update":
                args = self.strip_clean(lists)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
