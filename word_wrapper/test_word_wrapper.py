import unittest

from word_wrapper.word_wrapper import WordWrapper


class TestsWordWrapper(unittest.TestCase):

    def test_should_not_wrap_when_column_number_larger_than_string_size(self):
        expected_string = "dummy_string"
        column_number = 17
        wrapper = WordWrapper()
        actual_string = wrapper.wrap(expected_string, column_number)
        self.assertEqual(expected_string, actual_string)

    def test_should_break_at_the_boundary_when_column_number_matches_a_space_position_between_two_words(self):
        input_string = "dummy string"
        column_number = 5
        wrapper = WordWrapper()
        actual_string = wrapper.wrap(input_string, column_number)
        self.assertEqual("dummy\nstrin\ng", actual_string)

    def test_break_at_boundary_when_column_number_does_not_match_a_spoce_position_between_two_words(self):
        input_string = "dummy string"
        column_number = 7
        wrapper = WordWrapper()
        actual_string = wrapper.wrap(input_string, column_number)
        self.assertEqual("dummy\nstring", actual_string)

    def test_should_wrap_the_word_if_column_number_smaller_than_first_space_index(self):
        input_string = "dummy"
        column_number = 3
        wrapper = WordWrapper()
        actual_string = wrapper.wrap(input_string, column_number)
        self.assertEqual("dum\nmy", actual_string)

    def test_should_wrap_the_word_multiple_times_if_multiple_wraps_can_fit_before_first_space(self):
        input_string = "dummylongstring"
        column_number = 5
        wrapper = WordWrapper()
        actual_string = wrapper.wrap(input_string, column_number)
        self.assertEqual("dummy\nlongs\ntring", actual_string)


if __name__ == '__main__':
    unittest.main()
