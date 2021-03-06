import unittest
from typing import Tuple, Optional


class BowlingGame(object):

    def __init__(self):
        self.points = 0
        self.round_history = []

    def roll(self, pins):
        pre_round = self.define_pre_round()
        pre_pre_round = self.define_pre_pre_round()

        self.count_current_roll(pins, pre_round)
        self.deal_with_possible_strike(pins, pre_pre_round, pre_round)
        self.deal_with_possible_spare(pins, pre_round)

        self.update_round_history(pins)

    def count_current_roll(self, pins, pre_round):
        if len(self.round_history) < 10 or (pre_round and sum(pre_round) < 10):
            self.points += pins

    def define_pre_round(self) -> Optional[Tuple]:
        if len(self.round_history) > 0:
            return self.round_history[-1]
        return None

    def define_pre_pre_round(self) -> Optional[Tuple]:
        if len(self.round_history) > 1:
            return self.round_history[-2]
        return None

    def deal_with_possible_strike(self, pins, pre_pre_round, pre_round):
        if pre_pre_round:
            if len(pre_pre_round) == 1 and pre_pre_round[0] == 10 and len(pre_round) == 1:
                self.points += pins
        if pre_round:
            if len(pre_round) == 1 and pre_round[0] == 10:
                self.points += pins
            # Last round strike case
            if len(self.round_history) == 10 and len(pre_round) == 2 and pre_round[0] == 10:
                self.points += pins

    def deal_with_possible_spare(self, pins, pre_round):
        if pre_round:
            if len(pre_round) == 2 and sum(pre_round) == 10:
                self.points += pins

    def update_round_history(self, pins):
        new_round_criteria = (
            (not self.round_history or sum(self.round_history[-1]) == 10 or len(self.round_history[-1]) == 2)
            and len(self.round_history) < 10
        )
        if new_round_criteria:
            self.round_history.append((pins,))
        else:
            self.round_history[-1] += (pins,)

    def score(self) -> int:
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

        pins = [0, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(22, bowling_game.score())

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

    def test_last_round_cases(self):
        pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 6]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(19, bowling_game.score())

        pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 4, 6]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(16, bowling_game.score())

    def test_combination_of_strikes_and_spares(self):
        pins = [10, 5, 5, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        self.assertEqual(64, bowling_game.score())

    def test_update_round_history(self):
        pins = [10, 5, 5, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        expected_round_history = [(10,), (5, 5), (10,), (5, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.assertEqual(expected_round_history, bowling_game.round_history)

        pins = [0, 10, 5, 5, 10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bowling_game = self.play_bowling_game(pins)
        expected_round_history = [(0, 10), (5, 5), (10,), (5, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.assertEqual(expected_round_history, bowling_game.round_history)


if __name__ == '__main__':
    unittest.main()
