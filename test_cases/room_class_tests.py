import unittest
import sys
sys.path.append('../')
from room_class import Room, OfficeSpace, LivingSpace


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.office_space = OfficeSpace("Blue")
        self.living_space = LivingSpace("Emerald")
        
    def test_officespace_is_a_room_instance(self):
        self.assertIsInstance(self.office_space, Room, msg = "The object should be an instance of the Room class")

    def test_livingspace_is_a_room_instance(self):
        self.assertIsInstance(self.living_space, Room, msg = "The object should be an instance of the Room class")

    def test_livingspace_type(self):
        self.assertEqual(self.living_space.room_type, "Living Space", msg = "Room Created should be of type 'Living Space'")

    def test_max_size_of_living_space(self):
        self.assertEqual(self.living_space.capacity, 4, msg = 'The Maximum capacity is 4 occupants')

    def test_officespace_room_type(self):
        self.assertEqual(self.office_space.room_type, "Office", msg = "Room created should be of type Office")

    def test_max_size_of_office_space(self):
        self.assertEqual(self.office_space.capacity, 6, msg ='The Maximum capacity is 6 occupants')

    def test_raise_error_if_input_is_not_string(self):
    	with self.assertRaises(TypeError, msg = 'Use string input only'):
    		Blue = Room(100)
    
if __name__ == '__main__':
    unittest.main()
