import unittest
import sys
sys.path.append('../')
from my_app.amity_class import *



class Test_create_room(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def test_room_created_successfully_output(self):
        result = self.amity.create_room("office", "val")
        self.assertEqual(result.room_name, "val")

    def test_create_room_with_wrong_room_type(self):
        result = self.amity.create_room("game_room", "Blue")
        self.assertEqual(result, "Invalid room type!")

    def test_create_office_successfully(self):
        blue_office = self.amity.create_room("office", "blue")
        self.assertTrue(blue_office)

    def test_raise_error_if_input_is_not_string(self):
        with self.assertRaises(TypeError, msg="Use string input only"):
            blue_office = self.amity.create_room(201,"Office")

    def test_add_staff_successfully_output(self):
        result = self.amity.add_person(person_id = "AND100", name = "Victoria Aoka", person_type = "Staff")
        self.assertEqual(result, "Added successfully")

    def test_add_fellow_successfully(self):
        result = self.amity.add_person("AND105", "George Wafula", "Fellow")
        self.assertEqual(result, "Added successfully")

    def test_for_input_not_string(self):
        with self.assertRaises(TypeError, msg="\n\nUse input type of string only"):
            self.amity.add_person("And", 1000, "fellow", "Y")

class Test_reallocate_person(unittest.TestCase):
    """This class will test the method - reallocate person"""

    def test_successful_office_reallocation(self):
        """Test  correct office reallocation"""
        pass

    def test_successful_living_space_reallocation(self):
        """Test  correct living_space reallocation"""
        pass

    def test_reallocation_to_full_office(self):
        """Test for reallocation to a full office"""
        pass

    def test_reallocation_to_full_living_space(self):
        """Test for reallocation to a full living_space"""
        pass

    def test_reallocate_a_Person_not_registered(self):
        """Test for reallocating a person that is not registered"""
        pass

    def test_reallocate_a_person_without_a_room(self):
        """Test for reallocating a person who doesn't have a room yet"""
        pass
class Test_load_people(unittest.TestCase):
    """Test the load_people method"""
    def test_load_people_successfully(self):
        pass

    def test_load_empty_file(self):
        pass

class Test_print_allocations(unittest.TestCase):
    """Test the print_allocations method"""
    def test_print_allocations_successfully(self):
        pass

    def test_print_empty_room(self):
        pass

    def test_print_a_room_not_created(self):
        pass

class Test_print_unallocated(unittest.TestCase):
    """Test the print_unallocated method"""
    def test_successfully_print_unallocated(self):
        pass

class Test_print_room(unittest.TestCase):
    """Test the print_room method"""
    def test_print_room_successfully(self):
        pass

    def test_print_empty_room(self):
        pass

    def test_print_a_room_not_created(self):
        pass

class Test_save_state(unittest.TestCase):
    """Test the save_state method"""
    pass

class Test_load_state(unittest.TestCase):
    """Test the load_state method"""
    pass




if __name__ == '__main__':
    unittest.main()
