import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import random
from colorama import init
from termcolor import colored
init()
from room_class import Room, OfficeSpace, LivingSpace
from person_class import Person, Fellow, Staff
class Dojo():
    
    def __init__(self):
        self.all_fellows = []
        self.all_staff = []
        self.offices = []
        self.livingspaces = []
        self.all_rooms = []
        self.fellow_ids = []
        self.staff_ids = []
        self.room_names = []
        

    def create_room(self,room_type, room_name):
        """This method creates rooms based on a user's input.
        Rooms can either be an office or a living space.
        """
        if not isinstance(room_type, str) or not isinstance(room_name,str):
            raise TypeError (colored("\n\nUse input of type string only!\n\n", "red"))
        
        elif room_type.lower() != "office" and room_type.lower() != "livingspace":
            return colored("\n\nWrong room_type! rooms can only be offices or living spaces\n\n","red" )
        #print(room_name)        
        
        else:

            if room_type.lower() == "office":
                new_office = OfficeSpace(room_type, room_name)                
                for room in self.all_rooms:
                    self.room_names.append(room.room_name)
                if new_office.room_name in self.room_names:
                    print (colored("\n\nThe Office room already exists!\n\n", "red"))
                else:
                    self.offices.append(new_office)
                    self.all_rooms.append(new_office)
                    print (colored("\n\nAn office called " + room_name + " has been successfully created!\n\n","blue"))
                    return self 

            elif room_type.lower() == "livingspace":
                new_livingspace = LivingSpace(room_type, room_name)
                for room in self.all_rooms:
                    self.room_names.append(room.room_name)
                if new_livingspace.room_name in self.room_names:
                    print (colored("\n\nThe room name already exists!\n\n", "red"))
                else:
                    self.livingspaces.append(new_livingspace)
                    self.all_rooms.append(new_livingspace)
                    print (colored("\n\nA livingspace called " +room_name+" has been successfully created\n\n","blue"))
                    return self


    def add_person(self, person_id, name, person_type, wants_accom = "N"):
        """This method adds a new fellow or staff into the system.
        It also calls the allocate_livingspace and allocate_office method to assign the new staff and fellow rooms.
        """            
        if not isinstance(person_id, str) or not isinstance(name,str) or not isinstance(person_type,str):
            raise TypeError("\n\nUse input type of string only\n\n")
            
        elif isinstance(person_id, str) and isinstance(name, str) and isinstance(person_type, str):
            if person_type.lower() == "fellow":
                new_fellow = Fellow(person_id, name, person_type, wants_accom)
                self.all_fellows.append(new_fellow)
                if new_fellow.person_id in self.fellow_ids:
                    print (colored("\n\nFellow" + new_fellow.name + " already exists.\n\n","red"))
                else:
                    print(colored("\n\nFellow " + name +" has been successfully added.\n\n","blue"))
                    self.allocate_office(name)
                    self.fellow_ids.append(person_id)
                    if wants_accom == "Y":
                        self.allocate_livingspace(name)


            elif person_type.lower() == "staff":
                
                new_staff = Staff(person_id, name, person_type)
                
                if new_staff.person_id in self.staff_ids:
                    print(colored("\n\nStaff " +new_staff.name + "already exists.\n\n","red"))
                
                else:
                    self.all_staff.append(new_staff)
                    self.staff_ids.append(person_id)
                    print (colored("\n\nStaff " + name + "  has been successfully added.\n\n", "blue"))
                    self.allocate_office(name)
                    
    def allocate_office(self, name):
        """This function allocates a random office to a fellow and staff"""
        if len(self.offices) == 0:
            print (colored("\n\nThere are no rooms created yet\n\n", "red"))
            
        for office in self.offices:
            if len(self.offices) > 0:
                available_offices = []
                if len(office.occupants) < office.capacity:
                    available_offices.append(office)
                    selected_office = random.choice(available_offices)
                    selected_office.occupants.append(name)
                    print (colored("\n\n" +name + " has been allocated the office " + selected_office.room_name +".\n\n","blue"))
                    break


    def allocate_livingspace(self, name):
        """" This method allocates a living space to fellows who want accommodation"""
        for livingspace in self.livingspaces:
            
            if len(self.livingspaces) == 0:
                print (colored("\n\nThere are no livingspaces created yet.\n\n","red"))

            elif len(self.livingspaces) > 0:
                available_livingspace = []
                if len(livingspace.occupants) < livingspace.capacity:
                    available_livingspace.append(livingspace)
                    selected_livingspace = random.choice(available_livingspace)
                    selected_livingspace.occupants.append(name)
                    print (colored("\n\n"+ name + " has been allocated the livingspace " + selected_livingspace.room_name+"\n\n","blue"))
                    break
                    
                    






