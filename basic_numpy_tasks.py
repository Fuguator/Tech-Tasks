import numpy as np

# Exercise 1
arr1 = np.arange(1, 11)
first_five = arr1[:5]
last_three = arr1[-3:]
print("First five elements:", first_five)
print("Last three elements:", last_three)

# Exercise 2
arr2 = np.arange(1, 10).reshape(3, 3)
print("Original array:\n", arr2)
element = arr2[1, 2]
print("Element in second row, third column:", element)
arr2[1, 2] = 100
print("Modified array:\n", arr2)

# Exercise 3
zeros = np.zeros(10, dtype=int)
ones = np.ones(10, dtype=int)
result = zeros + ones
print("Element-wise addition of zeros and ones:", result)

# Exercise 4
arr4 = np.arange(1, 51).reshape(5, 10)
print("5x10 array:\n", arr4)
