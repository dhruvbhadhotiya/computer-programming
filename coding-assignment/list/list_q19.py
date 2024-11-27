 
# Find the Second Largest Element in a List

def second_largest(lst):
    unique = list(set(lst))  # Remove duplicates
    if len(unique) < 2:
        return None  # Not enough elements
    unique.sort()
    return unique[-2]

my_list = [10, 20, 4, 45, 99]
result = second_largest(my_list)
print(result)  # Output: 45
