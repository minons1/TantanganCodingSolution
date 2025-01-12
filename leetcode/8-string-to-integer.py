class Solution:
  def myAtoi(self, s: str) -> int:
# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
    left = -2**31
    right = 2**31 -1
    
    num = 0
    is_signed = False
    is_negative = False
    still_trailing_zero = True
    digit_found = False
    
    for i in s:
      if digit_found == False:
        if (i == '-' or i == '+' or i == ' ') and is_signed == True:
          break
        elif i == ' ':
          continue
        elif i == '-' :
          is_signed = True
          is_negative = True
          continue
        elif i == '+':
          is_signed = True
          continue
        elif i.isdigit() == False:
          break
        
        digit_found = True

      if i.isdigit() == False:
        break
      
      if i == '0' and still_trailing_zero:
        continue
      still_trailing_zero = False

      num = num * 10 + int(i)
      
      if is_negative:
        if -1 * num <= left:
          num = 2**31
          break
      else:
        if num >= right:
          num = 2**31 - 1
          break

    if is_negative:
      return -num
    else:
      return num


print(Solution().myAtoi('42'))
print(Solution().myAtoi('   -042'))
print(Solution().myAtoi('1337c0d3'))
print(Solution().myAtoi('0-1'))
print(Solution().myAtoi('words and 987'))
print(Solution().myAtoi('+-12'))
print(Solution().myAtoi('  + 431'))