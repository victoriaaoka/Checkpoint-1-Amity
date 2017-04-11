import unittest
import sys
sys.path.append('../')
from my_app.dojo_class import *

class Test_create_room(unittest.TestCase):
    
    def setUp(self):
        self.room = Dojo()

    def test_room_created_successfully_output(self):
        result = self.room.create_room(room_name = "Emerald", room_type = "Living Space")
        self.assertEqual(result, msg = "A Living Space called Emerald has been successfully created!")

    def test_create_room_without_room_name(self):
        result = self.room.create_room(room_name = "", room_type = "Office")
        self.assertEqual(result, msg = "Invalid room name")

    def test_create_room_with_wrong_room_type(self):
        result = self.room.create_room(room_name="Blue", room_type="Recreation Room")
        self.assertEqual(result, msg = "Invalid room name")

    def test_create_room_successfully(self):
        blue_office = self.room.create_room("Blue","Office")
        self.assertTrue(blue_office)

    def test_room_count(self):
        
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_raise_error_if_input_is_not_string(self):
        with self.assertRaises(TypeError, msg = "Use string input only"):
            blue_office = self.room.create_room(201,"Office")

class Test_add_person(unittest.TestCase):
    def setup(self):
        self.staff = Staff()
        self.fellow = Fellow()
        
    def test_add_staff_successfully_output(self):
        result = self.staff.add_person(person_id = "AND100", name = "Victoria Aoka", person_type = "Staff")
        self.assertEqual(result, msg = "Staff Victoria Aoka has been successfully added.")

    def test_add_fellow_successfully(self):
        result = self.fellow.add_person(person_id = "AND105", name="George Wafula", person_type="Fellow")
        self.assertEqual(result, msg = "Fellow George Wafula has been successfully added")    
                                        
    def test_for_input_not_string(self):
        with self.assertRaises(TypeError, msg = "Allow string input only"):
            Fellow("AND150" ,1000, "fellow", "Y")
    
    
if __name__ == '__main__':
    unittest.main()

    

        

    
