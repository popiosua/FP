from datetime import date
from typing import Optional
from domain.cheltuiala import Cheltuiala
from domain.validators import CheltuialaValidator
from repository.fileRepository import FileRepository
from itertools import count

from repository.memoryRepository import RepositoryException
from utils.fileutile import clearFileContent

class CheltuialaService:
    def __init__(self, repo : FileRepository, val : CheltuialaValidator):
        """
        Initialise service
        repo - repository - object to store cheltuieli
        val - validator - object to validate cheltuieli
        """

        self.__repo = repo
        self.__val = val
        self.__undoList = []
    
    #ADAUGARE

    def createCheltuiala(self, id : str, apartament : int, suma : float, tip : str, data : date) -> Cheltuiala:
        """
        Create a cheluiala and store it to repository
        id, tip are String, apartament is int, suma is float, data is date
        Return Cheltuiala
        """
        cheltuiala = Cheltuiala(id, apartament, suma, tip, data)
        self.__val.validate(cheltuiala)

        self.__repo.store(cheltuiala)
        
        self.__undoList.append(('a', id))

        return cheltuiala
    
    def updateCheltuiala(self, id : str, newID : str, newApartament : int, newSuma : float, newTip : str, newData : date) -> Cheltuiala:
        """
        Update a cheluiala with id with the new values into repository
        id, newID, newTip are String, newApartament is int, newSuma is float, newData is date
        Return Cheltuiala
        """
        oldCheltuiala = self.__repo.find(id)
        if(oldCheltuiala is not None):
            self.__undoList.append(('u', newID, oldCheltuiala))

        cheltuiala = Cheltuiala(newID, newApartament, newSuma, newTip, newData)
        self.__val.validate(cheltuiala)
        self.__repo.update(id, cheltuiala)

        return cheltuiala
    
    # STERGERE
    def deleteCheltuiala(self, id : str) -> bool:
        """
        Delete a cheluiala with id from repository
        id is String
        Return Cheltuiala
        """
        oldCheltuiala = self.__repo.find(id)
        if(oldCheltuiala != None):
            self.__undoList.append(('d', oldCheltuiala.getId(), oldCheltuiala.getApartament(), oldCheltuiala.getSuma(), oldCheltuiala.getTip(), oldCheltuiala.getDate()))

        ok = self.__repo.delete(id)

        return ok

    def deleteCheltuieliApartament(self, apartament : int, ok=True) -> list[Cheltuiala]:
        """
        Delete all cheluieli on an apartment from repository
        apartament is int
        Return list[Cheltuiala] that were removed
        """
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())
        eliminate = list[Cheltuiala]([])

        for elem in cheltuieli:
            if(elem.getApartament() == apartament):
                eliminate.append(elem)
                self.__repo.delete(elem.getId())

        if(ok == True):
            self.__undoList.append(('da', eliminate))

        return eliminate
    
    def deleteCheltuieliApartamentConsecutiv(self, start : int, stop : int) -> list[Cheltuiala]:
        """
        Delete all cheluieli on consecutive apartments from repository
        start, stop is int
        Return list[Cheltuiala] that were removed
        """
        eliminate = list[Cheltuiala]([])
        for i in range(start, stop+1):
            erased = self.deleteCheltuieliApartament(i, False)
            for elem in erased:
                eliminate.append(elem)

        self.__undoList.append(('dc', eliminate))

        return eliminate
    
    def deleteTipCheltuieliApartament(self, tip : str) -> list[Cheltuiala]:
        """
        Delete all chelutuieli with tip from all apartments from repository
        tip is str
        Return list[Cheltuiala] that were removed
        """
        eliminate = list[Cheltuiala]([])
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())
        for elem in cheltuieli:
            if(elem.getTip() == tip):
                eliminate.append(elem)
                self.__repo.delete(elem.getId())
        
        self.__undoList.append(('dt', eliminate))
        
        return eliminate

    # CAUTARE
    def findCheltuiala(self, id) -> Optional[Cheltuiala]:
        """
        Find cheltuiala id form repository
        id is str
        Return cheltuiala
        """
        return self.__repo.find(id)

    def findApartamentCheltuieliSumaMare(self, suma : float) -> list:
        """
        Find all apartaments with SUM of cheltuieli bigger than suma from repository
        suma is float
        Return list[Cheltuiala] that were found
        """
        apartamente = []
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())

        totalCheltuieli = {}
        for elem in cheltuieli:
            if(elem.getApartament() not in totalCheltuieli.keys()):
                totalCheltuieli[elem.getApartament()] = elem.getSuma()
            else:
                totalCheltuieli[elem.getApartament()] = totalCheltuieli[elem.getApartament()] + elem.getSuma()
        
        for key in totalCheltuieli.keys():
            if(totalCheltuieli[key] > suma):
                apartamente.append(key)
        
        return apartamente

    def findCheltuieliTip(self, tip : str) -> list[Cheltuiala]:
        """
        Find all apartaments with tip from repository
        tip is str
        Return list[Cheltuiala] that were found
        """
        rezultat = list[Cheltuiala]([])
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())

        for elem in cheltuieli:
            if(elem.getTip() == tip):
                rezultat.append(elem)

        return rezultat
    
    def findApartamentCheltuieliZiSumaMare(self, zi : int, suma : float) -> list[Cheltuiala]:
        """
        Find all cheltuieli on day that have suma bigger then suma from repository
        day is int, suma is float
        Return list[Cheltuiala] that were found
        """
        rezultate = list[Cheltuiala]([])
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())

        for elem in cheltuieli:
            day = str(elem.getDate()).split('-')[2]
            day = int(day)
            if(day == zi):
                if(elem.getSuma() > suma):
                    rezultate.append(elem)
        
        return rezultate
    
    #Rapoarte
    def sumTotalTip(self, tip : str) -> float:
        """
        Sum all cheltuieli on a tip from repository
        tip is str
        Return float sum of a tip
        """
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())
        suma = 0.0

        for elem in cheltuieli:
            if(elem.getTip() == tip):
                suma = suma + elem.getSuma()
        
        return suma

    def sortApartamentTip(self, tip : str, order="ASC") -> list[Cheltuiala]:
        """
        Sort ASC all apartaments after a tip from repository
        tip is str
        Return list[Cheltuiala] that were found
        """
        ok = False
        
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())

        totalCheltuieli = {}
        for elem in cheltuieli:
            if(elem.getApartament() not in totalCheltuieli.keys()):
                totalCheltuieli[elem.getApartament()] = {"apa" : 0.0, "canal" : 0.0, "incalzire" : 0.0, "gaz" : 0.0, "altele" : 0.0}
            totalCheltuieli[elem.getApartament()][elem.getTip()] = totalCheltuieli[elem.getApartament()][elem.getTip()] + elem.getSuma()
        
        if(order == 'DESC'):
            ok = True
             
        sortedCheltuieli = sorted(totalCheltuieli, key=lambda i:totalCheltuieli[i][tip], reverse=ok)

        # apartamente = []
        # for elem in sortedCheltuieli:
        #     apartamente.append(elem[0])

        return sortedCheltuieli

    def totalSumApartament(self, apartament : int) -> float:
        """
        Calculate sum of all cheltuieli of an aapartament from repository
        apartament is int
        Return sum float
        """
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())
        suma = 0.0

        for elem in cheltuieli:
            if(elem.getApartament() == apartament):
                suma = suma + elem.getSuma()
        
        return suma

    # Filtru
    def removeCheltuieliTip(self, tip : str) -> list[Cheltuiala]:
        """
        Filter all the cheltuieli showing all the cheltuieli that are not of tip from repository
        tip is str
        Return list[Cheltuiala] that are not of tip
        """
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())
        rezultat = list[Cheltuiala]([])

        for elem in cheltuieli:
            if(elem.getTip() != tip):
                rezultat.append(elem)
        
        return rezultat

    def removeCheltuieliSumaMica(self, suma : float) -> list[Cheltuiala]:
        """
        Filter all the cheltuieli showing all the cheltuieli that do not have suma less than suma
        sum is float
        Return list[Cheltuiala] that have sum greater than suma
        """
        cheltuieli = list[Cheltuiala](self.__repo.getAllCheltuieli())
        rezultat = list[Cheltuiala]([])

        for elem in cheltuieli:
            if(elem.getSuma() >= suma):
                rezultat.append(elem)
        
        return rezultat
    
    def getAllCheltuieli(self) -> list:
        """
        Return all cheltuieli from repository list
        """
        return self.__repo.getAllCheltuieli()
    
    # Undo
    def undo(self):
        """
        Undo the last operation
        """
        if(len(self.__undoList) > 0):
            undoOption = self.__undoList.pop()

            option = undoOption[0]

            match option:
                case 'a': # added a cheltuiala
                    self.__repo.delete(undoOption[1])
                    return "Undo add"
                case 'u': # updated a cheltuiala
                    cheltuiala = undoOption[2]
                    self.__repo.update(undoOption[1], cheltuiala)
                    return "Undo update"
                case 'd': # deleted a cheltuiala
                    cheltuiala = Cheltuiala(undoOption[1], undoOption[2], undoOption[3], undoOption[4], undoOption[5])
                    self.__repo.store(cheltuiala)
                    return "Undo delete"
                case 'da': # deleted all cheltuiala for an apartament
                    for elem in undoOption[1]:
                        self.__repo.store(elem)
                    return "Undo delete all cehltuieli for an apartament"
                case 'dc': # deleted all cheltuiala for a consecutive apartamente
                    for elem in undoOption[1]:
                        self.__repo.store(elem)
                    return "Undo delete all cehltuieli for an consecutive apartaments"
                case 'dt': # deleted all cheltuiala with tip from all apartamente
                    for elem in undoOption[1]:
                        self.__repo.store(elem)
                    return "Undo delete all cehltuieli with tip"
                case default:
                    return "No more undo!"
    
    def undoTimes(self) -> int:
        """
        Return the length of the undo list
        """
        return len(self.__undoList)
    

