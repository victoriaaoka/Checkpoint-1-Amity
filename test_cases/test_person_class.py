import unittest
import sys
sys.path.append('../')
from my_app.person_class import Person, Staff, Fellow

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.fellow = Fellow("Victoria Aoka", "fellowstaff" "M")
        self.staff = Staff("Isaiah", "fellowstaff")

    def test_fellow_person_type(self):
        self.assertEqual( self.fellow.person_type, "Fellow" ,
                          msg = "Invalid person_type specified")

    def test_staff_person_type(self):
        self.assertEqual( self.staff.person_type, "Staff" ,
                          msg = "Invalid person_type specified")

    def test_invalid_accomodation_option(self):
        self.assertEqual(self.fellow.wants_accom,'N' or 'Y',
                         msg = "Invalid option, wants accommodation can only be 'y' or 'N'")


if __name__ == '__main__':
    unittest.main()
