import unittest
from fizzbuzz_ng import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    def test_num(self):  # 普通の数字を返す
        self.assertEqual(fizzbuzz(7), '7')
    def test_fizz(self):  # 3の倍数
        self.assertEqual(fizzbuzz(99), 'Fizz')
    def test_buzz(self):  # 5の倍数
        self.assertEqual(fizzbuzz(25), 'Buzz')
    def test_fizzbuzz(self):  # 15の倍数
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')
