import re


class StringCalculator(object):

    def add(self, numbers: str):

        if not numbers:
            return 0

        return sum([int(num) for num in re.split(",|\n", numbers)])
