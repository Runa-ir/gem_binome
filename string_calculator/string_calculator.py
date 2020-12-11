import re


class StringCalculator(object):

    def add(self, numbers: str):

        if not numbers:
            return 0

        numbers, regex = self._extract_delimiter(numbers)
        integers = self._extract_integers(numbers, regex)
        self._handle_negatives(integers)

        return sum(integers)

    def _extract_integers(self, numbers, regex):
        integers = [int(num) for num in re.split(regex, numbers) if int(num) < 1000]
        return integers

    def _handle_negatives(self, integers):
        negatives = [num for num in integers if num < 0]
        if negatives:
            raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")

    def _extract_delimiter(self, numbers):
        regex = ",|\n"
        if numbers.startswith('//'):
            delimiter = numbers.split("\n", 1)[0][2:]
            numbers = numbers.split("\n", 1)[1]
            regex += f"|{delimiter}"
        return numbers, regex


