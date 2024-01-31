from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        is_even = total_len % 2 == 0


        last = second_from_last = None

        for i in range(math.floor(total_len / 2) + 1):
            num1 = nums1[0] if nums1 else None
            num2 = nums2[0] if nums2 else None

            second_from_last = last
            if num1 is not None and num2 is None:
                print('if')
                last = nums1.pop(0)
            elif num2 is not None and num1 is None:
                print('elif')
                last = nums2.pop(0)
            else:
                print('else')
                last = nums1.pop(0) if num1 <= num2 else nums2.pop(0)
        
        return (last + second_from_last) / 2 if is_even else last

sol = Solution()
# print(sol.findMedianSortedArrays([1,3], [0]))
# print(sol.findMedianSortedArrays([10], []))
# print(sol.findMedianSortedArrays([1,3], [2,4]))
print(sol.findMedianSortedArrays([0,0], [0,0]))