"""
This application uses docopt with the built in cmd module to provide an
interactive command application.
Usage:
    docopt create_room <room_type> <room_name>
    docopt add_person <person_id> <person_name> <FELLOW|STAFF> [wants_accommodation]
    docopt print_room <room_name>
    docopt load_people<file_name>
    docopt print_allocations [<file_name>]
    reallocate_person <person_id> <new_room>
    docopt (-i | --interactive)
    docopt (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import os
import cmd
from docopt import docopt, DocoptExit
from my_app.amity_class import Amity
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

            print("\n\nInvalid Command!\n\n")
            print(e)
            print ("\n\n")
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class AmitySpaceAllocationApp (cmd.Cmd):
    intro = colored("\n\n\n"+"*" * 170, "white")+ colored("\n\n\t\tHello, Welcome to the Amity space allocation app!\n\n", "blue")\
        +colored("\t\tThe commands are:\n\n \t\t> create_room <room_type> <room_name>\n\n\t\t")\
        +colored("> add_person <person_id> <first_name> <last_name> (FELLOW|STAFF) [<wants_accom>]")\
        +colored("\n\n \t\t> load_people <file_name>")\
        +colored("\n\n \t\t> print_room <room_name>\n\n \t\t> help\n\n\t\t> quit\n\n")\
        +colored("\n\t\t* To create multiple rooms, separate the room names with a comma(,) ","yellow")\
        +colored("\n\n\t\t* To print multiple rooms, separate the room names with a comma(,) ","yellow")\
        + colored("\n\n\t\t* Click on the screen to type.\n\n", "yellow") + colored("*" * 170 + "\n\n\n", "white")

    prompt = "(AmitySpaceAllocationApp) "
    file = None
    amity = Amity()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>"""
        room_type = arg["<room_type>"]
        roomnames = arg["<room_name>"].split(",")
        for room_name in roomnames:
            self.amity.create_room(room_type, room_name)


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
        if not wants_accom:
            wants_accom = "N"

        elif wants_accom.lower() != "n" and wants_accom.lower() != "y":
            print (colored("\n\nWants accommodation can only be 'Y' or 'N'\n\n", "red"))

        elif person_type.lower() == "staff" and wants_accom.lower()== "y":
            print (colored( "\n\nStaff cannot be allocated accomodation space\n\n","red"))

        self.amity.add_person(person_id, name, person_type, wants_accom)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg["<room_name>"]
        roomnames = arg["<room_name>"].split(",")
        for room_name in roomnames:
            self.amity.print_room(room_name)

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <file_name>"""
        file_name = arg["<file_name>"]
        self.amity.load_people(file_name)

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<filename>]"""
        filename = arg["<filename>"]
        self.amity.print_allocations(filename)

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<filename>]"""
        filename = arg["<filename>"]
        self.amity.print_unallocated(filename)

    @docopt_cmd
    def do_allocate_unallocated(self, arg):
        """Usage: allocate_unallocated <room_type>"""
        room_type = arg["<room_type>"]
        self.amity.allocate_unallocated(room_type)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_id> <new_room_name>"""
        person_id = arg["<person_id>"]
        new_room_name = arg["<new_room_name>"]
        self.amity.reallocate_person(person_id, new_room_name)

    @docopt_cmd
    def do_save_state(self, args):
        """
        Usage: save_state <db_name>
        """
        db_name = args["<db_name>"]
        self.amity.save_state(db_name)

    @docopt_cmd
    def do_load_state(self, args):
        """
        Usage: load_state <db_name>
        """
        db_name = args['<db_name>']
        self.amity.load_state(db_name)

    def do_clear(self, arg):
        """Clears screen"""

        os.system("clear")


    def do_quit(self, arg):
        """Exits the Interactive Mode."""
        print(colored("\n\n\t\t\tGood Bye! See you soon!\n\n", "green"))
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        AmitySpaceAllocationApp().cmdloop()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass
