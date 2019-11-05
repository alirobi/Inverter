import unittest

import inv

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = inv.calculate("-1 ~")
        self.assertEqual(1, result)