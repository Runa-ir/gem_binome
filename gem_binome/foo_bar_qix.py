from gem_binome.division_checker import DivisionChecker


class FooBarQix(object):

    def __init__(self, digit_map):
        self.map = digit_map
        self.division_checker = DivisionChecker(digit_map)

    def generate(self, number):

        res = self.division_checker.divisible_by_number(number)

        res += self._contains_number(number)

        if res != '':
            return res

        return str(number)

    def _contains_number(self, number):
        res = ''
        for char in str(number):
            for k, v in self.map.items():
                if char == str(k):
                    res += v
        return res

