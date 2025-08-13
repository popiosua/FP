from domain.validation import PlayerValidator
from repository.repository import PlayersRepositoryFile
from service.service import PlayerService
from ui.console import Console

repo = PlayersRepositoryFile("data/players.txt")
val = PlayerValidator()
srv = PlayerService(repo, val)
console = Console(srv)
console.run()
