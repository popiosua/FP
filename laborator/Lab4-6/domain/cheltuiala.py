import datetime

class Cheltuiala:
    # tip = {apa, canal, încălzire, gaz, altele}

    def __init__(self, id : str, apartament : int, suma : float, tip : str, data : datetime):
        """
        Create a new cheltuiala with the given id, apartament, suma and tip
        id, tip are Strings, apartament is integer, suma is double
        """
        self.__id = id
        self.__apartament = apartament
        self.__suma = suma
        self.__tip = tip
        self.__date = data


    def getId(self) -> str: 
        """
        Retriving the id for the current cheltuiala
        self - the current cheltuiala
        Return - id string
        """
        return self.__id
    
    def getApartament(self) -> int:
        """
        Retriving the apartament for the current cheltuiala
        self - the current cheltuiala
        Return - apartament integer
        """
        return self.__apartament
    
    def getSuma(self) -> float:
        """
        Retriving the suma for the current cheltuiala
        self - the current cheltuiala
        Return - suma double
        """
        return self.__suma
    
    def getTip(self) -> str:
        """
        Retriving the tip for the current cheltuiala
        self - the current cheltuiala
        Return - tip string
        """
        return self.__tip
    
    def getDate(self) -> datetime:
        """
        Retriving the date for the current cheltuiala
        self - the current cheltuiala
        Return - date datetime
        """
        return self.__date
    
    def __eq__(self, cheltuiala) -> bool:
        """
        Verify equality
        cheltuiala - Cheltuiala
        return True if the curent cheltuiala equals with other (have the same id)
        """
        return (self.getId()==cheltuiala.getId() and
                self.getApartament()==cheltuiala.getApartament() and
                self.getSuma()==cheltuiala.getSuma() and
                self.getTip()==cheltuiala.getTip() and
                self.getDate()==cheltuiala.getDate())

    def __repr__(self) -> str:
        return (f'{self.getId()} Ap.: {self.getApartament()}, tip: {self.getTip()}, suma: {self.getSuma()} on {self.__date}')


def testCreateCheltuiala():
    """
    Testing cheltuiala creation
    """

    bill = Cheltuiala("1", 1, 1.11, "apa", datetime.date(2020, 5, 17))
    assert bill.getId() == "1"
    assert bill.getApartament() == 1
    assert bill.getSuma() == 1.11
    assert bill.getTip() == "apa"
    assert bill.getDate() == datetime.date(2020, 5, 17)

def testEqualCheltuiala():
    """
    Testing = operator on cheltuiala
    """
    bill = Cheltuiala("1", 1, 1.11, "apa", datetime.date(2020, 5, 17))
    cheltuiala = Cheltuiala("1", 1, 1.11, "apa", datetime.date(2020, 5, 17))

    assert cheltuiala == bill

def test():
    testCreateCheltuiala()
    testEqualCheltuiala()

test()