
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 4)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()

    #py app1.py -v 

    """
    Outcomes Possible in Unit Testing
There are three types of possible test outcomes :

OK  This means that all the tests are passed.
FAIL  This means that the test did not pass and an AssertionError exception is raised.
ERROR  This means that the test raises an exception other than AssertionError.

    
    """