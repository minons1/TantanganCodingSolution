
from typing import List
class Solution:
    def reverse(self, x: int) -> int:
      max_signed_int = [i for i in str(2**31 - 1)]
      min_signed_int = [i for i in str(-(2**31))]

      digits = [i for i in str(x)[-1::-1]]

      if x & 2**31 -1 != x:
        #negative, swap sign
        digits.insert(0, digits[-1])
        digits.pop()

        if len(digits) == len(min_signed_int):
          for i in range(1, len(digits)):
            if int(digits[i]) < int(min_signed_int[i]):
              return -1 * self.construct(digits[1:])
            elif int(digits[i]) == int(min_signed_int[i]):
              continue
            else:
              return 0
        else:
          return -1 * self.construct(digits[1:])
      else:
        if len(digits) == len(max_signed_int):
          for i in range(len(digits)):
            if int(digits[i]) < int(max_signed_int[i]):
              return self.construct(digits)
            elif int(digits[i]) == int(max_signed_int[i]):
              continue
            else:
              return 0
        else:
          return self.construct(digits)

    def construct(self, nums: List[str]) -> int:
        num = 0
        for i in nums:
          num = num * 10 + int(i)
        
        return num

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(0))
print(sol.reverse(120))

