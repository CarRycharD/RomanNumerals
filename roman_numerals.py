class RomanNumeralConverter:
    def __init__(self):
        # Create a dictionary to map Roman numerals to integers
        self.roman_to_int = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
 
    def integer_to_roman(self, number: int) -> str:
        # Convert an integer to a Roman numeral

        if number < 1 or number > 3999:
            raise ValueError('Input must be between 1 and 3999.')
        if not isinstance(number, int):
            raise TypeError('Input must be an integer.')
        
        roman_numeral = ""
        for symbol, value in self.roman_to_int.items():
            count = number // value
            roman_numeral += symbol * count
            number -= value * count
        return roman_numeral

    def roman_to_integer(self, roman: str) -> int:
        # Convert a Roman numeral to an integer

        if not roman:
            raise ValueError("Input must not be empty")
        if not all(symbol in self.roman_to_int for symbol in roman):
            raise ValueError("Invalid Roman numeral")
        
        total = 0
        last_value = 0
        for symbol in roman:
            value = self.roman_to_int[symbol]
            if value > last_value:
                total += value - 2 * last_value
            else:
                total += value
            last_value = value
        if self.integer_to_roman(total) != roman:
            raise ValueError("Invalid Roman numeral")
        return total

