import unittest


class PhoneNumberChecker:

    def __init__(self, phone_book: dict):
        self.phone_book = phone_book
        self.numbers = self._extract_numbers()

    def _extract_numbers(self) -> list:
        return list(self.phone_book.values())

    def check_consistency(self):
        numbers_list = self.numbers
        for n in numbers_list:
            numbers_list.pop(0)
            for m in numbers_list:
                if m.startswith(n) or n.startswith(m):
                    return False

        return True


class TestPhoneNumbers(unittest.TestCase):
    def test_no_number_starts_with_another_number(self):
        phone_book = {'Nick': "123", "Frank": "12"}
        number_checker = PhoneNumberChecker(phone_book)
        self.assertEqual(False, number_checker.check_consistency())

        phone_book = {'Nick': "323", "Frank": "12"}
        number_checker = PhoneNumberChecker(phone_book)
        self.assertEqual(True, number_checker.check_consistency())




if __name__ == '__main__':
    unittest.main()
