# Reduce function is used to reduce number of entries in a single 


from functools import reduce
rain_water = [10, 20, 30, 40, 5]

def collector(bucket,water):
    print(bucket,water)
    return bucket + water

print(reduce(collector, rain_water,0))