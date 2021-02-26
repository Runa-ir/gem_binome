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


class RPNEvaluator(object):

    def evaluate(self, expression):
        separate_symbols = expression.split(" ")
        last_char = separate_symbols[-1]
        if last_char in map_operation.keys():
            return map_operation[last_char](separate_symbols[0], separate_symbols[1])
        return "".join(separate_symbols)


class TestRPN(unittest.TestCase):

    def test_get_number_when_number_given(self):
        rpn = RPNEvaluator()
        result = rpn.evaluate("3")
        self.assertEqual("3", result)

    def test_get_number_formed_by_digits(self):
        rpn = RPNEvaluator()
        result = rpn.evaluate("3 4 5")
        self.assertEqual("345", result)

    def test_get_new_line_when_enter_given(self):
        rpn = RPNEvaluator()
        result = rpn.evaluate("3\n4 5")
        self.assertEqual(result, "3\n45")

    def test_get_math_operation_when_operator_is_given_between_two_numbers(self):
        rpn = RPNEvaluator()
        result = rpn.evaluate("20 5 /")
        self.assertEqual(result, "4")


if __name__ == '__main__':
    unittest.main()
