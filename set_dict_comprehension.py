# this is quite similar to list comprehension

set_one = {i for i in range(10)}
print(set_one)


# now dict comprehension

dic = {
    "x":1,
    "y":2,
    "z":3
}

my_dict_comp = {key:value**2 for key,value in dic.items()}

print(my_dict_comp)