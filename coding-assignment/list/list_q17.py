 
#  Rotate a List by k Positions

def rotate_list(lst, k):
    k %= len(lst)  
    return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4, 5]
k = 2
rotated = rotate_list(my_list, k)
print(rotated) 