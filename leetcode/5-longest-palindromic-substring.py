class Solution:
    def longestPalindrome(self, s: str) -> str:
      pal_res = ''
      for i, _ in enumerate(s):

        temp_pal = s[i]
        pal_1 = self.findPalindrome(temp_pal, s, i - 1, i + 1)
        pal_2 = self.findPalindrome('', s, i - 1, i)
        pal_3 = self.findPalindrome('', s, i, i + 1)

        temp_pal = max([pal_1, pal_2, pal_3], key=len)

        pal_res = temp_pal if len(temp_pal) > len(pal_res) else pal_res
      
      return pal_res

    def findPalindrome(self, temp_pal: str, s: str, left_pointer: int, right_pointer: int) -> str:

      if left_pointer < 0 or right_pointer == len(s):
          return temp_pal

      left_char = s[left_pointer]
      right_char = s[right_pointer]
      if left_char == right_char:
        return self.findPalindrome(left_char + temp_pal + right_char, s, left_pointer - 1, right_pointer + 1)
      else:
        return temp_pal
      

sol = Solution()
print(sol.longestPalindrome('babad'))
print(sol.longestPalindrome('cbbd'))
print(sol.longestPalindrome('ccc'))