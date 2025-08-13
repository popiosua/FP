import datetime
from domain.cheltuiala import Cheltuiala

class ValidatorException(Exception):
    
    def __init__(self, errors = None):
        """
        Create a new validator with the given errors
        errors - list
        """
        if errors == None:
            errors = []
        self.errors = errors
    
    def getErrors(self) -> list:
        """
        Retriving the errors for the current validator
        self - the current validator
        Return - errors list
        """
        return self.errors
    

class CheltuialaValidator:
    def validate(self, object : Cheltuiala):
        """
        throw ValidatorException if 
        - filds are empty
        - apartement is an integer <= 0
        - tip i not one of {"apa", "canal", "incalzire", "gaz", "altele"}
        - suma < 0.0
        - date don't have exact 10 characters yyyy.mm.dd
        """

        errors = []
        if (object.getId() == ""): errors.append("Id can not be empty!") 
        if (object.getApartament() <= 0): errors.append("Apartamentul trebuie sa fie numar pozitiv >0!") 
        if (object.getTip() not in ["apa", "canal", "incalzire", "gaz", "altele"]): errors.append("Tipul trebuie sa fie : 'apa, canal, încălzire, gaz, altele'!") 
        if (object.getSuma() < 0.0): errors.append("Suma nu poate fi negativa!") 
        if (len(str(object.getDate())) != 10): errors.append("Data trebuie sa fie in formatul yyyy-mm-dd!") 

        if len(errors) > 0:
            raise ValidatorException(errors)
    
def testCheltuialaValidator():
    """
    Testing the validator
    """
    validator = CheltuialaValidator()

    object = Cheltuiala("", -1, -1, "APA", "11111111")
    try:
        validator.validate(object)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==5
    
    object = Cheltuiala("", -1, -1, "APA", datetime.date(2020, 10, 11))
    try:
        validator.validate(object)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==4

    object = Cheltuiala("", -1, -1.0, "apa", datetime.date(2020, 10, 11))
    try:
        validator.validate(object)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==3

    object = Cheltuiala("", -1, 1.21, "apa", datetime.date(2020, 10, 11))
    try:
        validator.validate(object)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==2

    object = Cheltuiala("", 1, 1.21, "apa", datetime.date(2020, 10, 11))
    try:
        validator.validate(object)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==1

    object = Cheltuiala("0", 1, 20.1, "apa", datetime.date(2020, 10, 11))
    try:
        validator.validate(object)
        assert True
    except ValidatorException as ex:
        assert False
        

def test():
    testCheltuialaValidator()

test()