# # map func is used to deal with data and process at the same time
# # It maps a process individually to a entry


# li = [1, 2, 3]

# def adder_map(para_li):
#     return para_li + 1

# # print(list(map(adder_map, li)))
# # print(map.__doc__)

# # now simiilarly filter func has same functionality as map func but it is used to filter

# def odds(para):
#     return para%2 !=0

# # print(list(filter(odds, li)))
name = ["hammad", "john", "jane","alpha"]
def name_filter(name):
    if name != 'john':
        return name



print(list(filter(name_filter, name)))


# Now zip funtion
# It takes two iterables and returns a new iterable which is a zipped version

li_1 = [1, 2, 3]
li_2 = ["Hamamd", "John", "Jane"]
print(list(zip(li_1, li_2)))