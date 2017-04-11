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
            raise TypeError("bbb")
        elif isinstance(room_type,str) and isinstance(room_name,str):
            if room_type.lower() == "office":
                self.offices.append(room_name)
                return "An office called " + room_name + " has been successfully created!"

            elif room_type.lower() == "living space":
                self.livingspaces.append(room_name)
                return "A living space called " +room_name+" has been created"
            elif room_type.lower() != "office" or room_type.lower() != "living_space":
                return "Wrong room_type! rooms can only be offices or living spaces"
        else:
            return "Error"


    def add_person():
        pass

my_room = Dojo()
print (my_room.create_room("office", "Acacia"))
print (my_room.create_room("Living Space", "Tsavo")) 
