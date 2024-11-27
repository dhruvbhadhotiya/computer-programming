 
# How do you use multiple return values from a function?

def calculate(a, b):
    return a + b, a * b
sum_result, product_result = calculate(3, 5)
print(sum_result, product_result)
