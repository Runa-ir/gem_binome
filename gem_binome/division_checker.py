class DivisionChecker:

    def __init__(self, digit_map):
        self.map = digit_map

    def divisible_by_number(self, number):
        res = ''

        for k, v in self.map.items():
            if number % k == 0:
                res += v

        return res
