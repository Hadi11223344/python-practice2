# Dictionary is mutable data type
# The keys of dictionary can be changed but data type must be
# immutable like tuple, string

dictionary = {"player": "name", "power": "full", "age": 18}
# i can modify it but if key is mutable it will throw error

# following will throw error
# dict1 = {"player": "name", "power": "full", {}: 18}
# dict2 = {"player": "name", "power": "full", []: 18}


# HERE ARE SOME FUNCTIONS TO USED WITH DICTIONARIES

print(dictionary["player"])  # will print value of key
print(dictionary.keys()) # will
print(dictionary.get('power')) # will print values of key
print(dictionary.items()) 
print("player" in dictionary.keys()) # will return Boolean value
print(dictionary.popitem()) # it will remove the last item from the dictionary
# but in big dictionary it will randomly return