import unittest
from Karmand import Karmand

class TestKarmand(unittest.TestCase):
    
    def setUp(self):
        print('Start..')
        self.emp_1 = Karmand('AmirHosein', 'Deist', 21)
        self.emp_2 = Karmand('Mahmoud', 'Davoudi', 20)

    def tearDown(self):
        print('Over..')

    def test_email(self):
        print('testing email...')

        self.assertEqual(self.emp_1.email, 'AmirHosein.Deist@gmail.com')
        self.assertEqual(self.emp_2.email, 'Mahmoud.Davoudi@gmail.com')

        self.emp_1.first = 'Ali'
        self.emp_2.first = 'Sara'

        self.assertEqual(self.emp_1.email, 'Ali.Deist@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sara.Davoudi@gmail.com')

    def test_FullName(self):
        print('testing FullName...')

        self.assertEqual(self.emp_1.FullName, 'AmirHosein.Deist')
        self.assertEqual(self.emp_2.FullName, 'Mahmoud.Davoudi')

        self.emp_1.first = 'Ali'
        self.emp_2.first = 'Sara'

        self.assertEqual(self.emp_1.FullName, 'Ali.Deist')
        self.assertEqual(self.emp_2.FullName, 'Sara.Davoudi')

    def apply_raise(self):
        print('testing apply_raise...')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 210)
        self.assertEqual(self.emp_2.pay, 420)

if __name__ == '__main__':
    unittest.main()
