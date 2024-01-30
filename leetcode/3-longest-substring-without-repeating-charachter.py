class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        max_len = 0
        for char in s:
            if char not in substring:
                substring = substring + char
            else:
                substring = substring[substring.index(char) + 1:] + char
            cur_len = len(substring)
            max_len = cur_len if cur_len > max_len else max_len
        return max_len

sol = Solution()
print(sol.lengthOfLongestSubstring('salim'))
print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring('bbbbb'))
print(sol.lengthOfLongestSubstring('pwwkew'))
print(sol.lengthOfLongestSubstring('aabaab!bb'))