def dummy(repo : FileRepository):
    """
    Pre populate repository with some dummy objects
    repo - FileRepository the rrepository that we are populating
    """
        
    dummyList = [
        Cheltuiala('1', 1, 11.12, 'apa', date(2022, 5, 11)),
        Cheltuiala('2', 1, 20.50, 'canal', date(2022, 5, 12)),
        Cheltuiala('3', 1, 35.75, 'incalzire', date(2022, 6, 1)),
        Cheltuiala('4', 1, 45.00, 'gaz', date(2022, 6, 3)),
        Cheltuiala('5', 1, 18.90, 'altele', date(2022, 6, 5)),

        Cheltuiala('6', 2, 25.00, 'apa', date(2022, 7, 10)),
        Cheltuiala('7', 2, 15.20, 'canal', date(2022, 7, 15)),
        Cheltuiala('8', 3, 55.30, 'incalzire', date(2022, 8, 1)),
        Cheltuiala('9', 3, 65.00, 'gaz', date(2022, 8, 2)),
        Cheltuiala('10', 4, 40.00, 'altele', date(2022, 8, 3)),
        ]


    for elem in dummyList:
        repo.store(elem)
        

def testAdaugareService():
    """
    Test ADAUGARE in service
    adaugare cheltuiala
    modificare cheltuiala
    """
    fileName = "test.txt"
    clearFileContent(fileName)

    repo = FileRepository(fileName)
    dummy(repo)
    assert len(repo.getAllCheltuieli()) == 10

    validator: CheltuialaValidator =  CheltuialaValidator()

    service : CheltuialaService = CheltuialaService(repo, validator)
    assert len(service.getAllCheltuieli()) == 10

    try:
        service.createCheltuiala('1', 1, 11.12, 'apa', date(2022, 5, 11))
        assert False
    except RepositoryException as ex:
        assert True

    assert len(service.getAllCheltuieli()) == 10

    service.createCheltuiala('11', 2, 1130.12, 'incalzire', date(2022, 7, 16))
    assert len(service.getAllCheltuieli()) == 11

    service.updateCheltuiala('11', '12', 2, 130.12, 'altele', date(2022, 7, 16))
    assert len(service.getAllCheltuieli()) == 11
    assert service.findCheltuiala('11') == None
    assert service.findCheltuiala('12') == Cheltuiala('12', 2, 130.12, 'altele', date(2022, 7, 16))
    

