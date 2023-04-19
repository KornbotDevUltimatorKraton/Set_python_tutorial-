# Define the same set as two different variables
set1 = {1, 2, 3}
set2 = {2, 3, 4, 5}

# Find the union using union() method
union = set1.union(set2)
print(union)  # Output: {1, 2, 3, 4, 5}

# Find the union using | operator
union = set1 | set2
print(union)  # Output: {1, 2, 3, 4, 5}
