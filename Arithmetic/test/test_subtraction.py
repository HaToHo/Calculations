__author__ = 'hans'
#Filename: test_subtraction.py
import unittest
from Arithmetic.subtraction import subInt


class fibonacciTest(unittest.TestCase):

    def testSubInt(self):
        """
        Test av subInt
        """
        self.assertEqual(subInt(2, "34"), -32, "addInt(2, \"34\") = -2 ")

        self.assertEqual(subInt(2, "qwerty"), 2, "addInt(2, \"qwerty\") = 2 ")

if __name__ == '__main__':
    unittest.main()