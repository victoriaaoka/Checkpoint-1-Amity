class Person(object):
    """
    This class describes the instance of person
    """
    def __init__(self, person_id="", person_name="", person_type=""):
        self.person_id = person_id
        self.person_name = person_name
        self.person_type = person_type
        self.people = []


class Fellow(Person):
    """This class inherits from the Person class
    and defines an instance of fellow"""
    def __init__(self, person_id="", person_name="", person_type="", wants_accom=""):
        super(Fellow, self).__init__(person_id, person_name, person_type)
        self.person_id = person_id
        self.person_name = person_name
        self.person_type = "Fellow"
        self.wants_accom = wants_accom


class Staff(Person):
    """This class inherits from the Person class
    and defines an instance of Person """
    def __init__(self, person_id="", person_name="", person_type="", wants_accom="N"):
        super(Staff, self).__init__(person_id, person_name, person_type)
        self.person_id = person_id
        self.person_name = person_name
        self.person_type = "Staff"
        self.wants_accom = "N"

