 
#  How do you create a function that modifies a global variable?

x = 10
def modify_global():
    global x
    x += 5
modify_global()
print(x)
