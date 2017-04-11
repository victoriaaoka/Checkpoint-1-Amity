from room_class import Room, OfficeSpace, LivingSpace
class Dojo():
    
    def __init__(self):
        self.fellows = []
        self.staff = []
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

my_room = Dojo()
my_room.create_room("office", "Acacia")
print (my_room.create_room("Living Space", "Tsavo"))

