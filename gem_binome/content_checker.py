class ContentChecker:

    def __init__(self, digit_map):
        self.map = digit_map

    def contains_number(self, number):
        res = ''
        for char in str(number):
            for k, v in self.map.items():
                if char == str(k):
                    res += v
        return res