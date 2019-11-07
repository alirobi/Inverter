import unittest

import inv

# class TestBasics(unittest.TestCase):
#     def test_add(self):
#         result = inv.calculate("1 1 +")
#         self.assertEqual(2, result)

class TestBasics(unittest.TestCase):
    def test_log(self):
        result = inv.calculate("8 3 +")
        self.assertEqual(2, result)