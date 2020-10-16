import unittest


class FooBarQix(object):

    def generate(self, number):

        return "1"


class FooBarQixTest(unittest.TestCase):
    def test_should_return_one_when_number_is_one(self):

        foo_bar_qix = FooBarQix()
        actual = foo_bar_qix.generate(1)
        self.assertEqual("1", actual)

if __name__ == '__main__':
    unittest.main()
