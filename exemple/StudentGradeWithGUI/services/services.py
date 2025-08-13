from domain.validators import StudentValidator
from repository.inmemory import StudentRepository
from repository.inmemory import DuplicatedIDException
from domain.entities import Student
from domain.entities import Address
from domain.validators import ValidationException
class StudentService:
    """
      Class responsible with the use cases related to Student CRUD
      GRASP Controller
    """
    def __init__(self, val, repo):
        """
          Initialise the controller,
          controller need a validator and a repository to perform the operations
          val - StudentValidator (injected)
          repo - StudentRepository (injected
        """
        self.__val = val
        self.__repo = repo

    def create(self, id, name, street, nr, city):
        """
          Create validate and store a student
          id,name, street,city- strings
          nr - int
          return Student
          raise ValueEror if the data is invalid, on duplicated id
        """
        #create Student instance
        st = Student(id, name, Address(street,nr,city))
        #validate, raise exception if student is invalid
        self.__val.validate(st)
        #store the student, raise exception if duplicated id
        self.__repo.store(st)
        return st

    def getNrStudents(self):
        """
          Return the number of students
          return int
        """
        return self.__repo.size()

    def remove(self, id):
        """
         Remove student with the given id
         id - string, student id
         return Student, the removed Student
         raise ValueError if there is no student with the given id
        """
        return self.__repo.remove(id)
    def search(self, criteria):
        """
          Search students with name containing criteria
          criteria string
          return list of students, where the name contains criteria
        """
        all = self.__repo.getAll()
        if criteria=="":
            return all

        rez = []
        for st in all:
            if criteria in st.getName():
                rez.append(st)
        return rez

    def update(self, id, name, street, nr, city):
        """
          Update student with the given id
          id,name, adr strings
          return the old student
          raise ValueError if the student is invalid, if there is no student with the given id
        """
        newSt = Student(id, name, Address(street, nr, city))

        #validate the student
        self.__val.validate(newSt)

        #get the old student
        oldSt = self.__repo.find(id)

        #update the student
        self.__repo.update(id, newSt)
        return oldSt


def testCreateStudent():
    """
     test function for create student
     Feature 1 - add a student
     Task 4 - Create student - controller
    """
    #create the controller and inject the validator and repository
    ctr =  StudentService(StudentValidator(), StudentRepository())
    st = ctr.create("1", "Ion", "Adr", 1, "Cluj")
    assert st.getId()=="1"
    assert st.getName()=="Ion"
    assert st.getAdr().getStreet()=="Adr"
    assert ctr.getNrStudents()==1
    #test for an invalid student
    try:
        ctr.create("1", "", "", 1, "Cluj")
        assert False
    except ValidationException:
        assert True
    #test for duplicated id
    try:
        ctr.create("1", "Ion2", "Adr2", 1, "Cluj")
        assert False
    except DuplicatedIDException:
        assert True


testCreateStudent()

def testRemoveStudent():
    """
      Test function for remove
      Feature 2 - remove student
      Task 2 - remove student controller
    """
    ctr =  StudentService(StudentValidator(), StudentRepository())
    st = ctr.create("1", "Ion", "Adr", 1, "Cluj")
    #test for an invalid id
    try:
        ctr.remove("2")
        assert False
    except ValueError:
        assert True
    assert ctr.getNrStudents()==1

    st = ctr.remove("1")
    assert ctr.getNrStudents()==0
    assert st.getId()=="1"
    assert st.getName()=="Ion"
    assert st.getAdr().getStreet()=="Adr"



testRemoveStudent()

def testSearchCriteria():
    """
      test first search
      Feature 3 - List students for a criteria
      Task 2 - all students where the name contains a given string
    """
    ctr =  StudentService(StudentValidator(), StudentRepository())
    st = ctr.create("1", "Ion", "Adr", 1, "Cluj")
    st = ctr.create("2", "Ion2", "Adr", 1, "Cluj")
    st = ctr.create("3", "Ioana1", "Adr", 1, "Cluj")
    st = ctr.create("4", "Ioana2", "Adr", 1, "Cluj")
    st = ctr.create("5", "Vlad", "Adr", 1, "Cluj")

    studs = ctr.search("Ion")
    assert len(studs)==2
#     assert studs[0].getId()=="1"
#     assert studs[1].getName()=="Ion2"

    studs = ctr.search("Io")
    assert len(studs)==4
#     assert studs[3].getName()=="Ioana2"

    studs = ctr.search("Al")
    assert len(studs)==0

    #for empty string
    studs = ctr.search("")
    assert len(studs)==5


testSearchCriteria()

def testUpdate():
    """
     test function for update
     Feature 4 - update a student information
     Task 2 - update student - controller
    """
    ctr =  StudentService(StudentValidator(), StudentRepository())
    st = ctr.create("1", "Ion", "Adr", 1, "Cluj")
    st = ctr.update("1", "Ionel", "Addrr", 1, "Cluj")

    studs = ctr.search("Ionel")
    assert len(studs)==1
    assert studs[0].getAdr().getStreet()=="Addrr"
    #verify if the old student is returned
    assert st.getName()=="Ion"
    assert st.getAdr().getStreet()=="Adr"

    #try to opdate an inexistend student
    try:
        st = ctr.update("2", "Ionel", "Addrr", 1, "Cluj")
        assert False
    except ValueError:
        assert True

    #try to update to invalid data
    try:
        ctr.update("1", "", "", 1, "Cluj")
        assert False
    except ValidationException:
        assert True

testUpdate()