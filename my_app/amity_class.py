import os.path
import sys
import itertools
import random
from tabulate import tabulate
from colorama import init
from termcolor import colored
from .person_class import Person, Fellow, Staff
from .room_class import Room, OfficeSpace, LivingSpace
init()


class Amity(object):
    """This class contains all the methods/functions required . """

    def __init__(self):
        self.all_fellows = []
        self.all_staff = []
        self.offices = []
        self.livingspaces = []
        self.fellow_and_staff_ids = []
        self.office_waitinglist = []
        self.livingspace_waitinglist = []


    def create_room(self,room_type, room_name):
        """This method creates rooms based on a user's input.
        Rooms can either be an office or a living space.
        """
        if not isinstance(room_type, str) or not isinstance(room_name,str):
            raise TypeError (colored("\n\nUse input of type string only!\n\n", "red"))

        elif room_type.lower() != "office" and room_type.lower() != "livingspace":
            print (colored("\n\nWrong room_type! rooms can only be offices or living spaces\n\n","red" ))
            return("Invalid room type!")
        #print(room_name)

        else:

            if room_type.lower() == "office":
                new_office = OfficeSpace(room_type, room_name)
                if new_office.room_name.lower() in [room.room_name.lower() for room in itertools.chain(self.offices, self.livingspaces)]:
                    print (colored("\n\nThe room name " + room_name + " already exists!\n\n", "red"))
                else:
                    self.offices.append(new_office)
                    print (colored("\n\nAn office called " + room_name + " has been successfully created!\n\n","blue"))
                    return new_office

            elif room_type.lower() == "livingspace":
                new_livingspace = LivingSpace(room_type, room_name)
                if new_livingspace.room_name.lower() in [room.room_name.lower() for room in itertools.chain(self.offices, self.livingspaces)]:
                    print (colored("\n\nThe room name " + room_name + " already exists!\n\n", "red"))
                else:
                    self.livingspaces.append(new_livingspace)
                    print (colored("\n\nA livingspace called " +room_name+" has been successfully created\n\n","blue"))
                    return new_livingspace


    def add_person(self, person_id, name, person_type, wants_accom = "N"):
        """This method adds a new fellow or staff into the system.
        It also calls the allocate_livingspace and allocate_office method to assign the new staff and fellow rooms.
        """
        if not isinstance(person_id, str) or not isinstance(name,str) or not isinstance(person_type,str):
            raise TypeError("\n\nUse input type of string only\n\n")
            return "Use input type of string only"

        elif person_type.lower() != "staff" and person_type.lower() != "fellow":
            print (colored("\n\nWrong person_type! A person can only be a staff or fellow\n\n","red" ))
            return "Wrong person_type! A person can only be a staff or fellow"

        else:
            if person_type.lower() == "fellow":
                new_fellow = Fellow(person_id, name, person_type, wants_accom)
                self.all_fellows.append(new_fellow)
                if new_fellow.person_id in self.fellow_and_staff_ids:
                    print (colored("\n\nFellow id: " + new_fellow.person_id +" already exists.\n\n","red"))
                else:
                    print(colored("\n\nFellow " + name +" has been successfully added.\n\n","blue"))
                    self.fellow_and_staff_ids.append(person_id)
                    self.allocate_office(name)
                    if wants_accom == "Y":
                        self.allocate_livingspace(name)
                        return "There are no available living spaces! Added to waiting List"
                    return "Added successfully"



            elif person_type.lower() == "staff":

                new_staff = Staff(person_id, name, person_type)

                if new_staff.person_id in self.fellow_and_staff_ids:
                    print(colored("\n\nStaff id: "+ new_staff.person_id +" already exists.\n\n","red"))


                else:
                    self.all_staff.append(new_staff)
                    self.fellow_and_staff_ids.append(person_id)
                    print (colored("\n\nStaff " + name + "  has been successfully added.\n\n", "blue"))
                    self.allocate_office(name)
                    return "Added successfully"

    def allocate_office(self, name):
        """This method allocates a random office to a new fellow or staff"""

        if len(self.offices) == 0:
            self.office_waitinglist.append(name)
            print (colored("\n\nThere are no offices created yet! Added to waiting list \n\n", "red"))
        elif len(self.offices) > 0:
            available_offices = []
            full_offices = []
            for office in self.offices:
                if len(office.occupants) < office.capacity:
                    available_offices.append(office)
            if available_offices:
                selected_office = random.choice(available_offices)
                selected_office.occupants.append(name)
                print (colored("\n\n" + name + " has been allocated the office " + selected_office.room_name +".\n\n","blue"))
            else:
                self.office_waitinglist.append(name)
                print (colored("\n\nThere are no available offices! Added to waiting List.\n\n", "red"))

    def allocate_livingspace(self, name):
        """" This method allocates a living space to fellows who want accommodation"""

        if len(self.livingspaces) == 0:
            self.livingspace_waitinglist.append(name)
            print (colored("\n\nThere are no living spaces created yet! Added to waiting list.\n\n", "red"))
        elif len(self.livingspaces) > 0:
            available_livingspaces = []
            full_livingspaces = []
            for livingspace in self.livingspaces:
                if len(livingspace.occupants) < livingspace.capacity:
                    available_livingspaces.append(livingspace)
            if available_livingspaces:
                    selected_livingspace = random.choice(available_livingspaces)
                    selected_livingspace.occupants.append(name)
                    print (colored("\n\n"+ name + " has been allocated the livingspace " + selected_livingspace.room_name+"\n\n","blue"))
            else:
                self.livingspace_waitinglist.append(name)
                print (colored("\n\nThere are no available living spaces! Added to waiting List\n\n", "red"))

    def print_room(self, room_name):
            """This method prints a list of the specified room's occupants"""
            if not room_name.lower() in [room.room_name.lower() for room in itertools.chain(self.offices, self.livingspaces)]:
                print(colored("\nThe room " + room_name+ " does not exist!\n" ,"red"))

            else:
                for room in itertools.chain(self.offices, self.livingspaces):
                    if len(room.occupants) <= 0:
                        print (colored("\n\nThe room has no occupants\n\n", "yellow"))
                        return "The room has no occupants"
                    else:
                        while room.room_name == room_name:
                            table = enumerate(room.occupants, start = 1)
                            print ("\n\n" + tabulate(table, headers=[room.room_name+" |  "+ room.room_type], tablefmt="fancy_grid"))
                            break


    def load_people(self, file_name):
        """This method adds people from a txt file.
        """

        if not os.path.isfile(file_name + ".txt"):
            print(colored("\n\nThe file "+file_name+".txt does not exist!\n\n"))
        elif not os.stat(file_name + ".txt").st_size:
            print(colored("\n\nThe file "+file_name+".txt is empty!\n","yellow"))

        else:

            with open(file_name + ".txt") as input_file:
                for line in input_file:
                    read_line = line.split()
                    if len(read_line) > 5 or len(read_line) < 4:
                        print(colored("\n\nInvalid input!\n PLease ensure if follows +\
                            the format: Id FirstName LastName Person_type +\
                            [Wants_Accommodation]", "yellow"))
                    else:
                        try:
                            person_id = read_line[0]
                            name = read_line[1] + " " + read_line[2]
                            person_type = read_line[3]
                        except IndexError:
                            wants_accom = read_line[4]

                        self.add_person(person_id, name, person_type, wants_accom="N")

            print (colored("\n\nData loaded successfully\n\n", "blue"))

    def print_allocations(self):
        pass

    def print_unallocated(self):
        pass


    def reallocate_person(self, person_id, new_room):
        pass

    def save_state(self):
        pass

    def load_state(self):
        pass
