 
# find the single element in a list that appears only once, while all other elements appear exactly twice.

def find_non_duplicate(arr):
    result = 0
    for num in arr:
        result ^= num  
    return result

n = int(input())  
arr = list(map(int, input().split())) 
print(find_non_duplicate(arr))
