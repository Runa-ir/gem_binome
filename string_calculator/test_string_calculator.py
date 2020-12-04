import unittest

from string_calculator import StringCalculator


class StringCalculatorTestCase(unittest.TestCase):
    def test_should_return_zero_when_input_empty(self):
        self.assertEqual(0, StringCalculator().add(""))

    def test_should_return_number_if_single_number_passed(self):
        self.assertEqual(1, StringCalculator().add("1"))

    def test_should_return_sum_if_two_numbers_passed(self):
        self.assertEqual(8, StringCalculator().add("3, 5"))

    def test_should_handle_new_lines_between_numbers(self):
        self.assertEqual(6, StringCalculator().add("1\n2,3"))


if __name__ == '__main__':
    unittest.main()
