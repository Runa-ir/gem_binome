import unittest


class WordWrapper(object):

    def wrap(self, words, column_number):
        if len(words) > column_number:
            return words[:column_number] + '\n' + words[column_number + 1:]
        return words


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
        self.assertEqual("dummy\nstring", actual_string)


if __name__ == '__main__':
    unittest.main()
