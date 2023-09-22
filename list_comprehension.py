# List comprehensions: Case-1

# li_one = []
# for i in range(10):
#     li_one.append(i)
    
# print(li_one)


# now we can convert this into one line
li_one = [i for i in range(10)]
print(li_one)

# List comprehensions: Case-2


li_two = [i**2 for i in range(10)]
print(li_two)

# List comprehensions: Case-3
# li_three = []
# for i in range(10):
#     if i % 2 == 0:
#         li_three.append(i**2)
        
# print(li_three)


li_three = [i**2 for i in range(10) if i % 2 == 0]
print(li_three)


# def even(num):
#     return num % 2 == 0

# print(list(filter(even, li_two)))
    
