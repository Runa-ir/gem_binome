import unittest


class WordWrapper(object):

    def wrap(self, words, column_number):
        return words


class TestsWordWrapper(unittest.TestCase):

    def test_should_not_wrap_when_column_number_larger_than_string_size(self):
        expected_string = "dummy_string"
        column_number = 17
        wrapper = WordWrapper()
        actual_string = wrapper.wrap(expected_string, column_number)
        self.assertEqual(expected_string, actual_string)


if __name__ == '__main__':
    unittest.main()
