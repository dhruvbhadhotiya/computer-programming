 
#  How can you create a dictionary with default values for a list of keys?

keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)
print(default_dict)
