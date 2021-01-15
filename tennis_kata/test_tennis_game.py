import unittest

from tennis_kata.tennis_game import TennisGame


class TestTennisGame(unittest.TestCase):

    def setUp(self):
        self.tennis_game = TennisGame()

    def set_score(self, player_name, score):
        for i in range(score):
            self.tennis_game.won_point(player_name)

    def test_initial_score_is_love_love(self):
        self.assertEqual(self.tennis_game.get_score(), "Love - Love")

    def test_player_score_is_fifteen_when_player_scores_for_the_first_time(self):
        self.tennis_game.won_point("player1")
        self.assertEqual(self.tennis_game.get_score(), "Fifteen - Love")

    def test_score_after_several_points(self):
        self.set_score("player1", 3)
        self.set_score("player2", 1)
        self.assertEqual(self.tennis_game.get_score(), "Forty - Fifteen")

    def test_equality_situation(self):
        self.set_score("player1", 3)
        self.set_score("player2", 3)
        self.assertEqual(self.tennis_game.get_score(), "Deuce")

    def test_advantage_situation(self):
        self.set_score("player1", 3)
        self.set_score("player2", 4)
        self.assertEqual(self.tennis_game.get_score(), "Advantage player2")

        self.tennis_game.won_point("player1")
        self.assertEqual(self.tennis_game.get_score(), "Deuce")

    def test_end_of_game(self):
        self.set_score("player1", 4)
        self.assertEqual(self.tennis_game.get_score(), "Win for player1")

        self.set_score("player2", 6)
        self.assertEqual(self.tennis_game.get_score(), "Win for player2")


if __name__ == '__main__':
    unittest.main()
