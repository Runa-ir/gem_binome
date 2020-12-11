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

    def test_should_handle_new_separator_if_provided(self):
        self.assertEqual(3, StringCalculator().add("//;\n1;2"))

    def test_should_throw_exception_if_negative_numbers_are_passed(self):
        with self.assertRaises(Exception) as context:
            StringCalculator().add("-1,2")
        self.assertEqual("Negatives not allowed: -1", context.exception.args[0])

    def test_should_ignore_numbers_greater_than_1000(self):
        self.assertEqual(2, StringCalculator().add("1001,2"))

if __name__ == '__main__':
    unittest.main()
