class Solution:
    def intToRoman(self, num: int) -> str:
        more_romans = [
            (1000, 'M'), 
            (900, 'CM'), 
            (500, 'D'), 
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),  
            (50, 'L'),  
            (40, 'XL'),
            (10, 'X'),   
            (9, 'IX'),  
            (5, 'V'),   
            (4, 'IV'),
            (1, 'I')
        ]
        roman = ''
        for key,value in more_romans:
            while num >= key:
                roman += value
                num -= key
        return roman


