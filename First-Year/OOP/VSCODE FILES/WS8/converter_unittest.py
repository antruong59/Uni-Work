import unittest
from converter import fahrenheit

class TestCelsius(unittest.TestCase):
    def test_temperature(self):
        self.assertEqual(fahrenheit(27),27*(9/5)+32)
        self.assertEqual(fahrenheit(0),32)
        self.assertEqual(fahrenheit(-4),(-4)*(9/5)+32)
        self.assertRaises(TypeError, fahrenheit, True)
        self.assertRaises(TypeError, fahrenheit, "34")

unittest.main()