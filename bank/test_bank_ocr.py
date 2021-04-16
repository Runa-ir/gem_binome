
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
    def recognize_pattern(self, pattern):
        return MAP_SYMBOL_NUMBER[pattern]

    def recognize_digit(self, mosaic):
        digit = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        for pattern in mosaic:
            digit = digit.intersection(set(self.recognize_pattern(pattern)))

        return list(digit)


class TestBankOCR:

    def test_recognize_pattern(self):
        bank_ocr = BankOCR()
        assert [1] == bank_ocr.recognize_pattern("   ")

    def test_recognize_digit(self):
        bank_ocr = BankOCR()
        assert [2, 5] == bank_ocr.recognize_digit([" _ ", " _|", "|_ "])
