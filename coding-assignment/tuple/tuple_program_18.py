# P Nested tuple iteration
my_tuple = (1, (2, 3), (4, 5), 6)
for item in my_tuple:
    if isinstance(item, tuple):
        for sub_item in item:
            print(sub_item)
    else:
        print(item)
