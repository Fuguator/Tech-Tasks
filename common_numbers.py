import random

list1 = random.sample(range(1, 101), 10)
list2 = random.sample(range(1, 101), 10)

common_numbers = [num for num in list1 if num in list2]

print("List 1:", list1)
print("List 2:", list2)
print("Common numbers:", common_numbers)