import unittest
from fizzbuzz_ng import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_num(self):
        self.assertEqual(fizzbuzz(7), '7')
    def test_fizz(self):
        self.assertEqual(fizzbuzz(99), 'Fizz')
    def test_buzz(self):
        self.assertEqual(fizzbuzz(25), 'Buzz')
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')
