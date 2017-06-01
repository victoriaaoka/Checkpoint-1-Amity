import os.path
import sys
import itertools
import random
from tabulate import tabulate
from colorama import init
from termcolor import colored

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Column, Table
from sqlalchemy.ext.declarative import declarative_base

from .person_class import Person, Fellow, Staff
from .room_class import Room, OfficeSpace, LivingSpace
from db.amity_database import Base, PersonDb, RoomDb



init()


class Amity(object):
    """
    This class contains all the methods/functions required for the
    entire amity system.
    """

    def __init__(self):
        self.people = []
        self.offices = []
        self.livingspaces = []
        self.office_waitinglist = []
        self.livingspace_waitinglist = []
        self.status = False

    def create_room(self, room_type, room_name):
        """
        This method creates rooms based on a user's input.
        Rooms can either be an office or a living space.
        """
        if not isinstance(room_type, str) or not isinstance(room_name, str):
            raise TypeError(
                colored("\nUse input of type string only!\n", "red"))

        elif room_type.lower() != "office" and room_type.lower() != "livingspace":
            print(colored(
                "\nWrong room_type! rooms can only be offices or living spaces\n", "red"))
            return("Invalid room type!")

        else:

            if room_type.lower() == "office":
                new_office = OfficeSpace(room_type, room_name)
                if new_office.room_name.lower() in [room.room_name.lower() for room in itertools.chain(self.offices, self.livingspaces)]:
                    print (colored("\nThe room name " +
                                   room_name + " already exists!\n", "red"))
                else:
                    self.offices.append(new_office)
                    print (colored("\nAn office called " + room_name +
                                   " has been successfully created!\n", "blue"))
                    return new_office

            elif room_type.lower() == "livingspace":
                new_livingspace = LivingSpace(room_type, room_name)
                if new_livingspace.room_name.lower() in [room.room_name.lower() for room in itertools.chain(self.offices, self.livingspaces)]:
                    print (colored("\nThe room name " +
                                   room_name + " already exists!\n", "red"))
                else:
                    self.livingspaces.append(new_livingspace)
                    print (colored("\nA livingspace called " + room_name +
                                   " has been successfully created\n", "blue"))
                    return new_livingspace

    def add_person(self, person_id, person_name, person_type, wants_accom="N"):
        """
        This method adds a new fellow or staff into the system.
        It also calls the allocate_livingspace and allocate_office method to assign the new staff and fellow rooms.
        """
        if not isinstance(person_id, str) or not isinstance(person_name, str) or not isinstance(person_type, str):
            raise TypeError("\nUse input type of string only\n")
            return "Use input type of string only"

        elif person_id.lower() in [person.person_id.lower() for person in self.people]:
            print(colored("\nPerson id: " + person_id + " already exists.\n", "red"))

        elif person_type.lower() == "fellow":
            new_person = Fellow(person_id, person_name, person_type, wants_accom)
            self.people.append(new_person)
            print(colored("\nFellow " + person_name + " has been successfully added.\n", "blue"))
            self.allocate_office()
            if wants_accom.lower() == "y":
                self.allocate_livingspace()
            return "Added successfully"

        elif person_type.lower() == "staff":
            new_person = Staff(person_id, person_name, person_type, wants_accom="N")
            self.people.append(new_person)
            print (colored("\nStaff " + person_name + "  has been successfully added.\n", "blue"))
            self.allocate_office()
            return "Added successfully"
        else:
            print (colored("\nWrong person_type! A person can only be a staff or fellow\n", "red"))
            return "Wrong person_type! A person can only be a staff or fellow"

    def allocate_office(self):
        """
        This method allocates a random office to a new fellow or staff
        """
        person = self.people[-1]
        if len(self.offices) == 0:
            self.office_waitinglist.append(person)
            print (colored("\nThere are no offices created yet! Added to waiting list \n", "red"))
        elif len(self.offices) > 0:
            available_offices = []
            full_offices = []
            for office in self.offices:
                if len(office.occupants) < office.capacity:
                    available_offices.append(office)
            if available_offices:
                selected_office = random.choice(available_offices)
                selected_office.occupants.append(person)
                self.status = True
                print (colored("\n" + person.person_name + " has been allocated the office " +
                               selected_office.room_name + ".\n", "blue"))
            else:
                self.office_waitinglist.append(person)
                print(colored("\nThere are no available offices! Added to waiting List.\n", "red"))

    def allocate_livingspace(self):
        """"
        This method allocates a living space to fellows who want accommodation
        """
        person = self.people[-1]
        if len(self.livingspaces) == 0:
            self.livingspace_waitinglist.append(person)
            print (colored("\nThere are no living spaces created yet! Added to waiting list.\n", "red"))
        elif len(self.livingspaces) > 0:
            available_livingspaces = []
            full_livingspaces = []
            for livingspace in self.livingspaces:
                if len(livingspace.occupants) < livingspace.capacity:
                    available_livingspaces.append(livingspace)
            if available_livingspaces:
                selected_livingspace = random.choice(available_livingspaces)
                selected_livingspace.occupants.append(person)
                self.status = True
                print (colored("\n" + person.person_name + " has been allocated the livingspace " +
                               selected_livingspace.room_name + "\n", "blue"))
            else:
                self.livingspace_waitinglist.append(person)
                print (colored("\nThere are no available living spaces! Added to waiting List\n", "red"))

    def print_room(self, room_name):
        """
        This method prints a list of the specified room's occupants
        """
        if room_name.lower() not in [room.room_name.lower()
                                     for room in itertools.chain(self.offices, self.livingspaces)]:
            print(colored("\nThe room " + room_name + " does not exist!\n", "red"))

        else:
            for room in itertools.chain(self.offices, self.livingspaces):
                while room.room_name.lower() == room_name.lower():
                    if len(room.occupants) <= 0:
                        print(colored("\nThe room has no occupants\n", "yellow"))
                        return "The room has no occupants"
                    else:
                        names = []
                        for occupant in room.occupants:
                            names.append(occupant.person_name)
                        table = enumerate(names, start=1)
                        print ("\n" + tabulate(table, headers=[room.room_name + " |  \
" + room.room_type], tablefmt="fancy_grid"))
                        print("\n")
                    break

    def load_people(self, file_name):
        """
        This method adds people from a txt file.
        """

        if not os.path.isfile(file_name + ".txt"):
            print(colored("\nThe file " + file_name + ".txt does not exist!\n"))
        elif not os.stat(file_name + ".txt").st_size:
            print(colored("\nThe file " + file_name +
                          ".txt is empty!\n", "yellow"))

        else:
            with open(file_name + ".txt") as input_file:
                for line in input_file:
                    read_line = line.split()
                    if len(read_line) > 5 or len(read_line) < 4:
                        print(colored("\nInvalid input!\n PLease ensure if follows +\
                            the format: Id FirstName LastName Person_type +\
                            [Wants_Accommodation]\n", "yellow"))
                    else:
                        try:
                            person_id = read_line[0]
                            person_name = read_line[1] + " " + read_line[2]
                            person_type = read_line[3]
                            wants_accom = read_line[4]
                        except IndexError:
                            wants_accom = "N"

                        self.add_person(person_id, person_name,
                                        person_type, wants_accom=wants_accom)

            print(colored("\nData loaded successfully!\n", "green"))

    def print_allocations(self, filename=None):
        """
        This method prints a list of allocations onto the screen.
        Specifying the optional -o option ie, the file _name,
        outputs the registered allocations to a txt file.
        """
        output = ""
        if not self.offices and not self.livingspaces:
            print(colored("\nThere are no rooms in the Amity!", "red"))

        for room in itertools.chain(self.offices, self.livingspaces):
            if len(room.occupants) <= 0:
                print(colored("\n" + room.room_type + " " +
                              room.room_name + " has no occupants", "yellow"))
            else:
                if room.occupants:
                    output += ("\n" + room.room_name +
                               " - " + room.room_type)
                    output += ("\n" + "-" * 50 + "\n")
                    for occupant in room.occupants:
                        output += (occupant.person_name+ ", ")

        if filename is None:
            print(colored(output, "blue"))
            print("\n")

        else:
            print("\nSaving data to file...\n")
            txt_file = open(filename + ".txt", "w+")
            txt_file.write(output)
            txt_file.close()
            print("\nData has been successfully \
saved to " + filename + ".txt\n")

    def reallocate_person(self, person_id, new_room_name):
        """
        This method allows the facilities manager to reallocate a person \
        to a different room.
        """
        all_rooms = self.livingspaces + self.offices
        try:
            reallocating_person = [person for person in self.people if person.person_id.lower() == person_id.lower()][0]
        except IndexError:
            print(colored("\nThe person does not exist.\n", "red"))
            return "The person does not exist."

        try:
            new_room = [room for room in all_rooms if room.room_name.lower() == new_room_name.lower()][0]
        except IndexError:
            print(colored("\nThe room does not exist.\n", "red"))
            return "The room does not exist."

        if reallocating_person in new_room.occupants:
            print(colored("\nThe person is in the room! Reallocation can not be to same room.\n", "red"))

        elif len(new_room.occupants) == new_room.capacity:
            print(colored("\nThe new room is full!\n", "yellow"))

        # elif new_room.room_type != current_room.room_type:
        # print("Reallocation can only be office - office or livingspace - livingspace")

        else:
            try:
                current_room = [room for room in all_rooms if reallocating_person in room.occupants and new_room.room_type == room.room_type][0]
                if new_room.room_type == current_room.room_type:
                    new_room.occupants.append(reallocating_person)
                    current_room.occupants.remove(reallocating_person)
                    print(colored("\n" + reallocating_person.person_name + " successfully reallocated to " + new_room.room_type
                        + " " + new_room.room_name + "\n", "green"))
                    return"Successfully reallocated!"

                else:
                    print(colored("\nReallocation can only be office - office or livingspace - livingspace.\n", "red"))
            except IndexError:
                if reallocating_person.person_type.lower() == "staff" and new_room.room_type.lower() == "livingspace":
                    print(colored("\nStaff cannot be reallocated to a living space!\n", "red"))
                else:
                    print(colored("\nThe person does not have any room currently. Please use allocate_unallocted.\n", "yellow"))


    def print_unallocated(self, filename=None):
        output = ""

        if not self.office_waitinglist and not self.livingspace_waitinglist:
            print(colored("\nThere are no unallocated Fellows or Staff at the moment.\n", "yellow"))
            return "There are no unallocated Fellows or Staff at the moment."
        else:
            output = ("\n List Of Unallocated Fellows AND Staff\n"\
                + "-" * 40 + "\n")
            for person in self.office_waitinglist:
                output += ( "\n"+ person.person_id + " "
                           + person.person_name+ " " + person.person_type + " - Office\n")

            for person in self.livingspace_waitinglist:
                if person.person_type.lower() == "fellow":
                    output += ("\n"+ person.person_id + " "
                               + person.person_name+ " " + person.person_type + " "
                               + person.wants_accom + " - Livingspace \n")
                else:
                    print("error")

            if filename is None:
                print(colored("\n" + output + "\n", "blue"))
            else:
                print(colored("Saving unallocations to file...\n", "blue"))
                txt_file = open(filename + ".txt", "w+")
                txt_file.write(output)
                txt_file.close()
                print(colored("\nUnallocations successfully saved to " + filename + ".txt\n", "green"))
                return "Unallocations successfully saved"

    def allocate_unallocated_office(self, person_id):
            try:
                available_office = [room for room in self.offices if len(room.occupants) < room.capacity][0]
                if self.office_waitinglist:
                    try:
                        person = [person for person in self.office_waitinglist if person.person_id.lower() == person_id.lower()][0]
                        available_office.occupants.append(person)
                        self.office_waitinglist.remove(person)
                        print(colored("\n" + person.person_name + " moved from waiting list to office " + available_office.room_name+ "\n", "green"))
                    except IndexError:
                        print(colored("The person is not in the office_waitinglist.\n", "yellow"))


                else:
                    print(colored("\nThere are no people in the office_waitinglist\n","yellow"))
            except IndexError:
                print(colored("\nThere are no available offices.\n", "yellow"))

    def allocate_unallocated_livingspace(self, person_id):
            try:
                available_livingspace = [room for room in self.livingspaces if len(room.occupants) < room.capacity][0]
                if self.livingspace_waitinglist:
                    try:
                        person = [person for person in self.livingspace_waitinglist if person.person_id.lower() == person_id.lower()][0]
                        available_livingspace.occupants.append(person)
                        self.livingspace_waitinglist.remove(person)
                        print(colored("\n" + person.person_name + " moved from waiting list to livingspace " + available_livingspace.room_name+ "\n", "green"))
                    except IndexError:
                        print(colored("The person is not in the livingspace_waitinglist.\n", "yellow"))
                else:
                    print(colored("\nThere are no people in the livingspace_waitinglist\n","yellow"))
            except IndexError:
                print(colored("\nThere are no available livingspaces.\n", "yellow"))

    def disallocate_person(self, person_id):

        try:
            person_to_disallocate = [person for person in self.people if person.person_id.lower() == person_id.lower()][0]
            for room in itertools.chain(self.offices, self.livingspaces):
                if person_to_disallocate in room.occupants:
                    if room.room_type == "office":
                        self.office_waitinglist.append(person_to_disallocate)
                        room.occupants.remove(person_to_disallocate)
                    else:
                        self.livingspace_waitinglist.append(person_to_disallocate)
                        room.occupants.remove(person_to_disallocate)
            print(colored("\nPerson disallocated successfully!\n","green"))

        except IndexError:
            print(colored("\nThe person is not assigned any room.\n", "red"))
            return "The person is not assigned any room."


    def delete_person(self, person_id):
        all_rooms = self.offices + self.livingspaces

        try:
            person_to_delete = [person for person in self.people if person.person_id.lower() == person_id.lower()][0]
            self.people.remove(person_to_delete)
            for room in itertools.chain(self.offices, self.livingspaces):
                if person_to_delete in room.occupants:
                    room.occupants.remove(person_to_delete)

            for person in itertools.chain(self.office_waitinglist, self.livingspace_waitinglist):
                if person == person_to_delete:
                    if person in self.office_waitinglist:
                        self.office_waitinglist.remove(person)
                    else:
                        self.livingspace_waitinglist.remove(person)
            print(colored("\nPerson deleted successfully!\n","green"))

        except IndexError:
            print(colored("\nThe person does not exist.\n", "red"))
            return "The person does not exist."

    def delete_room(self, room_name):
        try:
            room_to_delete = [room for room in itertools.chain(self.offices, self.livingspaces) if room.room_name.lower() == room_name.lower()][0]
            for room in itertools.chain(self.offices, self.livingspaces):
                if room == room_to_delete:
                    if room in self.offices:
                        if len(room.occupants) > 0:
                            for occupant in room.occupants:
                                self.office_waitinglist.append(occupant)
                                room.occupants.remove(occupant)
                        self.offices.remove(room)
                    else:
                        if len(room.occupants) > 0:
                            for occupant in room.occupants:
                                self.livingspace_waitinglist.append(occupant)
                                room.occupants.remove(occupant)
                        self.livingspaces.remove(room)
            print(colored("\nRoom deleted successfully!\n", "green"))
        except IndexError:
            print(colored("\nThe room does not exist.\n", "red"))
            return "The room does not exist."

    def save_state(self, db_name='amity_database.db'):
        """
        This method persists all the data stored in the app to a SQLite database.
        """
        if db_name:
            engine = create_engine("sqlite:///{}".format(db_name))
        else:
            engine=create_engine("sqlite:///amity_database.db")

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        all_rooms = self.offices + self.livingspaces

        for person in self.people:
            room_allocated = []
            for room in all_rooms:
                if person in room.occupants:
                    room_allocated.append(room.room_name)
            room_allocated =  " ".join(room_allocated)
            person = PersonDb(id = None, person_id=person.person_id, person_name=person.person_name, person_type=person.person_type, wants_accommodation=person.wants_accom, room_allocated=room_allocated)
            session.add(person)
            session.commit()

        for room in all_rooms:
            room_occupants = ""
            for occupant in room.occupants:
                room_occupants += occupant.person_name
            room = RoomDb(id=None, room_name=room.room_name,
                        room_type=room.room_type, occupants=room_occupants)
            session.add(room)
            session.commit()
        session.close()
        print("Data saved successfully!")


    def load_state(self, db_name):
        """
        This method loads data from the database into the application.
        """
        engine = create_engine("sqlite:///{}".format(db_name))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for p_record in  session.query(PersonDb):
            if p_record.person_type.lower() == "fellow":
                person = Fellow(p_record.person_id, p_record.person_name, p_record.person_type, p_record.wants_accommodation)
                self.people.append(person)

            elif p_record.person_type.lower() == "staff":
                person = Staff(p_record.person_id, p_record.person_name, p_record.person_type, p_record.wants_accommodation)
                self.people.append(person)


        for r_record in session.query(RoomDb):
            if r_record.room_type.lower() == "office":
                room = OfficeSpace(r_record.room_type, r_record.room_name, r_record.occupants)
                self.offices.append(room)

            else:
                room = LivingSpace(r_record.room_type, r_record.room_name, r_record.occupants)
                self.livingspaces.append(room)
        print ("Data loaded succesfully!")
