#  how can you create a dictonary 

# Method 1
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)

#  Method 2

my_dict = dict(a=1, b=2, c=3)
print(my_dict)

#  Method 3

keys = ['a', 'b', 'c']
my_dict = dict.fromkeys(keys, 0)
print(my_dict)
