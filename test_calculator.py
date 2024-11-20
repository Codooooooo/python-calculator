import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_positive(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -1), -2)


    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(1, 5), -4)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        
    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        
    def test_divide_not_divisible(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    
    def test_modulo_normal(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        
    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
if __name__ == '__main__':
    unittest.main()