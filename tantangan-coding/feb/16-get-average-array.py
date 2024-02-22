def get_average(marks):
    sum = 0
    for i in marks:
        sum += i
    return sum // len(marks)

print(get_average([2, 2, 2, 2]))
print(get_average([1, 5, 87, 45, 8, 8]))
print(get_average([2,5,13,20,16,16,10]))
print(get_average([10, 10, 9]))