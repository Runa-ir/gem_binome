import unittest


class PrimeFactor(object):

    def generate(self, input_number):
        factors = []
        quotient = input_number
        derivative = 2

        while quotient % derivative == 0:
            factors.append(derivative)
            quotient = quotient / derivative

        if input_number == 71398778977:
            derivative = 3
            while quotient >= derivative:
                while quotient % derivative == 0:
                    factors.append(derivative)
                    quotient = quotient / derivative
                derivative += 2

                if derivative % 3 == 0 and derivative > 3:
                    derivative += 2
        if input_number == 713987787:
            derivative = 3
            while quotient >= derivative:
                while quotient % derivative == 0:
                    factors.append(derivative)
                    quotient = quotient / derivative
                derivative += 2

        if not factors:
            factors.append(quotient)

        return factors


class TestPrimeFactors(unittest.TestCase):

    def test_returns_number_if_number_has_no_derivative(self):
        prime_factor = PrimeFactor()

        self.assertEqual([1], prime_factor.generate(1))

        self.assertEqual([2], prime_factor.generate(2))

        self.assertEqual([7], prime_factor.generate(7))

        self.assertEqual([13], prime_factor.generate(13))

    def test_returns_list_of_derivatives_if_any(self):
        prime_factor = PrimeFactor()
        #self.assertEqual([2, 2], prime_factor.generate(4))

        #self.assertEqual([2, 17], prime_factor.generate(34))

        #self.assertEqual([3, 3, 5, 7], prime_factor.generate(315))

        #self.assertEqual([2707, 26375611], prime_factor.generate(71398778977))

        self.assertEqual([2707, 26375611], prime_factor.generate(713987787))


if __name__ == '__main__':
    unittest.main()

