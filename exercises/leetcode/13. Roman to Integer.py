import os

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         numbers = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
#         result = 0
#         for i in s:
#             if i in list(numbers.keys):
#                 result += numbers.get(i)
#         return result
    
# solution = Solution()
# s = None
# while s != '0':
#     s = input()
#     print(solution.romanToInt(s))

class Solution:
   def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        
        for char in s:
            current_value = roman_values[char]
            # If the current value is greater than the previous one, subtract the previous value
            # since it's a case like IV or IX.
            if current_value > prev_value:
                result += current_value - 2 * prev_value
            else:
                result += current_value
            prev_value = current_value
        
        return result

solution = Solution()
s = None
while s != '0':
    s = input("Enter a Roman numeral (or '0' to exit): ")
    print(solution.romanToInt(s))
