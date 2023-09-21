# def small_all(alist):
#     sum = 0
#     for i in range(len(alist)):
#         sum += alist[i]
        
#     return sum

def cumulative_sum(alist):
    c_sum = 0
    for i in range(len(alist)):
        
       alist[i+1] += alist[i]
    print(alist[i])
    

num = [4 , 2 , 6 , 2 , 5 , 6 , 7 , 8 , 9 ]
# print(small_all(num))
print(cumulative_sum(num))