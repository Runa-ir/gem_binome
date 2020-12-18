import unittest


class PhoneNumberChecker:

    def __init__(self, phone_book: dict):
        self.phone_book = phone_book
        self.numbers = self._normalize_numbers(self._extract_numbers())

    def _extract_numbers(self) -> list:
        return list(self.phone_book.values())

    def _normalize_numbers(self, numbers):
        return ["".join(filter(str.isalnum, number)) for number in numbers]

    def check_consistency(self):
        numbers_list = self.numbers.copy()
        for n in self.numbers:
            numbers_list.pop(0)
            for m in numbers_list:
                if m.startswith(n) or n.startswith(m):
                    print(m, n)
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

        phone_book = {'Nick': "323", "Frank": "12", "Anna": "441"}
        number_checker = PhoneNumberChecker(phone_book)
        self.assertEqual(True, number_checker.check_consistency())

    def test_to_normalize_for_numbers(self):
        phone_book = {'Nick': "1-23", "Frank": "12-3"}
        number_checker = PhoneNumberChecker(phone_book)
        self.assertEqual(False, number_checker.check_consistency())



    def test_check_consistence_of_a_small_file(self):
        with open("phone_data_10000.txt", "r") as file:
            data = file.read()
            data = data.split("\n")
            phone_book = {}
            for line in data[1:]:
                try:
                    (name, number) = line.split(",")
                except ValueError:
                    continue
                phone_book[name] = number
        number_checker = PhoneNumberChecker(phone_book)
        self.assertEqual(True, number_checker.check_consistency())



if __name__ == '__main__':
    unittest.main()
