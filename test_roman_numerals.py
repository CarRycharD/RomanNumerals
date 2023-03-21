import unittest

from roman_numerals import RomanNumeralConverter


class TestRomanNumeral(unittest.TestCase):
    def setUp(self):
        # Create an instance of the RomanNumeral class to use in the tests
        self.roman_numeral_converter = RomanNumeralConverter()

    def test_roman_conversion(self):
        for number in range(1, 3999):
            roman = self.roman_numeral_converter.integer_to_roman(number)
            integer = self.roman_numeral_converter.roman_to_integer(roman)
            self.assertEqual(integer, number)

        self.assertRaises(ValueError, self.roman_numeral_converter.roman_to_integer, 'MMMM')
        self.assertRaises(ValueError, self.roman_numeral_converter.roman_to_integer, '')
        self.assertRaises(ValueError, self.roman_numeral_converter.roman_to_integer, 'CD1X')
        self.assertRaises(ValueError, self.roman_numeral_converter.roman_to_integer, 'XVX')


if __name__ == "__main__":
    unittest.main()
