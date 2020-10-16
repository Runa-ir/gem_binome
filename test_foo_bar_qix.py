import unittest

from foo_bar_qix import FooBarQix

class FooBarQixTest(unittest.TestCase):

    def test_should_return_number_when_number(self):
        self.assertEqual("2", self.foo_bar_qix.generate(2))

    def test_should_return_foo_when_divisible_by_three(self):
        self.assertEqual("Foo", self.foo_bar_qix.generate(9))

    def test_should_return_bar_when_divisible_by_five(self):
        self.assertEqual("Bar", self.foo_bar_qix.generate(10))

    def test_should_return_qix_when_number_divisible_by_seven(self):
        self.assertEqual("Qix", self.foo_bar_qix.generate(14))

    def test_should_return_foofoo_when_number_contains_three_and_is_divisible_by_three(self):
        self.assertEqual("FooFoo", self.foo_bar_qix.generate(3))

    def setUp(self):
        self.foo_bar_qix = FooBarQix()

if __name__ == '__main__':
    unittest.main()
