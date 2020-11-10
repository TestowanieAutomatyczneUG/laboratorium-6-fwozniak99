import unittest
from zad2.src import Password

class ValidTest(unittest.TestCase):
    def setUp(self):
        self.temp = Password()

    def test_is_long_enough(self):
        self.assertEqual(self.temp.ValidPassword("abc"), False)

    def tearDown(self):
        self.temp = None