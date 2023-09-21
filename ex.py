# a qUick BroWn Fox juMps Over the laZy Dog

string = "a qUick BroWn Fox juMps Over the laZy Dog"

def small_letter(str):
    count = 0
    for i in range(len(string)):
        if string[i].islower():
            count += 1
    return count    
    
def big_letter(str):
    count = 0
    for i in range(len(string)):
        if string[i].isupper():
            count += 1
    return count    

print("The small letters are: ",small_letter(string))
print("The Capital letters are: ",big_letter(string))