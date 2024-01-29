def zero_fuel(distance_to_pump, mpg, fuel_left):
  #Happy Coding! ;)
    return distance_to_pump <= mpg * fuel_left

print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))