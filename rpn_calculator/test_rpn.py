import unittest


def sum(a, b):
    return str(int(a) + int(b))


def subtract(a, b):
    return str(int(a) - int(b))


def multiply(a, b):
    return str(int(a) * int(b))


def divide(a, b):
    return str(int(a) // int(b))


map_operation = {"*": multiply, "-": subtract, "/": divide, "+": sum}


def evaluate(expression):
    separate_symbols = expression.split(" ")

    stack = []
    for symbol in separate_symbols:
        if symbol not in map_operation.keys():
            stack.append(symbol)
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(map_operation[symbol](left, right))

    return "".join(stack)


class TestRPN(unittest.TestCase):

    def test_get_number_when_number_given(self):
        result = evaluate("3")
        self.assertEqual("3", result)

    def test_get_number_formed_by_digits(self):
        result = evaluate("3 4 5")
        self.assertEqual("345", result)

    def test_get_new_line_when_enter_given(self):
        result = evaluate("3\n4 5")
        self.assertEqual(result, "3\n45")

    def test_get_math_operation_when_operator_is_given_between_two_numbers(self):
        result = evaluate("20 5 /")
        self.assertEqual(result, "4")

        result = evaluate("20 5 / 3 -")
        self.assertEqual(result, "1")

        result = evaluate("4 2 + 3 -")
        self.assertEqual(result, "3")

        result = evaluate("3 5 8 * 7 + *")
        self.assertEqual(result, "141")

if __name__ == '__main__':
    unittest.main()
