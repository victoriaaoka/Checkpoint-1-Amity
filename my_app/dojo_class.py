from room_class import Room, OfficeSpace, LivingSpace
from person_class import Person, Fellow, Staff
class Dojo():
    
    def __init__(self):
        self.all_fellows = []
        self.all_staff = []
        self.offices = []
        self.livingspaces = []

    def create_room(self,room_type, room_name):
        """This function creates rooms based on a user's input.
        Rooms can either be an office or a living space.
        """
        if not isinstance(room_type, str) or not isinstance(room_name,str):
            raise TypeError("Use input of type string only")
        elif isinstance(room_type,str) and isinstance(room_name,str):
            if room_type.lower() == "office":
                new_office = OfficeSpace()
                created_office = new_office.create_room(room_type, room_name)
                self.offices.append(new_office)
                print ("An office called " + room_name + " has been successfully created!")
                #print (created_office.room_name)
                #print (created_office.capacity)
                return self

            elif room_type.lower() == "living space":
                new_livingspace = LivingSpace()
                created_livingspace = new_livingspace.create_room(room_type, room_name)
                self.livingspaces.append(created_livingspace)
                print ("A living space called " +room_name+" has been successfully created")
            elif room_type.lower() != "office" or room_type.lower() != "living_space":
                return "Wrong room_type! rooms can only be offices or living spaces"
        else:
            return "Error"

    def add_person(self, person_id, name, person_type, wants_accom = "N"):
            """This function adds a new fellow or staff into the system"""            
            if not isinstance(person_id, str) or not isinstance(name,str) or not isinstance(person_type,str):
                raise TypeError("Use input type of string only")
            
            elif isinstance(person_id, str) and isinstance(name, str) and isinstance(person_type, str):
                if person_type.lower() == "fellow":
                    new_fellow = Fellow()
                    added_fellow = new_fellow.add_person(person_id, name, person_type, wants_accom)
                    self.all_fellows.append(added_fellow)
                    print ("Fellow " + name +" has been successfully added.")

                elif person_type.lower() == "staff":
                    new_staff = Staff()
                    added_staff = new_staff.add_person(person_id, name, person_type)
                    self.all_staff.append(added_staff)
                    print ("Staff " + name + "  has been successfully added.")                    
                    
                    
                    
                    

dojo = Dojo()
dojo.create_room("office", "Acacia")
dojo.create_room("Living Space", "Tsavo")
dojo.add_person("AND100", "Aoka", "Fellow", "Y")
dojo.add_person("AND105", "Victoria", "Staff")




