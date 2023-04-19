# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the intersection using intersection() method
intersection = set1.intersection(set2)
print(intersection)  # Output: {4, 5}

# Find the intersection using & operator
intersection = set1 & set2
print(intersection)  # Output: {4, 5}