def testStergereService():
    """
    Test DELETING in service
    stergere toate cheltuielile unui apartament
    stergere cheltuieli de la apartamente consecutive (ex 1->5)
    stergere cheltuieli de un anume tip de la toate apartamentele
    """
    fileName = "test.txt"
    clearFileContent(fileName)

    repo = FileRepository(fileName)
    dummy(repo)
    assert len(repo.getAllCheltuieli()) == 10

    validator: CheltuialaValidator =  CheltuialaValidator()

    service : CheltuialaService = CheltuialaService(repo, validator)
    assert len(service.getAllCheltuieli()) == 10

    service.deleteCheltuieliApartament(1)
    assert len(service.getAllCheltuieli()) == 5
    assert service.findCheltuiala('1') == None
    assert service.findCheltuiala('2') == None
    assert service.findCheltuiala('3') == None
    assert service.findCheltuiala('4') == None
    assert service.findCheltuiala('5') == None

    service.deleteCheltuieliApartament(0)
    assert len(service.getAllCheltuieli()) == 5
    
    service.deleteTipCheltuieliApartament('apa')
    assert len(service.getAllCheltuieli()) == 4
    assert service.findCheltuiala('6') == None

    service.deleteTipCheltuieliApartament('apa')
    assert len(service.getAllCheltuieli()) == 4

    service.deleteCheltuieliApartamentConsecutiv(2,2)
    assert len(service.getAllCheltuieli()) == 3
    assert service.findCheltuiala('7') == None

    service.deleteCheltuieliApartamentConsecutiv(3,4)
    assert len(service.getAllCheltuieli()) == 0
    assert service.findCheltuiala('8') == None
    assert service.findCheltuiala('9') == None
    assert service.findCheltuiala('10') == None

    service.deleteCheltuieliApartamentConsecutiv(1,4)
    assert len(service.getAllCheltuieli()) == 0


