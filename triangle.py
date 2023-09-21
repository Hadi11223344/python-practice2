canvas = 20
space = 10
space2 = 1

print("."+" "*9 + " X")
for i in range(10):
    print(" "*(space-i) +"X"+ "  "*(space2+i)+"X")

print("X"*24)