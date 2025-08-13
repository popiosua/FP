from domain.validators import StudentValidator
from repository.inmemory import StudentRepository
from repository.file import StudentFileRepository
from services.services import StudentService
from ui.console import ConsoleUI
from ui.gui import StudentGUI
from ui.web import WebPagesUI

#Application coordinator
#Use dependency injection pattern to asemble the application

#create a validator
val = StudentValidator()

#create repository
# repo = StudentRepository()

repo = StudentFileRepository("students.txt")

#create controller and inject dependencies
serv = StudentService(val, repo)

#create console ui and provide (inject) the controller
# ui = ConsoleUI(serv)
# ui = StudentGUI(serv)
ui = WebPagesUI(serv)
ui.startUI()

