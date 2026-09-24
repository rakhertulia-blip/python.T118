def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0 or a == 0:
        return "делить на ноль нельзя"
    return a/b
print (add(5,5))
print (subtract(5,3))
print (multiply(5,3))
print (divide(0,9))
print (divide(7,0))

