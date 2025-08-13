from domain.player import TennisPlayer
from domain.tournament_evaluation import PlayerTournamentEvaluation


class PlayerService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__val = validator

    def add(self, name: str, country: str, matches_played: int, matches_won: int, points: int):
        """
        Adauga un jucator cu informatiile date
        :param name: numele jucatorului
        :param country: tara de origine a jucatorului
        :param matches_played: numarul de meciuri jucate de-a lungul carierei
        :param matches_won: numarul de meciuri castigate de-a lungul carierei
        :param points: numarul de puncte
        :return: -;
        :raises: PlayerAlreadyExistsException daca un jucator cu numele si tara data exista deja
                 ValidationException daca datele jucatorului sunt invalide
        """
        p = TennisPlayer(name, country, matches_played, matches_won, points)
        self.__val.validate(p)
        self.__repo.store(p)

    def filter_players(self, country: str, threshold: float) -> list:
        """
        Returneaza lista de jucatori din tara country cu numar de puncte mai mare de threshold
        :param country: tara dupa care se filtreaza
        :param threshold: numarul de puncte
        :return: lista de jucatori care indeplinesc criteriile
        """
        all_players = self.__repo.get_all()
        players_from_country = [player for player in all_players if
                                player.country == country and player.points > threshold]
        return players_from_country

    def sort_by_win_percentage(self) -> list:
        """
        Sorteaza lista de jucatori dupa procentajul de meciuri castigate
        :return: lista de jucatori sortata
        """
        all_players = self.__repo.get_all()
        # alternativa: adaugare atribut win_percentage in TennisPlayer
        sorted_players = sorted(all_players, key=lambda player: player.matches_won / player.matches_played,
                                reverse=True)
        return sorted_players

    def evaluate_player(self, player_name: str, player_country: str, tournament_points: int,
                        result: str) -> PlayerTournamentEvaluation:
        """
        Simuleaza evolutia unui jucator intr-un turneu
        :param player_name: numele jucatorului
        :param player_country: tara de origine a jucatorului
        :param tournament_points: numarul de puncte care se acorda in turneu
        :param result: rezultatul jucatorului in turneu
        :return: evaluarea aferenta evolutiei jucatorului
        """
        player = self.__repo.find(player_name, player_country)
        return PlayerTournamentEvaluation(player, tournament_points, result)

    def get_all(self):
        """
        Returneaza colectia de jucatori
        :return:
        """
        return self.__repo.get_all()