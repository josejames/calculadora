import unittest

from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_suma_2_plus_2(self):
        cal = Calculator()
        self.assertEqual(4, cal.suma(2, 2))

    def test_suma_4_plus_2(self):
        cal = Calculator()
        self.assertEqual(6, cal.suma(4, 2))

    def test_suma_4_plus_4(self):
        cal = Calculator()
        self.assertEqual(8, cal.suma(4, 4))

    def test_suma_2_minus_2(self):
        cal = Calculator()
        self.assertEqual(0, cal.resta(2, 2))

    def test_suma_2_times_2(self):
        cal = Calculator()
        self.assertEqual(4, cal.multiplicacion(2, 2))

    def test_suma_2_div_2(self):
        cal = Calculator()
        self.assertEqual(1, cal.division(2, 2))

    def test_potencia_2_up_3(self):
        cal = Calculator()
        self.assertEqual(8, cal.pow(2, 3))

    def test_potencia_3_up_2(self):
        cal = Calculator()
        self.assertEqual(9, cal.pow(3, 2))


if __name__ == '__main__':
    unittest.main()
