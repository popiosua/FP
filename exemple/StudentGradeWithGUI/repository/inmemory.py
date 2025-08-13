from domain.entities import Student
from domain.entities import Address
from domain.validators import StudentCRUDException

class RepositorException(StudentCRUDException):
    """
      Base class for the exceptions in the repository
    """
    def __init__(self, msg):
        self.__msg = msg
    def getMsg(self):
        return self.__msg
    def __str__(self):
        return self.__msg

class DuplicatedIDException(RepositorException):
    def __init__(self):
        RepositorException.__init__(self, "Duplicated ID")

class StudentRepository:
    """
      Class responsible for managing a list of students (store, retrieve , update, etc)
      GRASP - Pure Fabrication -  Repository Pattern
    """
    def __init__(self):
        self.__studs = {}

    def store(self,st):
        """
          Store a student
          st - student
          raise DuplicatedIDException for duplicated id
        """
        if st.getId() in self.__studs:
            raise DuplicatedIDException()
        self.__studs[st.getId()] = st

    def size(self):
        """
          return the number of students in the repository
        """
        return len(self.__studs)

    def remove(self,id):
        """
          remove a student from the repository
          id - string, the id of the student to be removed
          return student
          post: the repository not contains student with the given id
          raise ValueError if there is no student with the given id
        """
        if not id in self.__studs:
            raise ValueError("No student for the id:"+id)
        st = self.__studs[id]
        del self.__studs[id]
        return st
    def removeAll(self):
        """
          Remove all the students from the repository
        """
        self.__studs = {}

    def getAll(self):
        """
          Retrive all the students
          return a list with students
        """
        return list(self.__studs.values())

    def update(self,id,st):
        """
          Update student in the repository
          id - string, the id of the student to be updated
          st - Student, the updated student
          raise ValueError if there is no student with the given id
        """
        #remove the old student (this will raise exception if there is no student
        self.remove(id)
        #store the student
        self.store(st)

    def find(self,id):
        """
          Find the student for a given id
          id - string
          return student with the given id or None if there is no student with the given id
        """
        if not id in self.__studs:
            return None
        return self.__studs[id]

def testStoreStudent():
    """
      test function for store
      Feature 1 - add a student
      Task 3 - Store Student
    """
    st = Student("1", "Ion", Address("Adr", 1,"Cluj"))
    rep = StudentRepository()
    assert rep.size()==0
    rep.store(st)
    assert rep.size()==1
    st2 = Student("2", "Vasile", Address("Adr2", 1,"Cluj"))
    rep.store(st2)
    assert rep.size()==2
    #can not store 2 students with the same id
    st3 = Student("2", "Ana", Address("Adr3", 1,"Cluj"))
    try:
        rep.store(st3)
        assert False
    except DuplicatedIDException:
        pass

testStoreStudent()

def testDeleteStudent():
    """
      Test function for delete
      Feature 2 - delete student
      Task 1 - remove student from the repository
    """
    rep = StudentRepository()
    st = Student("1", "Ion", Address("Adr", 1,"Cluj"))
    rep.store(st)
    st = Student("2", "Ion2", Address("Adr2", 1,"Cluj"))
    rep.store(st)
    assert rep.size()==2
    rep.remove("1")
    assert rep.size()==1
    #try to remove an inexistent student
    try:
        rep.remove("3")
        assert False
    except ValueError:
        assert True

testDeleteStudent()

def testListStudent():
    """
      test function for getAll
      Feature 3 - List students for a criteria
      Task 1 - retrieve all the students from the repository
    """
    rep = StudentRepository()
    st = Student("1", "Ion", Address("Adr", 1,"Cluj"))
    rep.store(st)
    st = Student("2", "Ion2", Address("Adr2", 1,"Cluj"))
    rep.store(st)

    all = rep.getAll()
    assert len(all)==2
    st1 = rep.find("1")
    assert st1.getId()=="1"
    assert st1.getName()=="Ion"
    assert st1.getAdr().getStreet()=="Adr"
    st2 = rep.find("2")
    assert st2.getId()=="2"
    assert st2.getName()=="Ion2"
    assert st2.getAdr().getStreet()=="Adr2"

testListStudent()

def testUpdate():
    """
     test function for update
     Feature 4 - update a student information
     Task 1 - update student in the repository
    """
    rep = StudentRepository()
    st = Student("1", "Ion", Address("Adr", 1,"Cluj"))
    rep.store(st)
    st = Student("1", "Ionel", Address("Addrr", 1,"Cluj"))
    rep.update("1",st)
    sts = rep.getAll()
    assert sts[0].getName()=="Ionel"
    assert sts[0].getAdr().getStreet()=="Addrr"

    #use case for a wrong id
    try:
        rep.update("2",st)
        assert False
    except ValueError:
        assert True

testUpdate()