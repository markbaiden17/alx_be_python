import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)

        self.assertEqual(self.calc.add(-5,-3), -8)
        self.assertEqual(self.calc.add(-10, 10), 0)

        self.assertEqual(self.calc.add(7, 0), 7)
        self.assertEqual(self.calc.add(0, -7), -7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(4, 10), -6)

        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(-10, -5), -5)

        self.assertEqual(self.calc.subtract(15, 0), 15)
        self.assertEqual(self.calc.subtract(0, 15), -15)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)

        self.assertEqual(self.calc.multiply(5, -4), -20)
        self.assertEqual(self.calc.multiply(-5, -4), 20)

        self.assertEqual(self.calc.multiply(1000, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        
        self.assertEqual(self.calc.divide(10, 4), 2.5)

        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()