# def square (x):
#     return x*x


# rv = square(5)
# print(rv)

# # we can reduce it to one line using lambda function

# rv1 = (lambda x: x*x )

# # print(rv1(5))

# # myadd = lambda a, b: a+b
# # mysub = lambda a, b: a-b
# # mymul = lambda a, b: a*b

# def mycalc(op, a, b):
#     return op(a,b)


# # rv1 = mycalc(myadd, 8, 2)
# # rv2 = mycalc(mysub, 8, 2)
# # rv3 = mycalc(mymul, 8, 2)

# # we can all above code into these three lines of code
# rv1 = mycalc(lambda a, b: a + b, 8, 2)
# rv2 = mycalc(lambda a, b: a - b, 8, 2)
# rv3 = mycalc(lambda a, b: a * b, 8, 2)
# print(rv1 , rv2 , rv3)
from functools import reduce

# numbers = [20, -20, 30, -4, -5]


# rv1 = (reduce(lambda a, b: a if a > b else b, numbers, 0))

# print(rv1)

mylist = [ 75 , 86 , 87 , 88 , 89 ]
map_object = map(lambda num: num%5, mylist)
remainders = list(map_object)

print("Original list: ", mylist)
print("List of remainders: ", remainders)
