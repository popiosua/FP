import datetime
from domain.cheltuiala import Cheltuiala
from typing import Optional

class RepositoryException(Exception):
    def __init__(self, error=""):
        """
        Create a new exception
        error - String
        """
        self.error = error
    
    def getError(self) -> str:
        """
        Retriving the error for the current exception
        self - the current exception
        Return - error String
        """
        return self.error

class MemoryRepository:
    def __init__(self, cheltuieli=None):
        """
        Create a new Memory Repository
        cheltuieli - dictionary
        """
        if cheltuieli is None:
            cheltuieli = {}
        self.__cheltuieli = cheltuieli
    
    def store(self, cheltuiala : Cheltuiala):
        """
        Store object in __cheltuieli
        cheltuiala is a cheltuiala
        raise RepositoryException if we have a student with same id
        """
        if cheltuiala.getId() in self.__cheltuieli:
            raise RepositoryException("Duplicate IDs!")
        self.__cheltuieli[cheltuiala.getId()] = cheltuiala

    def size(self) -> int:
        """
          The number of __cheltuieli in the repository
          return an integer number
        """
        return len(self.__cheltuieli)
    
    def getAllCheltuieli(self) -> list:
        """
        return a list, list of all __cheltuieli in the repository
        """
        return list(self.__cheltuieli.values())
    
    def update(self, id : str, newCheltuiala : Cheltuiala) -> bool:
        """
        Update cheltuiala with id with newCheltuiala in __cheltuieli
        id String, newCheltuiala Cheltuiala
        Return True if succeed, else False
        """
        if id in self.__cheltuieli:
            self.delete(id)
            self.__cheltuieli[newCheltuiala.getId()] = newCheltuiala
            return True
        
        return False
        
    
    def find(self, id : str) -> Optional[Cheltuiala]:
        """
        Find cheltuiala with id in __cheltuieli
        id - string
        Return - cheltuiala if therre is a cheltuiala with this id, or None
        """
        if id in self.__cheltuieli:
            return self.__cheltuieli[id]
        
        return None
    
    def delete(self, id) -> bool:
        """
        Delete cheltuiala with id from __cheltuieli
        id String
        Return True if succeed, else False
        """
        if id in self.__cheltuieli:
            del self.__cheltuieli[id]
            return True
        
        return False
    
def testStoreCheltuiala():
    """
    Test Storing in Repository (Store, Size)
    """
    cheltuiala1 = Cheltuiala('1', 1, 20.1, 'apa', datetime.date(2020, 10, 11))
    rep = MemoryRepository()

    assert rep.size()==0
    rep.store(cheltuiala1)
    assert rep.size()==1

    cheltuiala2 = Cheltuiala('2', 1, 319.12, 'gaz', datetime.date(2020, 10, 11))
    rep.store(cheltuiala2)
    assert rep.size()==2

    cheltuiala3 = Cheltuiala('2', 2, 19.13, 'gaz', datetime.date(2020, 10, 11))
    try:
        rep.store(cheltuiala3)
        assert False
    except RepositoryException:
        assert True

def testUpdateCheltuiala():
    """
    Test Updating in Repository (Update, Find)
    """
    cheltuiala1 = Cheltuiala('1', 1, 20.1, 'apa', datetime.date(2020, 10, 11))
    rep = MemoryRepository()

    assert rep.size()==0
    rep.store(cheltuiala1)
    assert rep.size()==1

    assert rep.find('1') == cheltuiala1

    cheltuiala2 = Cheltuiala('2', 1, 319.12, 'gaz', datetime.date(2020, 10, 11))
    rep.update('1', cheltuiala2)

    assert rep.find('1') == None
    assert rep.find('2') == cheltuiala2

    cheltuiala3 = Cheltuiala('3', 1, 319.12, 'gaz', datetime.date(2020, 10, 11))
    rep.store(cheltuiala3)
    assert rep.size()==2

def testDeleteCheltuiala():
    """
    Test Delete in Repository (Delete, Get All)
    """
    cheltuiala1 = Cheltuiala('1', 1, 20.1, 'apa', datetime.date(2020, 10, 11))
    rep = MemoryRepository()

    assert rep.size()==0
    rep.store(cheltuiala1)
    assert rep.size()==1

    assert rep.getAllCheltuieli() == [cheltuiala1]
    assert rep.delete('1') == True

    assert rep.getAllCheltuieli() == []
    assert rep.delete('1') == False

    rep.store(cheltuiala1)
    assert rep.size()==1

def test(): 
    testStoreCheltuiala()
    testUpdateCheltuiala()
    testDeleteCheltuiala()

test()