import unittest
import sys
sys.path.append('../')
from my_app.amity_class import *



class Test_amity(unittest.TestCase):

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

    def test_raise_error_if_room_type_is_not_string(self):
        with self.assertRaises(TypeError, msg="Use string input only"):
            blue_office = self.amity.create_room(201,"Blue")

    def test_raise_error_if_room_name_is_not_string(self):
        with self.assertRaises(TypeError, msg="Use string input only"):
            blue_office = self.amity.create_room("Office",101)

    def test_add_staff_successfully_output(self):
        result = self.amity.add_person(person_id = "AND100", name = "Victoria Aoka", person_type = "Staff")
        self.assertEqual(result, "Added successfully")

    def test_add_fellow_successfully(self):
        result = self.amity.add_person("AND105", "George Wafula", "Fellow")
        self.assertEqual(result, "Added successfully")

    def test_for_person_id_not_string(self):
        with self.assertRaises(TypeError, msg="Use input type of string only"):
            self.amity.add_person(100, "Aoka Victoria", "fellow", "Y")

    def test_for_person_name_not_string(self):
        with self.assertRaises(TypeError, msg="Use input type of string only"):
            self.amity.add_person("AND100", 100, "fellow", "Y")

    def test_for_person_person_type_not_string(self):
        with self.assertRaises(TypeError, msg="Use input type of string only"):
            self.amity.add_person("AND100", "Aoka Victoria", 100, "Y")

    def test_for_person_type_not_fellow_or_staff(self):
        aoka = self.amity.add_person("AND100", "Aoka Victoria", "Cook")
        self.assertEqual(aoka, "Wrong person_type! A person can only be a staff or fellow")

    def test_for_add_person_without_id(self):
         aoka = self.amity.add_person(" ", "Aoka Victoria", "Cook")
         self.assertEqual(aoka, "Wrong person_type! A person can only be a staff or fellow")

    def test_print_allocations_successfully(self):
        room = self.amity.create_room("office", "Red")
        self.amity.add_person("AND100", "Aoka Victoria", "staff")
        self.amity.add_person("AND200", "Jimmy Scott", "fellow")
        result = self.amity.print_room("red")
        table = enumerate(room.occupants, start = 1)
        expected_output = print ("\n\n" + tabulate(table, headers=[room.room_name], tablefmt="fancy_grid"))
        self.assertEqual(result, expected_output)

    def test_print_empty_room(self):
        office_red = self.amity.create_room("office", "Red")
        result = self.amity.print_room("red")
        self.assertEqual(result, "The room has no occupants")

    def test_print_a_room_that_does_not_exist(self):
        result = self.amity.print_room("java")
        expected_output = print(colored("\nThe room java does not exist!\n" ,"red"))
        self.assertEqual(result, expected_output)

    def test_load_empty_file(self):
        result = self.amity.load_people("empty_file")
        expected_output = print(colored("\n\nThe file empty_file.txt is empty!\n","yellow"))
        self.assertEqual(result, expected_output)


    def test_load_people_from_an_existing_file(self):
        self.amity.load_people("names")
        self.assertTrue(os.path.isfile("names.txt"))


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
