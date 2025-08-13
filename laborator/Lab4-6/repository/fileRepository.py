import datetime
from repository.memoryRepository import MemoryRepository
from domain.cheltuiala import Cheltuiala
from utils.fileutile import clearFileContent

class FileRepository(MemoryRepository):
    """
    Responsible with the CRUD from/into a text file
    Include different version of:
        reading from the file
        accessing base class attributes (fields/methods)
    """

    def __init__(self, fileName : str):
        """
        Create a new File Repository
        cheltuieli - dictionary
        """
        MemoryRepository.__init__(self, cheltuieli={})
        self.__fileName = fileName
        self.__loadFromFile()

    def __createCheltuialaFromLine(self, line : str) -> Cheltuiala:
        """
        Process the line that have the attributes separated by " "
        return Cheltuiala
        """

        fields = line.strip().split(" ")
        dateString = fields[4].split('-')
        data = datetime.date(int(dateString[0]), int(dateString[1]), int(dateString[2]))

        cheltuiala = Cheltuiala(fields[0], int(fields[1]), float(fields[2]), fields[3], data)
        return cheltuiala
    
    def __loadFromFile(self):
        """
        Load __cheltuieli from file
        process file line by line
        """

        file = open(self.__fileName)
        for line in file:
            if(line.strip() == ""):
                continue #empty line
            cheltuiala = self.__createCheltuialaFromLine(line)
            MemoryRepository.store(self, cheltuiala)
        
        file.close()
    
    def __writeToFile(self):
        """
        Write __cheltuieli to file
        write in file line by line
        """
        items = list[Cheltuiala](self.getAllCheltuieli())
        file = open(self.__fileName, "w")
        for elem in items:
            line = elem.getId() + " " + str(elem.getApartament()) + " " + str(elem.getSuma()) + " " + elem.getTip() + " " + str(elem.getDate()) + "\n"
            file.write(line)

        file.close()

    def store(self, cheltuiala):
        """
        Store a cheltuiala both to file and in memory
        """
        MemoryRepository.store(self, cheltuiala)
        self.__appendToFile(cheltuiala)

    def __appendToFile(self, cheltuiala : Cheltuiala):
        """
        Converting the cheltuiala to string than adding that string as a line in the file
        """

        file = open(self.__fileName, "a")
        line = cheltuiala.getId() + " " + str(cheltuiala.getApartament()) + " " + str(cheltuiala.getSuma()) + " " + cheltuiala.getTip() + " " + str(cheltuiala.getDate()) + "\n"

        file.write(line)
        file.close()

    def update(self, id, newCheltuiala) -> bool:
        """
        Update a cheltuiala with id whith new vaalues both to file and in memory
        Return True if succeed else False
        """
        ok = MemoryRepository.update(self, id, newCheltuiala)
        if ok:
            self.__writeToFile()

        return ok

    def delete(self, id) -> bool:
        """
        Delete a cheltuiala with id
        Return True if it succeed else False
        """
        ok = MemoryRepository.delete(self, id)
        if ok:
            self.__writeToFile()

        return ok
    
def testFileRepositoryStore():
    """
    Testing the File Repository Store
    """

    fileName = "test.txt"

    clearFileContent(fileName)
    repo = FileRepository(fileName)
    assert repo.size() == 0
    repo.store(Cheltuiala("1", 1, 10.11, "apa", datetime.date(2020, 5, 17)))
    assert repo.size() == 1

def testFileRepositoryRead():
    """
    Testing the File Repository Read
    """
    fileName = "test.txt"

    clearFileContent(fileName)
    repo = FileRepository(fileName)
    repo.store(Cheltuiala("1", 1, 10.11, "apa", datetime.date(2020, 5, 17)))
    repo.store(Cheltuiala("2", 1, 51.22, "gaz", datetime.date(2020, 5, 17)))
    
    repository = FileRepository(fileName)
    assert repository.size() == 2

def testFileRepositoryUpdate():
    """
    Testing the File Repository Update
    """

    fileName = "test.txt"

    clearFileContent(fileName)
    repo = FileRepository(fileName)
    assert repo.size() == 0
    repo.store(Cheltuiala("1", 1, 10.11, "apa", datetime.date(2020, 5, 17)))
    assert repo.size() == 1

    assert repo.update('1', Cheltuiala("2", 2, 10.11, "apa", datetime.date(2020, 5, 17)))
    assert repo.size() == 1

    assert repo.find('1') == None
    assert repo.find('2') == Cheltuiala("2", 2, 10.11, "apa", datetime.date(2020, 5, 17))


def testFileRepositoryDelete():
    """
    Testing the File Repository Delete
    """

    fileName = "test.txt"

    clearFileContent(fileName)
    repo = FileRepository(fileName)
    assert repo.size() == 0
    assert repo.delete('1') == False

    repo.store(Cheltuiala("1", 1, 10.11, "apa", datetime.date(2020, 5, 17)))
    assert repo.size() == 1

    assert repo.delete('1') == True
    assert repo.size() == 0

def test():
    testFileRepositoryRead()
    testFileRepositoryStore()
    testFileRepositoryUpdate()
    testFileRepositoryDelete()

test()