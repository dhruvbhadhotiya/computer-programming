 
# Find All Pairs in a List that Sum to a Given Number

def find_pairs(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

my_list = [1, 2, 3, 4, 5]
target = 6
result = find_pairs(my_list, target)
print(result)  