def testCautareService():
    """
    Testing FINDING in service
    tiparire apartamente cu cheltuieli mai mare decat o suma
    tiparire cheltuieli de un anumit tip de la toate apartamentele
    tiparire cheltuieli de pe o zi mai mare de o anumita suma (ex: suma, zi)
    """
    fileName = "test.txt"
    clearFileContent(fileName)

    repo = FileRepository(fileName)
    dummy(repo)
    validator =  CheltuialaValidator()

    service = CheltuialaService(repo, validator)

    assert service.findApartamentCheltuieliSumaMare(120.00) == [1, 3]
    assert service.findApartamentCheltuieliSumaMare(131.00) == [1]

    assert service.findCheltuieliTip('apa') == [ Cheltuiala('1', 1, 11.12, 'apa', date(2022, 5, 11)), Cheltuiala('6', 2, 25.00, 'apa', date(2022, 7, 10)) ]
    assert service.findCheltuieliTip('apaa') == []

    assert service.findApartamentCheltuieliZiSumaMare(1, 35.00) == [ Cheltuiala('3', 1, 35.75, 'incalzire', date(2022, 6, 1)), Cheltuiala('8', 3, 55.30, 'incalzire', date(2022, 8, 1)) ]
    assert service.findApartamentCheltuieliZiSumaMare(1, 55.00) == [ Cheltuiala('8', 3, 55.30, 'incalzire', date(2022, 8, 1)) ]
    assert service.findApartamentCheltuieliZiSumaMare(1, 55.30) == []


def testRapoarteService():
    """
    Testing RAPORT in service
    suma totala pentru un anumit tip de cheltuiala
    toate apartamentele sortate dupa un anumit tip de cheltuiala
    total cheltuieli pentru un apartament
    """
    fileName = "test.txt"
    clearFileContent(fileName)

    repo = FileRepository(fileName)
    dummy(repo)
    validator =  CheltuialaValidator()

    service = CheltuialaService(repo, validator)
    assert len(service.getAllCheltuieli()) == 10

    assert service.sumTotalTip('apa') == 36.12
    assert service.sumTotalTip('altele') == 58.90

    
    assert service.sortApartamentTip('apa') == [3, 4, 1, 2]
    assert service.sortApartamentTip('gaz', "DESC") == [3, 1, 2, 4]

    assert service.totalSumApartament(1) == 131.27
    assert service.totalSumApartament(5) == 0.00

def testFiltruService():
    """
    Testing FILTERING in service
    elimina toate cheltuielile de un anumit tip
    elimina toate cheltuielile mai mici decat o suma data
    """
    fileName = "test.txt"
    clearFileContent(fileName)

    repo = FileRepository(fileName)
    dummy(repo)
    validator =  CheltuialaValidator()

    service = CheltuialaService(repo, validator)
    assert len(service.getAllCheltuieli()) == 10

    filtruApa = service.removeCheltuieliTip('apa') #id : 1,6
    assert len(filtruApa) == 8
    assert len(service.getAllCheltuieli()) == 10

    filtruGaz = service.removeCheltuieliTip('gaz') #id : 4,9
    assert len(filtruGaz) == 8
    assert len(service.getAllCheltuieli()) == 10

    filtruSuma = service.removeCheltuieliSumaMica(20.00)
    assert len(filtruSuma) == 7
    assert len(service.getAllCheltuieli()) == 10

    filtruSuma = service.removeCheltuieliSumaMica(10.00)
    assert len(filtruSuma) == 10
    assert len(service.getAllCheltuieli()) == 10
    

