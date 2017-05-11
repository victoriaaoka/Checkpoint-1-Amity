import sys
import itertools
from tabulate import tabulate
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import random
from colorama import init
from termcolor import colored
init()
from person_class import Person, Fellow, Staff
from room_class import Room, OfficeSpace, LivingSpace

class Dojo():
    
    def __init__(self):
        self.all_fellows = []
        self.all_staff = []
        self.offices = []
        self.livingspaces = []
        self.fellow_and_staff_ids = []
        self.room_names = []
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
        #print(room_name)        
        
        else:

            if room_type.lower() == "office":
                new_office = OfficeSpace(room_type, room_name)                
                for room in self.offices:
                    self.room_names.append(room.room_name)
                if new_office.room_name in self.room_names:
                    print (colored("\n\nThe room name " + room_name + " already exists!\n\n", "red"))
                else:
                    self.offices.append(new_office)
                    print (colored("\n\nAn office called " + room_name + " has been successfully created!\n\n","blue"))
                    return self 

            elif room_type.lower() == "livingspace":
                new_livingspace = LivingSpace(room_type, room_name)
                for room in self.livingspaces:
                    self.room_names.append(room.room_name)
                if new_livingspace.room_name in self.room_names:
                    print (colored("\n\nThe room name " + room_name + " already exists!\n\n", "red"))
                else:
                    self.livingspaces.append(new_livingspace)
                    print (colored("\n\nA livingspace called " +room_name+" has been successfully created\n\n","blue"))
                    return self


    def add_person(self, person_id, name, person_type, wants_accom = "N"):
        """This method adds a new fellow or staff into the system.
        It also calls the allocate_livingspace and allocate_office method to assign the new staff and fellow rooms.
        """            
        if not isinstance(person_id, str) or not isinstance(name,str) or not isinstance(person_type,str):
            raise TypeError("\n\nUse input type of string only\n\n")

        elif person_type.lower() != "staff" and person_type.lower() != "fellow":
            print (colored("\n\nWrong person_type! A person can only be a staff or fellow\n\n","red" ))
   
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
                    return self


            elif person_type.lower() == "staff":
                
                new_staff = Staff(person_id, name, person_type)
                
                if new_staff.person_id in self.fellow_and_staff_ids:
                    print(colored("\n\nStaff " + new_staff.name + ", id: "+ new_staff.person_id +" already exists.\n\n","red"))
                
                else:
                    self.all_staff.append(new_staff)
                    self.fellow_and_staff_ids.append(person_id)
                    print (colored("\n\nStaff " + name + "  has been successfully added.\n\n", "blue"))
                    self.allocate_office(name)
                    return self
                    
    def allocate_office(self, name):
        """This method allocates a random office to a new fellow or staff"""
        if len(self.offices) == 0:
            print (colored("\n\nThere are no offices created yet\n\n", "red"))
             
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
            print (colored("\n\nThere are no living spaces created yet\n\n", "red"))     
        
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
        output = ""
        if not room_name.lower() in [room.room_name.lower() for room in itertools.chain(self.offices, self.livingspaces)]:
            print("\nThe room " + room_name+ " does not exist!\n" )

        else:
            for room in itertools.chain(self.offices, self.livingspaces):
                if room.room_name.lower() == room_name.lower():
                    table = enumerate(room.occupants, start = 1)
                    print ("\n\n" +tabulate(table, headers = [room_name], tablefmt = "fancy_grid"))
                    
                    
            
            
           
           
       

                
"""dojo = Dojo()
dojo.create_room("office", "Mara")
#dojo.create_room("office", "blue")
#dojo.create_room("office", "red")
dojo.create_room("livingspace", "Denvir")
dojo.create_room("livingspace", "Applex")
dojo.add_person("AND100", "Aoka Victoria", "staff")
dojo.add_person("AND102", "Aoka judith", "fellow", "Y")
dojo.add_person("AND103", "wangu Jane", "fellow", "Y")
dojo.add_person("AND104", "Jeff koinange", "staff")
dojo.add_person("AND106", "Geo mamboleo", "fellow", "Y")
dojo.add_person("AND105", "Geo graphy", "fellow", "Y")
dojo.add_person("AND107", "Geotumbo", "fellow", "Y")
dojo.print_room("Mara")
dojo.print_room("Denvir")
dojo.print_room("Applex")"""





                    







