import unittest

def add(a, b):
    return a + b
class TestAddFunction(unittest.TestCase):
    def testAddNumbers(self):
        self.assertEqual(add(3,4),9)
if __name__=='__main__':
    unittest.main()
"""

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 10)

if __name__ == '__main__':
    unittest.main()
"""