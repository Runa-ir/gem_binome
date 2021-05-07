
MAP_SYMBOL_NUMBER = {
    "  |": [0, 1, 7],
    "| |": [0],
    "   ": [1],
    " _ ": [0, 2, 3, 4, 5, 6, 7, 8, 9],
    " _|": [2, 3, 5, 9],
    "|_ ": [2, 5, 6],
    "|_|": [0, 4, 6, 8, 9]
}


class BankOCR:
    def _recognize_pattern(self, pattern):
        return MAP_SYMBOL_NUMBER[pattern]

    def _recognize_digit(self, mosaic):
        digit = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        for pattern in mosaic:
            digit = digit.intersection(set(self._recognize_pattern(pattern)))

        if digit == {2, 5}:
            digit = self._define_two_or_five(mosaic)
        return digit.pop()

    def _define_two_or_five(self, mosaic):
        if mosaic[1] == " _|":
            return {2}
        else:
            return {5}

    def _split_mosaic_into_pieces(self, mosaic):
        split_full_mosaic = []
        for pattern in mosaic:
            split_pattern = []
            sub_pattern = ""
            for idx, char in enumerate(pattern):
                sub_pattern += char
                if (idx + 1) % 3 == 0:
                    split_pattern.append(sub_pattern)
                    sub_pattern = ""
            split_full_mosaic.append(split_pattern)
        return split_full_mosaic

    def recognize_digit_sequence(self, mosaic):
        digit_sequence = []
        sub_mosaic_list = []
        split_full_mosaic = self._split_mosaic_into_pieces(mosaic)

        for i in range(len(split_full_mosaic[0])):
            sub_mosaic_list.append([split_full_mosaic[0][i], split_full_mosaic[1][i], split_full_mosaic[2][i]])

        for mosaic in sub_mosaic_list:
            digit_sequence.append(self._recognize_digit(mosaic))

        return digit_sequence


class TestBankOCR:

    def test_recognize_pattern(self):
        bank_ocr = BankOCR()
        assert [1] == bank_ocr._recognize_pattern("   ")

    def test_recognize_digit(self):
        bank_ocr = BankOCR()
        assert 2 == bank_ocr._recognize_digit([" _ ", " _|", "|_ "])

    def test_recognize_digit_sequence(self):
        bank_ocr = BankOCR()
        assert [2, 6] == bank_ocr.recognize_digit_sequence([" _  _ ", " _||_ ", "|_ |_|"])
        assert [2] == bank_ocr.recognize_digit_sequence([" _ ", " _|", "|_ "])

