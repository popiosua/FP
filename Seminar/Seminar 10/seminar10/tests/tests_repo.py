import unittest

from domain.player import TennisPlayer
from repository.repository import PlayersRepositoryMemory, PlayersRepositoryFile, PlayerAlreadyExistsException, \
    PlayerDoesNotExistException


class TestRepository(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp called")
        self.test_repo = PlayersRepositoryMemory()

    def test_store(self):
        print("test_store")
        self.assertEqual(len(self.test_repo.get_all()), 0)
        p = TennisPlayer("Test Player", "Country", 1286, 1100, 3522)
        self.test_repo.store(p)
        self.assertEqual(len(self.test_repo.get_all()), 1)

    def test_find(self):
        self.assertEqual(len(self.test_repo.get_all()), 0)
        p = TennisPlayer("Test Player", "Country", 1286, 1100, 3522)
        self.assertRaises(PlayerDoesNotExistException, self.test_repo.find, p.name, p.country)
        self.test_repo.store(p)
        self.assertEqual(len(self.test_repo.get_all()), 1)
        found_player = self.test_repo.find("Test Player", "Country")
        self.assertEqual(p, found_player)

    def test_get_all(self):
        print("test_get_all")
        self.assertEqual(len(self.test_repo.get_all()), 0)
        p1 = TennisPlayer("Test Player", "Country", 1286, 1100, 3522)
        self.test_repo.store(p1)
        self.assertEqual(len(self.test_repo.get_all()), 1)
        p2 = TennisPlayer("Test Player1", "Country2", 1286, 1100, 3522)
        self.test_repo.store(p2)
        self.assertEqual(len(self.test_repo.get_all()), 2)

    def tearDown(self) -> None:
        print("tearDown called")


class TestRepositoryFile(unittest.TestCase):
    def setUp(self):
        self.test_repo = PlayersRepositoryFile("test_players.txt")

    def test_store(self):
        self.assertEqual(len(self.test_repo.get_all()), 1)
        p1 = TennisPlayer("Test Player", "Country", 1286, 1100, 3522)
        self.test_repo.store(p1)
        self.assertEqual(len(self.test_repo.get_all()), 2)
        self.assertRaises(PlayerAlreadyExistsException, self.test_repo.store, p1)

    def tearDown(self):
        # replace whatever content we have added through a test with
        # something predefined - 1 player (can be more, can be empty file)
        # just test accordingly
        with open("test_players.txt", "w") as f:
            f.write("Casper Ruud,Norway,360,310,4360")
