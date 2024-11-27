# Finding the most frequent character in a string
from collections import Counter
my_string = "aabbbcccc"
counter = Counter(my_string)
most_frequent = counter.most_common(1)
print(most_frequent[0][0]) 
