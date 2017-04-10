import unittest
from room_class import *
class RoomTest(unittest.TestCase):
    """Test cases for the Room, officespace and livingspace classes.
    """
    def test_room_instance(self):
        Blue = Room("Blue")
        self.assertIsInstance(Blue, Room, msg="The object should be an instance of the Room class")

    

if __name__ == '__main__':
    unittest.main()
        
