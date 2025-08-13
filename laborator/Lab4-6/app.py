from domain.cheltuiala import Cheltuiala
from domain.validators import CheltuialaValidator
from repository.fileRepository import FileRepository
from services.cheltuialaService import CheltuialaService, dummy
from ui.console import Console
from utils.fileutile import clearFileContent

def run():
    fileName = "cheltuieli.txt"

    clearFileContent(fileName)
    rep = FileRepository(fileName)
    dummy(rep)
    val = CheltuialaValidator()

    serv = CheltuialaService(rep, val)

    ui = Console(serv)

    ui.showUI()

if __name__ == '__main__':
    run()