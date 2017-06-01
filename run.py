"""
This application uses docopt with the built in cmd module to provide an
interactive command application.
Usage:
    docopt create_room <room_type> <room_name>
    docopt add_person <person_id> <person_name> <FELLOW|STAFF> [wants_accommodation]
    docopt print_room <room_name>
    docopt load_people<file_name>
    docopt print_allocations [<file_name>]
    docopt  print_unallocated [<filename>]
    docopt reallocate_person <person_id> <new_room>
    docopt allocate_unallocated_office <person_id>
    docopt allocate_unallocated_livingspace <person_id>
    docopt disallocate_person <person_id>
    docopt delete_person <person_id>
    docopt delete_room <room_name>
    docopt save_state <db_name>
    docopt load_state <db_name>
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
from termcolor import colored




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
    intro = colored("\n\n\n"+"*" * 180, "white")+ colored("\n\n\t\tHello, \
Welcome to the Amity space allocation app!\n\n", "blue")\
        +colored("\t\tThe commands are:\
\n\n \t\t> add_person <person_id> <first_name> <last_name> \
(FELLOW|STAFF) [<wants_accom>]\n\n\t\t")\
        +colored("> create_room <room_type> <room_name> ...")\
        +colored("\t\t\t> load_people <file_name>")\
        +colored("\n\n \t\t> reallocate_person <person_id> <new_room>")\
        +colored("\t\t\t> print_allocations [<file_name>]")\
        +colored("\n\n \t\t> print_room <room_name>...")\
        +colored("\t\t\t\t\t> print_unallocated [<filename>]")\
        +colored("\n\n \t\t> allocate_unallocated_office <person_id>...")\
        +colored("\t\t\t> allocate_unallocated_livingspace <person_id>...")\
        +colored("\n\n \t\t> disallocate_person <person_id>...")\
        +colored("\t\t\t\t> delete_person <person_id>...")\
        +colored("\n\n \t\t> delete_room <room_name>...")\
        +colored("\t\t\t\t\t> save_state <db_name>")\
        +colored("\n\n \t\t> load_state <db_name>\t\t\t\t\t\t> help\n\n\t\t> quit\t\t\t\t\t\t\t\t> clear")\
        +colored("\n\n\t\t* The commands with (...) allow you to enter multiple input. \
Separate the input with a comma(,) ","yellow")\
        +colored("\n\n\t\t* use 'clear' to clear the screen", "yellow")\
        + colored("\n\n\t\t* Click on the screen to type.\n\n", "yellow") + colored("*" * 180 + "\n\n\n", "white")

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
        person_name = arg["<first_name>"]+" "+arg["<last_name>"]
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

        self.amity.add_person(person_id, person_name, person_type, wants_accom)

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
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
    def do_allocate_unallocated_office(self, arg):
        """Usage: allocate_unallocated_office <person_id>"""
        person_ids = arg["<person_id>"].split(",")
        for person_id in person_ids:
            self.amity.allocate_unallocated_office(person_id)

    @docopt_cmd
    def do_allocate_unallocated_livingspace(self, arg):
        """Usage: allocate_unallocated_livingspace <person_id>"""
        person_ids = arg["<person_id>"].split(",")
        for person_id in person_ids:
            self.amity.allocate_unallocated_livingspace(person_id)

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_id> <new_room_name>"""
        person_id = arg["<person_id>"]
        new_room_name = arg["<new_room_name>"]
        self.amity.reallocate_person(person_id, new_room_name)
    @docopt_cmd
    def do_disallocate_person(self, arg):
        """Usage: disallocate_person <person_id>"""
        person_ids = arg["<person_id>"].split(",")
        for person_id in person_ids:
            self.amity.disallocate_person(person_id)

    @docopt_cmd
    def do_delete_person(self, arg):
        """Usage: delete_person <person_id>"""
        person_ids = arg["<person_id>"].split(",")
        for person_id in person_ids:
            self.amity.delete_person(person_id)

    @docopt_cmd
    def do_delete_room(self, arg):
        """Usage: delete_room <room_name>"""
        roomnames = arg["<room_name>"].split(",")
        for room_name in roomnames:
            self.amity.delete_room(room_name)

    @docopt_cmd
    def do_save_state(self, arg):
        """
        Usage: save_state <db_name>
        """
        db_name = args["<db_name>"]
        self.amity.save_state(db_name)

    @docopt_cmd
    def do_load_state(self, arg):
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
