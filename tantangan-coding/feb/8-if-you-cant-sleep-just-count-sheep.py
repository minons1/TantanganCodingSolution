def count_sheep(n):
    sheeps = ''
    for i in range(n):
      sheeps = sheeps + f'{str(i+1)} sheep...'
    return sheeps

print(count_sheep(0))
print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))
