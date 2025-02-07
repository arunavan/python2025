import unittest   #pip install unittest
import loan
loan.apply()
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

#print(add(4,5))
#print(sub(6,3))

#test class
class TestAddFunction(unittest.TestCase):  #super, parent
    def test_add(self): #test method /function
        self.assertEqual(add(3,4), 7)
        self.assertFalse(False)

    def test_sub(self): #test methods
        self.assertEqual(sub(9,5), 4)
        self.assertEqual(sub(-2,-6),4)

if __name__ == '__main__':
    unittest.main()

""""class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

"""

