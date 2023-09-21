number = [0, 1, 2, 3, 4, 5 , 1 , 1 ,1 ,9 ,9 ,9 ,2,3]

# count method is used to count the number of occurences of a value in a list

# print(number.count(1))

# we can also use the index method to find the index of a value in a list

# print(number.index(1))
# we can also provide it range to check between
# print(number.index(1,1,3))
# check for 1 , from index 2 to index 3

# new_number = number.sort()
# So sort method modifies the actual list and returns NONE

# print(new_number)
# print(number)
new_num = sorted(number)
# Unlike sort , sorted method returns a copy of the original list
print(number)
print(new_num)

