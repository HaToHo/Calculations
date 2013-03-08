__author__ = 'hans'
#Filename: test_addition.py


import unittest
from Arithmetic.addition import addInt


class fibonacciTest(unittest.TestCase):

    def testAddInt(self):
        """
        Test av addInt
        """
        self.assertEqual(addInt(2, "34"), 36, "addInt(2, \"34\") = 36 ")

        self.assertEqual(addInt(2, "qwerty"), 2, "addInt(2, \"qwerty\") = 2 ")

if __name__ == '__main__':
    unittest.main()