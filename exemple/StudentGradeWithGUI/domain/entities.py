class Address:
    """
      Represent an address
    """
    def __init__(self, street, nr, city):
        self.__street = street
        self.__nr = nr
        self.__city = city

    def getStreet(self):
        return self.__street

    def getNr(self):
        return self.__nr

    def getCity(self):
        return self.__city

    def __str__(self):
        """
          Give a string representation for the address
          return string
        """
        return self.__street+" nr."+self.__nr+" "+self.__city

class Student:
    """
      Represent a student
    """
    def __init__(self, id, name, adr):
        """
         Create a new student
         id, name String
         address - Address
        """
        self.__id = id
        self.__name = name
        self.__adr = adr

    def getId(self):
        """
          Getter method for id
        """
        return self.__id

    def getName(self):
        """
          Getter for name
        """
        return self.__name

    def getAdr(self):
        """
         Getter for address
        """
        return self.__adr
    def __str__(self):
        """
          Give a string representation for the student
          return string
        """
        return self.__id+" "+self.__name+" "+str(self.__adr)

    def __eq__(self, ot):
        """
          Define equal for students
          ot - student
          return True if ot and the current instance represent the same student
        """
        return self.__id==ot.__id

def testIdentity():
    #attributes may change
    st = Student("1", "Ion", Address("Adr", 1, "Cluj"))
    st2 = Student("1", "Ion", Address("Adr2", 1, "Cluj"))
    assert st==st2

    #is defined by its identity
    st = Student("1", "Popescu", Address("Adr", 1, "Cluj"))
    st2 = Student("2", "Popescu", Address("Adr2", 1, "Cluj"))
    assert st!=st2

testIdentity()



# testCreateStudent()

import unittest

class TestCaseEntitati(unittest.TestCase):

    def setUp(self):
        self.st = Student("1", "Ion", Address("Adr", 1, "Cluj"))

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testCreateStudent(self):
        """
          Testing student creation
          Feature 1 - add a student
          Task 1 - Create student
        """
        
        self.assertTrue(self.st.getId() == "1")
        self.assertEqual(self.st.getName() ,"Ion")
#         assert st.getAdr().getStreet() == "Adr"
    
#         st = Student("2", "Ion2", Address("Adr2", 1, "Cluj"))
#         assert st.getId() == "2"
#         assert st.getName() == "Ion2"
#         assert st.getAdr().getStreet() == "Adr2"
#         assert st.getAdr().getCity() == "Cluj"

if __name__ == '__main__':
    unittest.main()