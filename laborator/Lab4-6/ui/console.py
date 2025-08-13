import datetime
from services.cheltuialaService import CheltuialaService
from domain.cheltuiala import Cheltuiala
from domain.validators import CheltuialaValidator
from repository.fileRepository import FileRepository
from repository.memoryRepository import RepositoryException

class Console:
    def __init__(self, serv : CheltuialaService):
        self.__srv = serv

    def showMenu(self):
        """
        Print the options MENU
        """
        print(
        'ADAUGARE\n'
        '1 adaugare cheltuiala\n'
        '2 modificare cheltuiala\n\n'

        'STERGERE\n'
        '3 stergere toate cheltuielile unui apartament\n'
        '4 stergere cheltuieli de la apartamente consecutive (ex 1->5)\n'
        '5 stergere cheltuieli de un anume tip de la toate apartamentele\n\n'

        'CAUTARE\n'
        '6 tiparire apartamente cu cheltuieli mai mare decat o suma\n'
        '7 tiparire cheltuieli de un anumit tip de la toate apartamentele\n'
        '8 tiparire cheltuieli de pe o zi mai mare de o anumita suma (ex: suma, zi)\n\n'

        'Rapoarte\n'
        '9 suma totala pentru un anumit tip de cheltuiala\n'
        '10 toate apartamentele sortate dupa un anumit tip de cheltuiala\n'
        '11 total cheltuieli pentru un apartament\n\n'

        'Filtru\n'
        '12 elimina toate cheltuielile de un anumit tip\n'
        '13 elimina toate cheltuielile mai mici decat o suma data\n\n'

        'Undo\n'
        '14 refacere ultima operatie\n'
        
        '15 Lista cheltuieli\n'
        '16 Exit\n\n')
    
    def __showAllCheltuieli(self):
        """
        Show all the cheltuieli
        """
        cheltuieli = self.__srv.getAllCheltuieli()
        if(len(cheltuieli) == 0):
            print('No cheltuieli has been made!')
        else:
            print(cheltuieli)
    
    def __adaugare(self):
        """
        Adding a cheltuiala
        """
        try:
            id = input('Dati id-ul: ')
            apartament = int(input('Dati apartamentul: '))
            suma = float(input('Dati suma: '))
            tip = input('Dati tip-ul: ')
            data = input('Dati data (yyyy-mm-dd): ')
            data = data.split('-')
            year = int(data[0])
            month = int(data[1])
            day = int(data[2])

            cheltuiala = self.__srv.createCheltuiala(id, apartament, suma, tip, datetime.date(year, month, day))
            print(f'Cheltuiala : {cheltuiala} adaugata cu succes')
        except ValueError as ex:
            print(ex)
        except RepositoryException as ex:
            print(ex)
        except Exception as ex:
            print(ex)
    
    def __update(self):
        """
        Updating a cheltuiala
        """
        try:
            oldID = input('Dati id-ul ce doriti sa-l modificati: ')
            id = input('Dati noul id: ')
            apartament = int(input('Dati noul apartament: '))
            suma = float(input('Dati noua suma: '))
            tip = input('Dati noul tip: ')
            data = input('Dati noua data (yyyy-mm-dd): ')
            data = data.split('-')
            year = data[0]
            month = data[1]
            day = data[2]

            cheltuiala = self.__srv.updateCheltuiala(oldID, id, apartament, suma, tip, datetime.date(year, month, day))
            print(f'Cheltuiala cu id {oldID} updatata cu success la {cheltuiala}')
        except ValueError as ex:
            print(ex)
        except RepositoryException as ex:
            print(ex)
        except Exception as ex:
            print(ex)

    def __deleteAllApartament(self):
        """
        Delete all cheltuiala from an apartament
        """
        apartament = int(input('Dati apartamentul: '))
        lista = self.__srv.deleteCheltuieliApartament(apartament)
        print(f'Cheltuieli sterse :\n {lista}')

    def __deleteAllApartamentConsecutive(self):
        """
        Delete all cheltuiala from a couple consecutive apartaments
        """
        start = int(input('Dati apartamentul de inceput: '))
        stop = int(input('Dati apartamentul de final: '))
        lista = self.__srv.deleteCheltuieliApartamentConsecutiv(start, stop)
        print(f'Cheltuieli sterse pentru apartamentele de la {start} la {stop} :\n {lista}')
    
    def __deleteTip(self):
        """
        Delete all cheltuiala with a tip
        """
        tip = input('Dati tipul: ')
        lista = self.__srv.deleteTipCheltuieliApartament(tip)
        print(f'Cheltuieli sterse cu tipul {tip}:\n {lista}')

    def __findApartamentCheltuieliMare(self):
        """
        Find the apartaments that have amount of cheltuiala bigger than a suma
        """
        suma = float(input('Dati suma: '))
        apartamente = self.__srv.findApartamentCheltuieliSumaMare(suma)
        print(f'Apartamente ce au suma cheltuielilor > {suma} :\n {apartamente}')
    
    def __findCheltuieliTip(self):
        """
        Find all cheltuiala with tip
        """
        tip = input('Dati tipul: ')
        cheltuieli = self.__srv.findCheltuieliTip(tip)
        print(f'Cheltuieli ce au tipul {tip} :\n {cheltuieli}')

    def __findCheltuialaZiSuma(self):
        """
        Find all cheltuiala that are made in a day and have amount bigger than a suma
        """
        zi = int(input('Dati ziua: '))
        suma = float(input('Dati suma: '))
        cheltuieli = self.__srv.findApartamentCheltuieliZiSumaMare(zi, suma)
        print(f'Cheltuieli din ziua {zi} cu suma > {suma} :\n {cheltuieli}')

    def __raportTotalTip(self):
        """
        Raport total of a tip
        """
        tip = input('Dati tipul: ')
        sumaTip = self.__srv.sumTotalTip(tip)
        print(f'Total cheltuieli pentru tipul {tip} : {sumaTip}')


    def __raportSortatApartamentTip(self):
        """
        Raport of all the cheltuiala sorted after the amount of a tip
        """
        tip = input('Dati tipul: ')
        apartamente = self.__srv.sortApartamentTip(tip)
        print(f'Apartamente sortate dupa tipul {tip} :\n {apartamente}')

    def __raportCheltuieliApartament(self):
        """
        Raport of all the cheltuiala of an apartament
        """
        apartament = int(input('Dati apartamentul: '))
        sumaApartament = self.__srv.totalSumApartament(apartament)
        print(f'Cheltuielile apartamentului {apartament} : {sumaApartament}')

    
    def __removeAllTip(self):
        """
        Filter all the cheltuiala that are not tip
        """
        tip = input('Dati tipul: ')
        cheltuieli = self.__srv.removeCheltuieliTip(tip)
        print(f'Filtru Cheltuieli fara tipul {tip}:\n {cheltuieli}')

    def __removeAllSumaMica(self):
        """
        Filter all the cheltuiala that have amount bigger then suma
        """
        suma = float(input('Dati suma: '))
        cheltuieli = self.__srv.removeCheltuieliSumaMica(suma)
        print(f'Filtru Cheltuieli fara cheltuieli cu suma < {suma}:\n {cheltuieli}')


    def __undo(self):
        """
        Undo the last action
        """
        mesaj = self.__srv.undo()
        print(f'{mesaj}')

    def showUI(self):
        """
        Main program (controller)
        Show the option
        Take an option and show the result
        """
        while True:
            self.showMenu()
            cmd = int(input('Alegeti optiunea : '))

            match cmd:
                case 1:
                    self.__adaugare()
                case 2:
                    self.__update()
                case 3:
                    self.__deleteAllApartament()
                case 4:
                    self.__deleteAllApartamentConsecutive()
                case 5:
                    self.__deleteTip()
                case 6:
                    self.__findApartamentCheltuieliMare()
                case 7:
                    self.__findCheltuieliTip()
                case 8:
                    self.__findCheltuialaZiSuma()
                case 9:
                    self.__raportTotalTip()
                case 10:
                    self.__raportSortatApartamentTip()
                case 11:
                    self.__raportCheltuieliApartament()
                case 12:
                    self.__removeAllTip()
                case 13:
                    self.__removeAllSumaMica()
                case 14:
                    self.__undo()
                case 15:
                    self.__showAllCheltuieli()
                case 16:
                    print('Good bye...')
                    break
                case default:
                    print('Don\'t know this comand.')