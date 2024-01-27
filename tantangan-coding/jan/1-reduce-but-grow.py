import functools

def grow(arr):
    
    return functools.reduce(lambda a,b: a * b, arr)