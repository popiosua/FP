from repository.inmemory import StudentRepository
from domain.entities import Student
from domain.entities import Address



class StudentFileRepository(StudentRepository):
    """
      Store/retrieve students from file
    """
    def __init__(self, fileN):
        """
          initialise repository
          fileName - string, file path where the students are stored
          post: students are loaded from the file
        """
        #properly initialise the base class
        StudentRepository.__init__(self)
        self.__fName = fileN
        #load student from the file
        self.__loadFromFile()

    def __loadFromFile(self):
        """
          Load students from file
          raise CorruptedFileException if there is an error when reading from the file
        """
        try:
            f = open(self.__fName, "r")
        except IOError:
            #file not exist
            return
        line = f.readline().strip()
        while line!="":
            attrs = line.split(";")
            st = Student(attrs[0], attrs[1], Address(attrs[2], attrs[3], attrs[4]))
            StudentRepository.store(self, st)
            line = f.readline().strip()
        f.close()

    def store(self, st):
        """
          Store the student to the file.Overwrite store
          st - student
          Post: student is stored to the file
          raise DuplicatedIdException for duplicated id
        """
        StudentRepository.store(self, st)
        self.__storeToFile()

    def update(self, id, st):
        """
          Update student in the repository
          id - string, the id of the student to be updated
          st - Student, the updated student
          raise ValueError if there is no student with the given id
        """
        StudentRepository.update(self, id, st)
        self.__storeToFile()


    def remove(self, id):
        """
          remove a student from the repository
          id - string, the id of the student to be removed
          return student
          post: the repository not contains student with the given id
          raise ValueError if there is no student with the given id
        """
        st = StudentRepository.remove(self, id)
        self.__storeToFile()
        return st


    def __storeToFile(self):
        """
         Store all the students  in to the file
         raise CorruptedFileException if we can not store to the file
        """
        #open file (rewrite file)
        f = open(self.__fName, "w")
        sts = StudentRepository.getAll(self)
        for st in sts:
            strf = st.getId()+";"+st.getName()+";"
            strf = strf + st.getAdr().getStreet()+";"+str(st.getAdr().getNr())+";"+st.getAdr().getCity()
            strf = strf+"\n"
            f.write(strf)
        f.close()

    def removeAll(self):
        """
          Remove all the students from the repository
          post: the repository is empty
        """
        StudentRepository.removeAll(self)
        self.__storeToFile()

def testStore():
    fileName = "teststudent.txt"
    repo = StudentFileRepository(fileName)
    repo.removeAll()

    st = Student("1", "Ion", Address("str", 3, "Cluj"))
    repo.store(st)
    assert repo.size()==1
    assert repo.find("1") == st
    #verify if the student is stored in the file
    repo2 = StudentFileRepository(fileName)
    assert repo2.size()==1
    assert repo2.find("1") == st

testStore()