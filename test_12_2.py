import unittest
from run import Runner
from run import Tournament

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for results in cls.all_results.values():
            print(results)

    def test_race_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = {rank: runner.name for rank, runner in results.items()}
        self.assertEqual(self.all_results[len(self.all_results)][1], "Усэйн")

    def test_race_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = {rank: runner.name for rank, runner in results.items()}
        self.assertEqual(self.all_results[len(self.all_results)][1], "Андрей")

    def test_race_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = {rank: runner.name for rank, runner in results.items()}
        self.assertEqual(self.all_results[len(self.all_results)][1], "Усэйн")


if __name__ == "__main__":
    unittest.main()