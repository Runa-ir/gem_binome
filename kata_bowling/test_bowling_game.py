import unittest

class BowlingGame(object):

    def __init__(self):
        self.points = 0
        self.last_rolls = []
        self.nb_strikes = 0

    def roll(self, pins):
        self.points += pins

        last_two_rolls = self.last_rolls[-2:]
        if 10 in last_two_rolls:
            for i in range(last_two_rolls.count(10)):
                self.points += pins
        else:
            if len(self.last_rolls) and (len(self.last_rolls) + self.nb_strikes) % 2 == 0:
                if sum(last_two_rolls) == 10:
                    self.points += pins

        self.last_rolls.append(pins)
        if pins == 10:
            self.nb_strikes += 1

    def score(self):
        return self.points

class TestBowlingGame(unittest.TestCase):

    def play_bowling_game(self, pins_list):
        bowling_game = BowlingGame()
        for pin in pins_list:
            bowling_game.roll(pin)

        return bowling_game

    def test_that_score_is_0_when_no_pin_down(self):
        pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(0, bowling_game.score())

    def test_that_score_is_number_of_pins_down(self):
        pins = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(3, bowling_game.score())

        pins = [3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(8, bowling_game.score())

    def test_spare_result(self):
        pins = [3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(10, bowling_game.score())

        pins = [3, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(18, bowling_game.score())

        pins = [3, 7, 4, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(32, bowling_game.score())

    def test_strike_result(self):
        pins = [10, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(18, bowling_game.score())

        pins = [10, 4, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(31, bowling_game.score())

        pins = [10, 10, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(51, bowling_game.score())

        pins = [10, 5, 3, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(46, bowling_game.score())

    def test_combination_of_strikes_and_spares(self):
        pins = [10, 5, 5, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(64, bowling_game.score())

        pins = [0, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(22, bowling_game.score())


if __name__ == '__main__':
    unittest.main()
