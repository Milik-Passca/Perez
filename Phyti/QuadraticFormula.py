# Import complex math module
#To calcualte Quadratic equation 

import math 

a= int(input("please input the enter the a value:"))
b= int(input("please input the enter the b value:"))
c=int(input("please input the enter the c value:"))

root1= ((-1* b) - math.sqrt((math.pow(b, 2)- 4.0*a*c)))/(2*a)
root2= ((-1* b) + math.sqrt((math.pow(b, 2)- 4.0*a*c)))/(2*a)

print ("Root1:"), root1
print ("Root2:"), root2