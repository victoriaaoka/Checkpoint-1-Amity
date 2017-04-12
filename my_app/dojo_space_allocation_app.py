"""
This application uses docopt with the built in cmd module to provide an
interactive command application.
Usage:
    docopt create_room <room_type> <room_name>
    docopt add_person <person_id> <person_name> <FELLOW|STAFF> [wants_accommodation]
    docopt (-i | --interactive)
    docopt (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
   
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo_class import Dojo
from colorama import init
from termcolor import colored
init()



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            """ To print a message to the user when invalid commands are entered."""

            print("Invalid Command!")
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DojoSpaceAllocationApp (cmd.Cmd):
    intro = colored("\n\n\n"+"*" * 100, "white")+ colored("\n\n\n\n \t\t\tWelcome to the Dojo space allocation app!", "blue")\
        + colored(" \n\n\n\n \t\t\tType help to view a list of commands.","white")\
        + colored("\n\n\n\n \t\t\tClick on the screen to type.\n\n\n\n", "blue") + colored("*" * 100 + "\n\n\n", "white")

    prompt = "(DojoSpaceAllocationApp) "
    file = None
    dojo = Dojo()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>"""
        room_type = arg["<room_type>"]
        room_names = arg["<room_name>"].split(",")
        for room_name in room_names:
            self.dojo.create_room(room_type, room_name)
        

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_id> <first_name> <last_name> (FELLOW|STAFF) [<wants_accom>]"""
        
        person_id = arg["<person_id>"]
        name = arg["<first_name>"]+" "+arg["<last_name>"]
        person_type = ""
        staff = arg["STAFF"]
        fellow = arg["FELLOW"]

        if staff is None:
            person_type = fellow
        else:
            person_type = staff
        wants_accom = arg["<wants_accom>"]
        self.dojo.add_person(person_id, name, person_type, wants_accom)

    def do_quit(self, arg):
        """Exits the Interactive Mode."""

        print(colored("\t\t\tGood Bye!", "yellow"))
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        DojoSpaceAllocationApp().cmdloop()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass
