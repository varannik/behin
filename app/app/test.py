from django.test import TestCase
from app.calc import add 
from app.calc import sub

class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract_numbers(self):
        self.assertEqual(sub(5, 3), 2)
