def minimum(arr):
    #your code here...
    min = None
    for num in arr:

      min = num if min is None or num < min else min
    
    return min

def maximum(arr):
    #...and here
  max = None
  for num in arr:
    max = num if max is None or num > max else max
  
  return max