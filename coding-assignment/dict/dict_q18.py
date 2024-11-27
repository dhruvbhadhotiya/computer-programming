#  How do you reverse the keys and values in a dictionary? 


my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in my_dict.items()}
print(reversed_dict)
