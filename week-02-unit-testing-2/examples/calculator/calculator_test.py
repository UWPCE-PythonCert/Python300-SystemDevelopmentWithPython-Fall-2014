import unittest

import calculator_functions as calc

class TestCalculatorFunctions(unittest.TestCase):

    def setUp(self):
        self.x = 2

    def test_add(self):
        self.assertEqual(calc.add(self.x, 3), 5)
        

if __name__ == "__main__":
    unittest.main()
