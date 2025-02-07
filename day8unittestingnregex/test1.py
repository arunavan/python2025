import unittest

def add(a, b):
    return a + b
#print(add(5,6))

class TestAddFunction(unittest.TestCase):
    def testAddNumbers(self):
        self.assertEqual(add(3,4),7)
    def testAddNumbers(self):
        self.assertEqual(add(30,40),70)

if __name__=='__main__':
    unittest.main()
