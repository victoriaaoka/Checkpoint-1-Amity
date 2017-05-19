import unittest
import sys
import os
from tabulate import tabulate
from colorama import init
from termcolor import colored
from my_app.amity_class import Amity

class Test_amity(unittest.TestCase):
    """This class contains methods used to perform unit tests for the class Amity."""

    def setUp(self):
        self.amity = Amity()

    def test_room_created_successfully_output(self):
        """Tests that an office, Val has been created successfully."""
        result = self.amity.create_room("office", "val")
        self.assertEqual(result.room_name, "val")

    def test_create_room_with_wrong_room_type(self):
        """Tests the creation of a room that is neither an office nor a living space."""
        result = self.amity.create_room("game_room", "Blue")
        self.assertEqual(result, "Invalid room type!")

    def test_raise_error_if_room_type_is_not_string(self):
        """Tests if a type error is raised when room_type is not of type string."""
        with self.assertRaises(TypeError, msg="Use string input only"):
            blue_office = self.amity.create_room(201,"Blue")

    def test_raise_error_if_room_name_is_not_string(self):
        """Tests if a type error is raised when room_name is not of type string."""
        with self.assertRaises(TypeError, msg="Use string input only"):
            blue_office = self.amity.create_room("Office",101)

    def test_add_staff_successfully_output(self):
        """Tests that a staff member has been added successfully."""
        result = self.amity.add_person(person_id = "AND100", name = "Victoria Aoka", person_type = "Staff")
        self.assertEqual(result, "Added successfully")

    def test_add_fellow_successfully(self):
        """Tests that a fellow has been added successfully."""
        result = self.amity.add_person("AND105", "George Wafula", "Fellow")
        self.assertEqual(result, "Added successfully")

    def test_for_person_id_not_string(self):
        """Tests if a type error is raised when person_id is not of type string."""
        with self.assertRaises(TypeError, msg="Use input type of string only"):
            self.amity.add_person(100, "Aoka Victoria", "fellow", "Y")

    def test_for_person_name_not_string(self):
        """Tests if a type error is raised when person_name is not of type string."""
        with self.assertRaises(TypeError, msg="Use input type of string only"):
            self.amity.add_person("AND100", 100, "fellow", "Y")

    def test_for_person_type_not_string(self):
        """Tests if a type error is raised when person_type/ role is not of type string."""
        with self.assertRaises(TypeError, msg="Use input type of string only"):
            self.amity.add_person("AND100", "Aoka Victoria", 100, "Y")

    def test_for_person_type_not_fellow_or_staff(self):
        """Tests the addition of people who are neither staff or fellows."""
        aoka = self.amity.add_person("AND100", "Aoka Victoria", "Cook")
        self.assertEqual(aoka, "Wrong person_type! A person can only be a staff or fellow")

    def test_for_add_person_without_id(self):
        """Tests the addition of a user without an ID number."""
        aoka = self.amity.add_person(" ", "Aoka Victoria", "Cook")
        self.assertEqual(aoka, "Wrong person_type! A person can only be a staff or fellow")

    def test_print_room_successfully(self):
        """Tests output produced by print_room method."""
        room = self.amity.create_room("office", "Red")
        self.amity.add_person("AND100", "Aoka Victoria", "staff")
        self.amity.add_person("AND200", "Jimmy Scott", "fellow")
        result = self.amity.print_room("red")
        table = enumerate(room.occupants, start = 1)
        expected_output = print ("\n\n" + tabulate(table, headers=[room.room_name], tablefmt="fancy_grid"))
        self.assertEqual(result, expected_output)

    def test_print_empty_room(self):
        """Tests the printing of an empty room."""
        office_red = self.amity.create_room("office", "Red")
        result = self.amity.print_room("red")
        self.assertEqual(result, "The room has no occupants")

    def test_print_a_room_that_does_not_exist(self):
        """Tests the output of printing a room that does not exist."""
        result = self.amity.print_room("java")
        expected_output = print(colored("\nThe room java does not exist!\n" ,"red"))
        self.assertEqual(result, expected_output)

    def test_load_empty_file(self):
        """Tets loading people from an empty txt file."""
        result = self.amity.load_people("empty_file")
        expected_output = print(colored("\n\nThe file empty_file.txt is empty!\n","yellow"))
        self.assertEqual(result, expected_output)

    def test_load_people_from_an_existing_file(self):
        """Tests successful loading of people from an existing txt file."""
        self.amity.load_people("names")
        self.assertTrue(os.path.isfile("names.txt"))

    def test_allocate_office_successfully(self):
        """Tets successful office allocation to new staff and fellows."""
        office = self.amity.create_room("office", "Java")
        self.amity.add_person("AND100", "Aoka Victoria", "staff")
        self.amity.add_person("AND200", "Jimmy Scott", "fellow")
        self.assertEqual(len(office.occupants), 2)

    def test_allocate_a_full_livingspace(self):
        """Tests allocation of a fellow to a living space that is fully occupied"""
        dojo_lv = self.amity.create_room("livingspace", "Dojo")
        self.amity.add_person("AND100", "Aoka Victoria", "fellow", "Y")
        self.amity.add_person("AND200", "Jimmy Scott", "fellow", "Y")
        self.amity.add_person("AND300", "Geo Green", "fellow", "Y")
        self.amity.add_person("AND400", "Adrian Otieno", "fellow", "Y")
        result = self.amity.add_person("AND500", "Daisy Macharia", "fellow", "Y")
        self.assertEqual(result, "There are no available living spaces! Added to waiting List")

    @unittest.skip("WIP")
    def test_successful_room_reallocation(self):
        """Test  correct office reallocation"""
        self.amity.create_room("office","Python")
        self.amity.add_person("AND100", "Aoka Victoria", "fellow")
        self.amity.create_room("office", "Docopt")
        result = self.amity.reallocate_person("AND100", "Docopt")
        self.assertEqual(result, "Reallocation successful!")

    @unittest.skip("WIP")
    def test_reallocation_to_same_room(self):
        """Test for reallocation to a full office"""
        self.amity.create_room("office","Python")
        self.amity.add_person("AND100", "Aoka Victoria", "fellow")
        result = self.amity.reallocate_person("AND100", "Python")
        self.assertEqual(result, "Person cannot be reallocated the same room!")

    @unittest.skip("WIP")
    def test_reallocate_a_Person_not_registered(self):
        """Test for reallocating a person that is not registered"""
        self.amity.create_room("office", "Pacific")
        self.amity.add_person("AND100", "Joseph Kachulio", "Fellow", "Y")
        self.amity.create_room("office", "Victoria")
        result = self.amity.reallocate_person("AND200", "Victoria")
        self.assertEqual(result, "The person does not exist!")

    @unittest.skip("WIP")
    def test_reallocate_to_a_room_not_available(self):
        """Test reallocation tla room that does not exist"""
        self.amity.create_room("office", "Guruz")
        self.amity.add_person("AND222", "Mac Felix", "staff")
        result = self.amity.reallocate_person("AND222", "mordor")
        self.assertEqual(result, "The room mordor does not exist.")

    @unittest.skip("WIP")
    def test_reallocate_a_person_without_a_room(self):
        """Test for reallocating a person who doesn't have a room yet"""
        self.amity.add_person("AND200", "Aoka Victoria", "fellow")
        result = self.amity.reallocate_person("AND200", "Tsavo")
        self.assertEqual(result, "The person, id: AND200 has not been allocated any room yet!")

    @unittest.skip("WIP")
    def test_reallocate_from_office_to_livingspace(self):
        """Tests reallocation from an office to a living space"""
        self.amity.create_room("office", "Mara")
        self.amity.add_person("AND111", "Judith Aoka", "fellow")
        self.amity.create_room("livingspace", "Bakhita")
        result = self.amity.reallocate_person("AND111", "Bakhita")
        self.assertEqual(result, "Failed! You can only perform an office - office or livingspace - livingspace reallocation.")

    @unittest.skip("WIP")
    def test_reallocate_from_livingspace_to_office(self):
        """Tests for reallocation from livingspace to office."""
        self.amity.create_room("livingspace", "Lux")
        self.amity.add_person("AND111", "Judith Aoka", "fellow")
        self.amity.create_room("office", "java")
        result = self.amity.reallocate_person("AND111", "java")
        self.assertEqual(result, "Failed! You can only perform an office - office or livingspace - livingspace reallocation.")

    @unittest.skip("WIP")
    def test_print_unallocated(self):
        """Tests the conents of the print_allocations method."""
        self.amity.add_person("AND333", "Kevin Tumbo", "Fellow", 'Y')
        result = self.amity.print_unallocated("file_name")
        self.assertEqual(result, "Unallocated list saved successfully!")

    @unittest.skip("WIP")
    def test_print_allocations_successfully(self):
        """Tests the contents of the print_allocations file."""
        dojo_lv = self.amity.create_room("livingspace", "Dojo")
        self.amity.add_person("AND100", "Aoka Victoria", "fellow", "Y")
        self.amity.add_person("AND200", "Jimmy Scott", "fellow", "Y")
        self.amity.add_person("AND300", "Geo Green", "fellow", "Y")
        self.amity.add_person("AND400", "Adrian Otieno", "fellow", "Y")
        result = self.amity.print_allocations("file_name")
        self.assertEqual(result, "Allocations saved successfully!")

if __name__ == "__main__":
    unittest.main()
