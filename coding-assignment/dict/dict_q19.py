 
#  How do you filter a dictionary to keep only keys greater than a certain value?

my_dict = {'a': 1, 'b': 2, 'c': 3}
filtered_dict = {k: v for k, v in my_dict.items() if v > 1}
print(filtered_dict)