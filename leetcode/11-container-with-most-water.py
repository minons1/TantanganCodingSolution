from typing import List, Dict
import math

# Original Solution
class Solution:
  def maxArea(self, height: List[int]) -> int:
    # optimization solution, we can use naive solution but account for possibility current index can reach max_water, else skip
    max_water = 0
    height_len = len(height)
    
    
    for idxh1, h1 in enumerate(height):
      
      if h1 * ((height_len - 1) - idxh1) <= max_water:
        continue
      
      min_idxh2 = idxh1 + math.ceil(max_water / h1)
      # start from min idxh2, because number below it didn't possible to beat max_water
      for j in range(min_idxh2, height_len):
        idxh2 = j
        h2 = height[j]

        max_water = max(min(h1, h2) * (idxh2 - idxh1), max_water)
    return max_water

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))
print(Solution().maxArea([0,0]))