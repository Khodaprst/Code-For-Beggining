import unittest
import Unitest

class TestUnitest(unittest.TestCase):

    def test_add(self):
        result = Unitest.add(10, 5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()