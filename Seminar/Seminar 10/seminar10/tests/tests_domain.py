import unittest

from domain.player import TennisPlayer
from domain.tournament_evaluation import PlayerTournamentEvaluation, EvaluationError
from domain.validation import PlayerValidator, ValidationException


class TestDomain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_player(self):
        p = TennisPlayer("Test Player", "Country", 1286, 1100, 3522)
        self.assertEqual(p.name, "Test Player")
        self.assertEqual(p.country, "Country")
        self.assertEqual(p.matches_played, 1286)
        self.assertEqual(p.matches_won, 1100)
        self.assertEqual(p.points, 3522)

        p.name = "John Smith"
        self.assertEqual(p.name, "John Smith")
        p.country = "USA"
        self.assertEqual(p.country, "USA")
        p.matches_played = 1294
        self.assertEqual(p.matches_played, 1294)
        p.matches_won = 1102
        self.assertEqual(p.matches_won, 1102)

        p.points = 3800
        self.assertEqual(p.points, 3800)

    def test_equal_player(self):
        player1 = TennisPlayer("Rafael Nadal", "Spain", 1285, 1100, 11025)
        player2 = TennisPlayer("Rafael Nadal", "Spain", 1735, 1573, 12363)
        self.assertEqual(player1, player2)

        player3 = TennisPlayer("Carlos Alcaraz", "Spain", 1735, 1573, 12363)
        self.assertNotEqual(player1, player3)

    def test_validate_player(self):
        validator = PlayerValidator()
        player = TennisPlayer("Rafael Nadal", "Spain", 1285, 1100, 11025)
        result = validator.validate(player)
        self.assertIsNone(result)

        player1 = TennisPlayer("Rafael Nadal", "Spain", -100, 1100, 11025)
        self.assertRaises(ValidationException, validator.validate, player1)

        player2 = TennisPlayer("Rafael Nadal", "Spain", 1328, -6, 11025)
        self.assertRaises(ValidationException, validator.validate, player2)

        player3 = TennisPlayer("Rafael Nadal", "Spain", 1328, 1500, 11025)
        self.assertRaises(ValidationException, validator.validate, player3)

    def tearDown(self) -> None:
        pass


class TestEvaluation(unittest.TestCase):
    def test_evaluation(self):
        player1 = TennisPlayer("Rafael Nadal", "Spain", 1000, 920, 10000)
        ev1 = PlayerTournamentEvaluation(player1, 100, "w")
        self.assertEqual(ev1.get_number_of_points(), 10100)

        ev2 = PlayerTournamentEvaluation(player1, 100, "f")
        self.assertEqual(ev2.get_number_of_points(), 10050)

        ev3 = PlayerTournamentEvaluation(player1, 1000, "sf")
        self.assertEqual(ev3.get_number_of_points(), 10250)

        ev4 = PlayerTournamentEvaluation(player1, 1000, "qf")
        self.assertEqual(ev4.get_number_of_points(), 10125)

        ev5 = PlayerTournamentEvaluation(player1, 800, "r16")
        self.assertEqual(ev5.get_number_of_points(), 10050)

        self.assertEqual(ev5.player, player1)

        ev6 = PlayerTournamentEvaluation(player1, 10, "other_result")
        self.assertRaises(EvaluationError, ev6.get_number_of_points)


if __name__ == "__main__":
    unittest.main()
