
class Room(object):
        """Room class describes the characteristics of each
        instance of a room created
        """
        def __init__(self, room_type = "", room_name = ""):
                self.room_name = room_name
                self.room_type = room_type
                self.occupants = []
                #return self

class OfficeSpace(Room):
        """This class defines an instance of each Office
        and inherits from Room class
        """
        def __init__(self, room_type = "", room_name = "", occupants=[]):
                super(OfficeSpace, self).__init__(room_type, room_name)
                self.room_type = room_type
                self.room_name = room_name
                self.occupants = []
                self.capacity = 6
                #return self

class LivingSpace(Room):
        """This class defines an instance of each Livingspace
        and inherits from Room class
        """
        def __init__(self,room_type = "", room_name = "", occupants=[]):
                super(LivingSpace, self).__init__(room_name)
                self.room_type = room_type
                self.room_name = room_name
                self.occupants = []
                self.capacity = 4
                #return self



