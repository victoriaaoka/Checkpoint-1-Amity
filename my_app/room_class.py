class Room(object):
	"""Room class describes the characteristics of each 
	instance of a room created
	"""
	def __init__(self, name):
		self.name = name
		self.occupants = []


class OfficeSpace(Room):
	"""This class defines an instance of each Office
	and inherits from Room class
	"""
	def __init__(self, name):
		super(OfficeSpace, self).__init__(name)
		self.room_type = "OFFICE"
		self.capacity = 6	
		

class LivingSpace(Room):
	"""This class defines an instance of each Livingspace
	and inherits from Room class
	"""
	def __init__(self, name):
		super(LivingSpace, self).__init__(name)
		self.room_type = "LIVING SPACE"
		self.capacity = 4
