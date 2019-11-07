import unittest

import inv

# class TestBasics(unittest.TestCase):
#     def test_add(self):
#         result = inv.calculate("1 1 +")
#         self.assertEqual(2, result)

class TestBasics(unittest.TestCase):
    def test_log(self):
        result = inv.calculate("10 +")
        self.assertEqual(1, result)