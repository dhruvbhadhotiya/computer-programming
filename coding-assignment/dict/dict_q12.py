 
#  How can you sort a dictionary by its values?

my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
