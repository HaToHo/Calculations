__author__ = 'hans'
#Filename: test_fibonacci.py
import unittest
from Arithmetic.Advanced.fibonacci import fibonacci


class fibonacciTest(unittest.TestCase):

    def testMethod(self):
        """
        Test av fibonacci
        """
        self.assertEqual(int(fibonacci(10)), 55, "fibonacci(10) = 55")


if __name__ == '__main__':
    unittest.main()