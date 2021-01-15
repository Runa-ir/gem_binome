import unittest


class PhoneNumberChecker:

    def __init__(self, phone_book: dict):
        self.phone_book = self._normalize_phone_book(phone_book)
        self.order_phone_book()

    def _normalize_phone_book(self, phone_book):
        normalized = {}
        for name, number in phone_book.items():
            normalized[name] = "".join(filter(str.isalnum, number))
        return normalized

    def order_phone_book(self):
        ordered = sorted(self.phone_book.items(), key=lambda item: item[1])
        self.phone_book = {k: v for k, v in ordered}

    def check_consistency(self):
        phone_book = self.phone_book.copy()
        for name, number in self.phone_book.items():
            phone_book.pop(name)
            if phone_book:
                next_name = list(phone_book.keys())[0]
                next_number = phone_book[next_name]

                if next_number.startswith(number):
                    print(name, number)
                    print(next_name, next_number)
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

    def test_to_order_phone_book_by_numbers(self):
        phone_book = {'Nick': "323", "Frank": "12", "Anna": "441"}
        number_checker = PhoneNumberChecker(phone_book)
        self.assertEqual({"Frank": "12", 'Nick': "323", "Anna": "441"}, number_checker.phone_book)

        phone_book = {'Nick': "123", "Frank": "12"}
        number_checker = PhoneNumberChecker(phone_book)
        self.assertEqual({"Frank": "12", 'Nick': "123"}, number_checker.phone_book)


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
        self.assertEqual(False, number_checker.check_consistency())


if __name__ == '__main__':
    unittest.main()
