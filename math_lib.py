import math

radians = (90.0 / 360.0) * 2 * math.pi 
print (math.sin(radians))

def multadd(a , b , c):
    angle_test = (math.sin(math.pi/4)+ (math.cos(math.pi/4)/2))
    print('sin(pi/4) + cos(pi/4)/2) is: ',  angle_test)
    ceiling_test = (276/19) + 2*math.log(12,7)
    print("ceiling(276/19) + 2 log_7(12) is: ", ceiling_test)
    
multadd(1,2,3)


