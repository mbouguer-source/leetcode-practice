class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
        roman = 0
        for current, next in zip(s, s[1:]):
            if roman_numerals[current] < roman_numerals[next]:
                roman -= roman_numerals[current]
            else:
                roman += roman_numerals[current] 
        roman += roman_numerals[s[-1]]
        return roman
        