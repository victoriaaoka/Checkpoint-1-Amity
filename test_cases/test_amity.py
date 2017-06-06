import unittest
import sys
import os
from tabulate import tabulate
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

    def test_raise_error_if_room_name_is_not_string(self):
        """Tests if a type error is raised when room_name is not of type string."""
        result = self.amity.create_room("Office", "101")
        self.assertEqual(result, "Room_name must be of type string!")

    def test_add_staff_successfully_output(self):
        """Tests that a staff member has been added successfully."""
        result = self.amity.add_person(person_id = "100",
            person_name = "Victoria Aoka", person_type = "Staff")
        self.assertEqual(result, "Added successfully!")

    def test_add_fellow_successfully(self):
        """Tests that a fellow has been added successfully."""
        result = self.amity.add_person("105", "George Wafula", "Fellow")
        self.assertEqual(result, "Added successfully!")

    def test_for_person_id_not_number(self):
        """Tests if a type error is raised when person_id is not of type integer/ ad digit."""
        result = self.amity.add_person("and", "Aoka Victoria", "fellow", "Y")
        self.assertEqual(result, "Person_id can only be number!")

    def test_for_person_name_not_string(self):
        """Tests if a type error is raised when person_name is not of type string."""
        result = self.amity.add_person("100", "v200 100", "fellow", "Y")
        self.assertEqual(result, "Person_name must be of type string!")

    def test_for_person_type_not_string(self):
        """Tests if a type error is raised when person_type/ role is not of type string."""
        result = self.amity.add_person("100", "Aoka Victoria", "100", "Y")
        self.assertEqual(result, "Person_type must be of type string!")

    def test_for_person_type_not_fellow_or_staff(self):
        """Tests the addition of people who are neither staff or fellows."""
        result = self.amity.add_person("100", "Aoka Victoria", "Cook")
        self.assertEqual(result, "Wrong person_type! \
A person can only be a staff or fellow")

    def test_print_room_successfully(self):
        """Tests output produced by print_room method."""
        room = self.amity.create_room("office", "Red")
        self.amity.add_person("100", "Aoka Victoria", "staff")
        self.amity.add_person("200", "Jimmy Scott", "fellow")
        result = self.amity.print_room("red")
        table = enumerate(room.occupants, start = 1)
        expected_output = print ("\n\n" + tabulate(table,
            headers=[room.room_name], tablefmt="fancy_grid"))
        self.assertEqual(result, expected_output)

    def test_print_empty_room(self):
        """Tests the printing of an empty room."""
        office_red = self.amity.create_room("office", "Red")
        result = self.amity.print_room("red")
        self.assertEqual(result, "The room has no occupants")

    def test_print_a_room_that_does_not_exist(self):
        """Tests the output of printing a room that does not exist."""
        result = self.amity.print_room("java")
        self.assertEqual(result, "The room does not exist!")

    def test_load_empty_file(self):
        """Tets loading people from an empty txt file."""
        result = self.amity.load_people("empty_file")
        expected_output = print(
            colored("\n\nThe file empty_file.txt is empty!\n","yellow"))
        self.assertEqual(result, expected_output)

    def test_load_people_from_an_existing_file(self):
        """Tests successful loading of people from an existing txt file."""
        self.amity.load_people("names")
        self.assertTrue(os.path.isfile("names.txt"))

    def test_allocate_office_successfully(self):
        """Tets successful office allocation to new staff and fellows."""
        office = self.amity.create_room("office", "Java")
        self.amity.add_person("100", "Aoka Victoria", "staff")
        self.amity.add_person("200", "Jimmy Scott", "fellow")
        self.assertEqual(len(office.occupants), 2)

    def test_successful_room_reallocation(self):
        """Test  correct office reallocation"""
        self.amity.create_room("office","Python")
        self.amity.add_person("100", "Aoka Victoria", "fellow")
        self.amity.create_room("office", "Docopt")
        result = self.amity.reallocate_person("100", "Docopt")
        self.assertEqual(result, "Successfully reallocated!")

    def test_reallocation_to_same_room(self):
        """Test for reallocation to a full office"""
        self.amity.create_room("office","Python")
        self.amity.add_person("100", "Aoka Victoria", "fellow")
        result = self.amity.reallocate_person("100", "Python")
        self.assertEqual(result, "The person is in the room! \
Reallocation can not be to same room.")

    def test_reallocate_a_Person_not_registered(self):
        """Test for reallocating a person that is not registered"""
        self.amity.create_room("office", "Pacific")
        self.amity.add_person("100", "Joseph Kachulio", "Fellow", "Y")
        self.amity.create_room("office", "Victoria")
        result = self.amity.reallocate_person("200", "Victoria")
        self.assertEqual(result, "The person does not exist.")

    def test_reallocate_to_a_room_not_available(self):
        """Test reallocation tla room that does not exist"""
        self.amity.create_room("office", "Guruz")
        self.amity.add_person("222", "Mac Felix", "staff")
        result = self.amity.reallocate_person("222", "mordor")
        self.assertEqual(result, "The room does not exist.")

    def test_reallocate_a_person_without_a_room(self):
        """Test for reallocating a person who doesn't have a room yet"""
        self.amity.add_person("200", "Aoka Victoria", "fellow")
        self.amity.create_room("office", "Tsavo")
        result = self.amity.reallocate_person("200", "Tsavo")
        self.assertEqual(result,
            "The person does not have any room currently. \
Please use allocate_unallocated.")

    def test_reallocate_from_office_to_livingspace(self):
        """Tests reallocation from an office to a living space"""
        self.amity.create_room("office", "Mara")
        self.amity.add_person("111", "Judith Aoka", "fellow")
        self.amity.create_room("livingspace", "Bakhita")
        result = self.amity.reallocate_person("111", "Bakhita")
        self.assertEqual(result, "The person has not been \
allocated a livingspace yet.")

    def test_reallocate_from_livingspace_to_office(self):
        """Tests for reallocation from livingspace to office."""
        self.amity.create_room("livingspace", "Lux")
        self.amity.add_person("111", "Judith Aoka", "fellow", "y")
        self.amity.create_room("office", "java")
        result = self.amity.reallocate_person("111", "java")
        self.assertEqual(result, "The person does not have any room currently. \
Please use allocate_unallocated.")

    def test_print_unallocated(self):
        """Tests the contents of the print_allocations method."""
        self.amity.add_person("333", "Kevin Tumbo", "Fellow", 'Y')
        result = self.amity.print_unallocated("file_name")
        self.assertEqual(result, "Unallocations successfully saved.")

    def test_print_allocations_successfully(self):
        """Tests the contents of the print_allocations file."""
        self.amity.create_room("livingspace", "Dojo")
        self.amity.add_person("100", "Aoka Victoria", "fellow", "Y")
        self.amity.add_person("200", "Jimmy Scott", "fellow", "Y")
        self.amity.add_person("300", "Geo Green", "fellow", "Y")
        self.amity.add_person("400", "Adrian Otieno", "fellow", "Y")
        result = self.amity.print_allocations("file_name")
        self.assertEqual(result, "Allocations saved successfully!")

    def test_allocate_unallocated_person_an_office_successfully(self):
        """Tests the allocation of an office to a person in the waitinglist."""
        self.amity.add_person("122", "Will Smith", "fellow")
        self.amity.create_room("office", "Java")
        result = self.amity.allocate_unallocated_office("122")
        self.assertEqual(result, "Allocation successful!")

    def test_allocate_unallocated_person_a_livingspace_successfully(self):
        """Tests the allocation of a livingspace to a person in the waitinglist."""
        self.amity.add_person("122", "Will Smith", "fellow", "y")
        self.amity.create_room("livingspace", "Lux")
        result = self.amity.allocate_unallocated_livingspace("122")
        self.assertEqual(result, "Allocation successful!")

    def test_allocate_unallocated_to_room_not_office_or_livingspace(self):
        """Tests the allocation of a room that is neither an office or livingspace."""
        self.amity.add_person("122", "Will Smith", "fellow", "y")
        result = self.amity.allocate_unallocated("122", "game_room")
        self.assertEqual(result, "A person can only be allocated an office \
or a livingspace.")

    def test_deallocate_person_not_registered(self):
        """Tests the disallocation of a person not registered."""
        result = self.amity.deallocate_person("2789", "office")
        self.assertEqual(result,"The person is not registered yet.")

    def test_deallocate_person_not_assigned_an_office(self):
        """Tests the disallocation of a person not assigned an office."""
        self.amity.add_person("1", "Max Black", "fellow")
        result = self.amity.deallocate_person("1", "office")
        self.assertEqual(result, "The person has not been allocated any office.")

    def test_deallocate_person_not_assigned_a_livingspace(self):
        """Tests the disallocation of a person not assigned a livingspace."""
        self.amity.add_person("1", "Max Black", "fellow", "y")
        result = self.amity.deallocate_person("1", "livingspace")
        self.assertEqual(result, "The person has not been allocated any livingspace.")

    def test_disallocation_can_only_be_from_an_office_or_livingspace(self):
        """
        Tests the disallocation of a person from a room that is neither
        an office or a livingspace.
        """
        self.amity.create_room("office", "mongo")
        self.amity.add_person("1", "Max Black", "fellow")
        result = self.amity.deallocate_person("1", "game_room")
        self.assertEqual(result, "A person can only be deallocated from an office \
or a livingspace.")

    def test_deallocate_person_successfully(self):
        """Tests for successful disallocation of a person from an office."""
        ninjaz = self.amity.create_room("office", "Ninjaz")
        self.amity.add_person("123", "Aoka Victoria", "fellow")
        self.amity.add_person("345", "Debon Vanmou", "fellow")
        self.amity.add_person("98", "Max Black", "staff")
        self.amity.add_person("1000", "Carolyn Chaning", "fellow")
        result = self.amity.deallocate_person("123", "office")
        self.assertEqual(result, "Person deallocated successfully!")
        self.assertEqual(len(ninjaz.occupants), 3)

    def test_delete_person_not_registered(self):
        """Tests the deletion of a person not registered."""
        result = self.amity.delete_person("300")
        self.assertEqual(result, "The person does not exist.")

    def test_delete_person_successcully(self):
        """Tests for successful deletion of a person from the Amity system."""
        java = self.amity.create_room("office", "Java")
        self.amity.add_person("123", "Robert Burale", "staff")
        self.amity.add_person("234", "Carol Radul", "fellow")
        self.amity.delete_person("123")
        self.assertEqual(len(java.occupants), 1)

    def test_delete_room_not_created(self):
        """Tests for successful deletion of a room from the Amity system."""
        result = self.amity.delete_room("Dakar")
        self.assertEqual(result, "The room does not exist.")

    def test_delete_empty_room_successfully(self):
        """Tests for successful deletion of an empty room from the Amity system."""
        self.amity.create_room("office", "Val")
        self.amity.create_room("office", "Django")
        result = self.amity.delete_room("Val")
        self.assertEqual(result, "Room deleted successfully!")
        self.assertEqual(len(self.amity.offices), 1)

    def test_delete_room_that_has_occupants(self):
        """Tests for successful deletion of a room that has occupants."""
        self.amity.create_room("Livingspace", "Luxury")
        self.amity.add_person("167", "Ciccy Boke", "fellow", "Y")
        self.amity.add_person("098", "Christine Shiku", "fellow", "y")
        result = self.amity.delete_room("Luxury")
        self.assertEqual(result, "Room deleted successfully!")
        self.assertEqual(len(self.amity.livingspace_waitinglist), 2)

    def test_save_and_load_room_data_to_and_from_DB(self):
        """
        Tests for successful saving and loading of room data
        to and from a database.
        """
        java = self.amity.create_room("office", "Java")
        pacific = self.amity.create_room("livingspace", "Pacific")
        self.amity.add_person("1234", "Judith Gathua", "staff")
        self.amity.add_person("123", "Macdonald Felix", "fellow", "Y")
        self.amity.add_person("554", "Godwin Karanja", "fellow", "y")
        self.amity.save_state("Amitydb")
        self.amity.load_state("Amitydb")
        self.assertEqual(len(java.occupants), 3)
        self.assertEqual(len(pacific.occupants), 2)

    def test_save_and_load_people_data_to_and_from_DB(self):
        """
        Tests for successful saving and loading of people data
        to and from a database.
        """
        self.amityy = Amity()
        lux = self.amity.create_room("office", "lux")
        self.amityy.add_person("1234", "Judith Gathua", "staff")
        self.amityy.add_person("123", "Macdonald Felix", "fellow", "Y")
        self.amityy.add_person("554", "Godwin Karanja", "fellow", "y")
        self.amityy.save_state("newdb")
        self.amity.load_state("newdb")
        self.assertEqual(len(self.amityy.people), 3)

    def test_load_data_from_a_file_that_does_not_exist(self):
        """Tests for loading of data from a database that does not exist."""
        result = self.amity.load_state("nonexistingdb")
        self.assertEqual(result, "The database does not exist!")

if __name__ == "__main__":
    unittest.main()
