import re


class StringCalculator(object):

    def add(self, numbers: str):

        if not numbers:
            return 0

        regex = ",|\n"
        if numbers.startswith('//'):
            separator = numbers.split("\n", 1)[0][2:]
            numbers = numbers.split("\n", 1)[1]
            regex += f"|{separator}"

        integers = [int(num) for num in re.split(regex, numbers)]
        negatives = [num for num in integers if num < 0]

        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")

        return sum(integers)
