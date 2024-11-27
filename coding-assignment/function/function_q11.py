 
# How do you define a function inside another function?

def outer_function():
    def inner_function():
        return "Inner Function"
    return inner_function()
print(outer_function())
