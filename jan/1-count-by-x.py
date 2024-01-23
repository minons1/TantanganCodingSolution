def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [x * (i +1) for i in range(n)]

print(count_by(1, 10))
print(count_by(2,5))