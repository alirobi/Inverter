import unittest

import inv

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = inv.calculate("1 1 +")
        self.assertEqual(2, result)

class TestBasics(unittest.TestCase):
    def test_mean(self):
        result = inv.calculate("2 -")
        self.assertEqual(2, result)