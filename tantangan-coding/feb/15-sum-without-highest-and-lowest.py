def sum_array(arr):
    if not arr:
        return 0
    temp_sum = 0
    cur_highest = None
    cur_lowest = None
    for idx, el in enumerate(arr):
        if idx == 0:
            cur_highest = el
            cur_lowest = el
            continue
        
        temp_val = el
        if el > cur_highest:
            temp_val = cur_highest
            cur_highest = el
        
        if el < cur_lowest:
            temp_val = cur_lowest
            cur_lowest = el

        if idx == 1:
            continue
        
        temp_sum += temp_val
    return temp_sum

print(sum_array(None))
print(sum_array([]))

print(sum_array([3]))
print(sum_array([ 3, 5]))
print(sum_array([6, 2, 1, 8, 10]))

print(sum_array([1,1,1,1,1,1,1,1]))