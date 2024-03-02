import unittest
from temperature import Temperature


class TestTemperature(unittest.TestCase):
    def test_get_celsius(self):
        check = Temperature(27)
        self.assertEqual(check.get_celsius(), 27)

    def test_zero(self):
        check = Temperature(0)
        self.assertEqual(check.get_fahrenheit(), 32)

    def test_hundred(self):
        check = Temperature(100)
        self.assertEqual(check.get_fahrenheit(), 212)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            Temperature(True)
        with self.assertRaises(TypeError):    
            Temperature('100')

unittest.main()



