import random
from room_class import Room, OfficeSpace, LivingSpace
from person_class import Person, Fellow, Staff
class Dojo():
    
    def __init__(self):
        self.all_fellows = []
        self.all_staff = []
        self.offices = []
        self.livingspaces = []
        

    def create_room(self,room_type, room_name):
        """This method creates rooms based on a user's input.
        Rooms can either be an office or a living space.
        """
        if not isinstance(room_type, str) or not isinstance(room_name,str):
            raise TypeError("\n\nUse input of type string only\n\n")
        
        elif isinstance(room_type,str) and isinstance(room_name,str):
            if room_type.lower() == "office":
                new_office = OfficeSpace(room_type, room_name)
                self.offices.append(new_office)
                print ("\n\nAn office called " + room_name + " has been successfully created!\n\n")
                return self

            elif room_type.lower() == "livingspace":
                new_livingspace = LivingSpace(room_type, room_name)
                self.livingspaces.append(new_livingspace)
                print ("\n\nA living space called " +room_name+" has been successfully created\n\n")
                return self
                
            elif room_type.lower() != "office" or room_type.lower() != "living_space":
                return "\n\nWrong room_type! rooms can only be offices or living spaces\n\n"
        else:
            return "Error"

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
                print ("\n\nFellow " + name +" has been successfully added.\n\n")
                self.allocate_office(name)
                if wants_accom == "Y":
                    self.allocate_livingspace(name)

            elif person_type.lower() == "staff":
                new_staff = Staff(person_id, name, person_type)
                self.all_staff.append(new_staff)
                print ("\n\nStaff " + name + "  has been successfully added.\n\n")
                self.allocate_office(name)
                    
    def allocate_office(self, name):
        """This function allocates a random office to a fellow and staff"""
        if len(self.offices) == 0:
            print ("\n\nThere are no rooms created yet\n\n")
            
        for office in self.offices:
            if len(self.offices) > 0:
                available_offices = []
                if len(office.occupants) < office.capacity:
                    available_offices.append(office)
                    selected_office = random.choice(available_offices)
                    selected_office.occupants.append(name)
                    print ("\n\n" +name + " has been allocated the office " + office.room_name +"\n\n")


    def allocate_livingspace(self, name):
        """" This method allocates a living space to fellows who want accommodation"""
        for livingspace in self.livingspaces:
            
            if len(self.livingspaces) == 0:
                print ("\n\nThere are no livingspaces created yet\n\n")

            elif len(self.livingspaces) > 0:
                available_livingspace = []
                if len(livingspace.occupants) < livingspace.capacity:
                    available_livingspace.append(livingspace)
                    selected_livingspace = random.choice(available_livingspace)
                    selected_livingspace.occupants.append(name)
                    print ("\n\n"+ name + " has been allocated the livingspace " + livingspace.room_name+"\n\n")  
                    
                    
dojo = Dojo()
#dojo.create_room("office", "Acacia")
#dojo.create_room("LivingSpace", "Tsavo")
dojo.add_person("AND100", "Aoka", "Fellow", "Y")
dojo.add_person("AND105", "Victoria", "Staff")





