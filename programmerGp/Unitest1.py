import unittest
import Unitest

class TestUnitest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Unitest.add(10, 5), 15)
        self.assertEqual(Unitest.add(1, -1), 0)
        self.assertEqual(Unitest.add(-1, -2), -3)
        self.assertEqual(Unitest.add(5, 5), 10)

    def test_multiply(self):
        self.assertEqual(Unitest.multiply(3, 5), 15)
        self.assertEqual(Unitest.multiply(10, 5), 50)
        self.assertEqual(Unitest.multiply(-1, -1), 1)

    def test_devide(self):
        self.assertEqual(Unitest.devide(50, 25), 2)
        self.assertEqual(Unitest.devide(725, 5), 145)
        self.assertRaises(ValueError, Unitest.devide, 8, 0)

        self.assertRaises(ValueError, Unitest.devide, 2, 0)

    def test_subtract(self):
        self.assertEqual(Unitest.subtract(10, 5), 5)
        self.assertEqual(Unitest.subtract(-1, 1), -2)

        

if __name__ == '__main__':
    unittest.main()