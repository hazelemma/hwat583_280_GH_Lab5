import unittest

from 280lab5_1 import factorial

class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        num = 5
        result = factorial(num)
        
        self.assertEqual(result, 120)
