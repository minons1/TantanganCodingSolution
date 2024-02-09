from functools import reduce
def a_plus_b(a, b):
    return a + b

def array_plus_array(arr1,arr2):
    return reduce(a_plus_b, arr1) + reduce(a_plus_b, arr2)

print(array_plus_array([1, 2, 3], [4, 5, 6]))
print(array_plus_array([-1, -2, -3], [-4, -5, -6]))
print(array_plus_array([0, 0, 0], [4, 5, 6]))
print(array_plus_array([100, 200, 300], [400, 500, 600]))