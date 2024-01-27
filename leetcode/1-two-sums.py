from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    number_map = {}
    for index, num in enumerate(nums):
        if num in number_map:
            number_map[num].append(index)
        else:
            number_map[num] = [index]
    
    for num in number_map:
        first_index = number_map[num].pop(0)

        second_num = target - num
        if second_num in number_map and len(number_map[second_num]) > 0:
            second_index = number_map[second_num].pop(0)
            return [first_index, second_index]
        
        number_map[num].append(first_index)

print(twoSum([2,3,4,5,6,6,7], 10))
print(twoSum([1,2,3,4,5,6,7], 13))