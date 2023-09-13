cool = ['blue', 'green', 'yellow']
chill = cool[:]
chill.append('black')
# We can do this to copy every element of the list
# So that both are pointing to the different memory locations

print(cool)
print(chill)