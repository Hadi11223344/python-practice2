# args and kwargs
# we use it when we want to pass variable number of arguements
# kwargs is used to pass variable arguments

def adder(*args,**kwargs):
    print(args) # it will be printed as tuple
    print(kwargs) # it will be printed as dictionary
    total = 0
    for i in kwargs.values():
        total += i
    return sum(args)+total

print(adder(1, 2, price = 10 , tax = 2))