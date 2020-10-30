from gem_binome.content_checker import ContentChecker
from gem_binome.division_checker import DivisionChecker


class FooBarQix(object):

    def __init__(self, digit_map):
        self.map = digit_map
        self.division_checker = DivisionChecker(digit_map)
        self.content_checker = ContentChecker(digit_map)

    def generate(self, number):

        res = self.division_checker.divisible_by_number(number)

        res += self.content_checker.contains_number(number)

        if res != '':
            return res

        return str(number)

