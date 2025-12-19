import random
import math

numbers = [random.randint(1, 20) for _ in range(10)]
print("Original list:", numbers)

def cumulative_sum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

cum_list = cumulative_sum(numbers)
print("Cumulative sum list:", cum_list)

areas = [math.pi * r * r for r in cum_list if r % 3 == 0]

if areas:
    print("Areas of circles (radius divisible by 3):", areas)
else:
    print("radius not found")