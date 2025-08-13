from repository.inmemory import DuplicatedIDException
from domain.validators import ValidationException
from domain.validators import StudentCRUDException
class ConsoleUI:
    """
      Class responsible with the user interface
      Will use the controller to perform operations other than read, print
    """
    def __init__(self,ctr):
        """
          Initialise UI
          ctr StudentControler
        """
        self.__ctr = ctr

    def __readUserCommand(self):
        """
          Read the command from the user
          return string, the command
        """
        print ("""
        0 - exit
        1 - add student
        2 - remove student
        3 - search student
        4 - update student
        """)
        return input("Give command:").strip()

    def __createdStudent(self):
        """
          Read a student and store in the apllication
        """
        id = input("Student id:").strip()
        name = input("Student name:").strip()
        street = input("Address - street:").strip()
        nr = input("Address - number:").strip()
        city = input("Address - city:").strip()
        try:
            self.__ctr.create(id, name,street,nr,city)
        except ValidationException as ex:
            print ("special treatment")
            print (ex)
        except StudentCRUDException as ex:
            print (ex)


    def __removeStudent(self):
        """
          Read a student id and remove the student

        """
        id = input("Student id:").strip()
        try:
            st = self.__ctr.remove(id)
            print ("Student "+st.getName()+" removed")
        except ValueError as msg:
            print (msg)

    def __searchStudent(self):
        """
          Search for students with name containing a given string
        """
        cr = input("Name contains:").strip()
        sts = self.__ctr.search(cr)
        if sts ==[]:
            print ("No match")
            return
        print ("")
        print ("Search results :"+str(len(sts))+" students")
        print ("____________________________")
        print ("ID".ljust(4)+"Name".ljust(10)+"Address")
        for st in sts:
            print (st.getId().ljust(4)+st.getName().ljust(10)+str(st.getAdr()))
        print ("____________________________")

    def __updateStudent(self):
        id = input("Give the id of the student:").strip()
        name = input("Student name:").strip()
        street = input("Address - street:").strip()
        nr = input("Address - number:").strip()
        city = input("Address - city:").strip()
        try:
            old = self.__ctr.update(id, name, street,nr,city)
            print ("Student "+old.getName()+ " updated")
        except ValueError as msg:
            print (msg)

    def startUI(self):
        """
          Start the ui
        """
        while True:
            c = self.__readUserCommand()
            if c=="0":
                print ("By By")
                return
            if c =="1":
                self.__createdStudent()
            if c =="2":
                self.__removeStudent()
            if c =="3":
                self.__searchStudent()
            if c =="4":
                self.__updateStudent()
