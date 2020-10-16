import unittest


class FooBarQix(object):

    def generate(self, number):

        if number %3 == 0:
            return "Foo"
        if number %5 == 0:
            return "Bar"
        return str(number)


class FooBarQixTest(unittest.TestCase):
    def test_should_return_number_when_number(self):

        foo_bar_qix = FooBarQix()
        actual = foo_bar_qix.generate(2)
        self.assertEqual("2", actual)

    def test_should_return_foo_when_divisible_by_three(self):

        foo_bar_qix = FooBarQix()
        actual = foo_bar_qix.generate(9)
        self.assertEqual("Foo", actual)

    def test_should_return_bar_when_divisible_by_five(self):
        foo_bar_qix = FooBarQix()
        actual = foo_bar_qix.generate(10)
        self.assertEqual("Bar", actual)

if __name__ == '__main__':
    unittest.main()