def testUndoService():
    """
    Testing UNDO in service
    Undo is done on modifiing actions add update delete
    """
    fileName = "test.txt"
    clearFileContent(fileName)

    repo = FileRepository(fileName)
    dummy(repo)
    validator =  CheltuialaValidator()

    service = CheltuialaService(repo, validator)
    assert len(service.getAllCheltuieli()) == 10

    assert service.undoTimes() == 0
    service.createCheltuiala('11', 2, 1130.12, 'incalzire', date(2022, 7, 16))
    assert len(service.getAllCheltuieli()) == 11

    assert service.undoTimes() == 1
    service.updateCheltuiala('11', '12', 2, 130.12, 'altele', date(2022, 7, 16))
    assert len(service.getAllCheltuieli()) == 11

    assert service.undoTimes() == 2
    assert service.findCheltuiala('11') == None
    assert service.findCheltuiala('12') == Cheltuiala('12', 2, 130.12, 'altele', date(2022, 7, 16))
    service.undo()

    assert service.undoTimes() == 1
    assert len(service.getAllCheltuieli()) == 11
    assert service.findCheltuiala('11') == Cheltuiala('11', 2, 1130.12, 'incalzire', date(2022, 7, 16))
    assert service.findCheltuiala('12') == None

    service.undo()
    assert len(service.getAllCheltuieli()) == 10
    assert service.findCheltuiala('11') == None
    assert service.undoTimes() == 0

    service.deleteCheltuieliApartament(1)
    assert len(service.getAllCheltuieli()) == 5
    assert service.findCheltuiala('1') == None
    assert service.findCheltuiala('2') == None
    assert service.findCheltuiala('3') == None
    assert service.findCheltuiala('4') == None
    assert service.findCheltuiala('5') == None
    assert service.undoTimes() == 1

    service.undo()
    assert len(service.getAllCheltuieli()) == 10
    assert service.findCheltuiala('1') is not None
    assert service.findCheltuiala('2') is not None
    assert service.findCheltuiala('3') is not None
    assert service.findCheltuiala('4') is not None
    assert service.findCheltuiala('5') is not None
    assert service.undoTimes() == 0

    service.deleteCheltuieliApartament(0)
    assert len(service.getAllCheltuieli()) == 10
    assert service.undoTimes() == 1

    service.undo()
    assert len(service.getAllCheltuieli()) == 10
    assert service.undoTimes() == 0

    service.deleteTipCheltuieliApartament('apa')
    assert len(service.getAllCheltuieli()) == 8
    assert service.findCheltuiala('1') == None
    assert service.findCheltuiala('6') == None
    assert service.undoTimes() == 1

    service.undo()
    assert len(service.getAllCheltuieli()) == 10
    assert service.findCheltuiala('1') is not None
    assert service.findCheltuiala('6') is not None
    assert service.undoTimes() == 0

    service.deleteCheltuieliApartamentConsecutiv(2,2)
    assert len(service.getAllCheltuieli()) == 8
    assert service.findCheltuiala('6') == None
    assert service.findCheltuiala('7') == None
    assert service.undoTimes() == 1

    service.undo()
    assert len(service.getAllCheltuieli()) == 10
    assert service.findCheltuiala('6') is not None
    assert service.findCheltuiala('7') is not None
    assert service.undoTimes() == 0

    service.deleteCheltuieliApartamentConsecutiv(3,4)
    assert len(service.getAllCheltuieli()) == 7
    assert service.findCheltuiala('8') == None
    assert service.findCheltuiala('9') == None
    assert service.findCheltuiala('10') == None
    assert service.undoTimes() == 1

    service.undo()
    assert len(service.getAllCheltuieli()) == 10
    assert service.findCheltuiala('8') is not None
    assert service.findCheltuiala('9') is not None
    assert service.findCheltuiala('10') is not None
    assert service.undoTimes() == 0

    service.deleteCheltuieliApartamentConsecutiv(1,4)
    assert len(service.getAllCheltuieli()) == 0
    assert service.undoTimes() == 1

    service.undo()
    assert len(service.getAllCheltuieli()) == 10
    assert service.undoTimes() == 0

    service.undo()


def test():
    testAdaugareService()
    testStergereService()
    testCautareService()
    testRapoarteService()
    testFiltruService()
    testUndoService()

test()