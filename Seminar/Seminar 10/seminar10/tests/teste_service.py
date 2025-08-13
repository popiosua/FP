import unittest

from domain.player import TennisPlayer
from domain.validation import PlayerValidator, ValidationException
from repository.repository import PlayersRepositoryFile, PlayerAlreadyExistsException, PlayerDoesNotExistException
from service.service import PlayerService


class TestService(unittest.TestCase):
    def setUp(self) -> None:
        test_repo = PlayersRepositoryFile("test_players_for_service.txt")
        validator = PlayerValidator()
        self.test_service = PlayerService(test_repo, validator)

    def test_add_player(self):
        initial_size = len(self.test_service.get_all())
        self.test_service.add("Player name", "Country", 1200, 1023, 12000)
        self.assertEqual(len(self.test_service.get_all()), initial_size + 1)
        self.assertRaises(PlayerAlreadyExistsException, self.test_service.add, "Player name", "Country", 1200, 1023,
                          12000)
        self.assertRaises(ValidationException, self.test_service.add, "Player name", "Country", 1200, 1280, 12000)

    def test_filter(self):
        country = "Spain"
        threshold1 = 1000
        # Rafael Nadal,Spain,1285,1120,12400
        # Carlos Alcaraz,Spain,172,150,8945

        player1 = TennisPlayer("Rafael Nadal", "Spain", 1285, 1120, 12400)
        player2 = TennisPlayer("Carlos Alcaraz", "Spain", 172, 150, 8945)
        filtered_list = self.test_service.filter_players(country, threshold1)
        self.assertEqual(len(filtered_list), 2)
        self.assertIn(player1, filtered_list)
        self.assertIn(player2, filtered_list)

        threshold2 = 12000
        filtered_list2 = self.test_service.filter_players(country, threshold2)
        self.assertEqual(len(filtered_list2), 1)
        self.assertIn(player1, filtered_list)


        threshold3 = 15500
        filtered_list3 = self.test_service.filter_players(country, threshold3)
        self.assertEqual(len(filtered_list3), 0)

        country = "Romania"
        threshold4 = 1000
        filtered_list4 = self.test_service.filter_players(country, threshold4)
        self.assertEqual(len(filtered_list4), 0)

    def test_sort(self):
        sorted_list = self.test_service.sort_by_win_percentage()
        first_player = TennisPlayer("Daniil Medvedev", "Russia", 725, 650, 7280)
        self.assertEqual(sorted_list[0], first_player)

        last_player = TennisPlayer("Alexander Zverev", "Germany", 620, 510, 4465)
        self.assertEqual(sorted_list[-1], last_player)


    def test_evaluate_player(self):
        #Rafael Nadal,Spain,1285,1120,12400
        ev1 = self.test_service.evaluate_player("Rafael Nadal", "Spain", 100, "sf")
        self.assertEqual(ev1.get_number_of_points(), 12425)
        ev2 = self.test_service.evaluate_player("Rafael Nadal", "Spain", 1000, "qf")
        self.assertEqual(ev2.get_number_of_points(), 12525)
        ev3 = self.test_service.evaluate_player("Rafael Nadal", "Spain", 550, "w")
        self.assertEqual(ev3.get_number_of_points(), 12950)
        ev2 = self.test_service.evaluate_player("Rafael Nadal", "Spain", 180, "f")
        self.assertEqual(ev2.get_number_of_points(), 12490)
        ev2 = self.test_service.evaluate_player("Rafael Nadal", "Spain", 80, "r16")
        self.assertEqual(ev2.get_number_of_points(), 12405)
        self.assertRaises(PlayerDoesNotExistException, self.test_service.evaluate_player, "Rafa", "Spain", 1942, "w")


    def tearDown(self) -> None:
        with open("test_players_for_service.txt", "w") as f:
            default_file = open("default_players.txt", 'r')
            default_players = default_file.read()
            default_file.close()
            f.write(default_players)
