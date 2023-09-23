# def square (x):
#     return x*x


# rv = square(5)
# print(rv)

# # we can reduce it to one line using lambda function

# rv1 = (lambda x: x*x )

# print(rv1(5))

# myadd = lambda a, b: a+b
# mysub = lambda a, b: a-b
# mymul = lambda a, b: a*b

def mycalc(op, a, b):
    return op(a,b)


# rv1 = mycalc(myadd, 8, 2)
# rv2 = mycalc(mysub, 8, 2)
# rv3 = mycalc(mymul, 8, 2)

# we can all above code into these three lines of code
rv1 = mycalc(lambda a, b: a + b, 8, 2)
rv2 = mycalc(lambda a, b: a - b, 8, 2)
rv3 = mycalc(lambda a, b: a * b, 8, 2)
print(rv1 , rv2 , rv3)