    print("Welcome {}.".format(Name))
    print("It is our pleasure inviting you.")
    print("Have a wonderful day.")

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'find' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num1
#  2. INTEGER num2
#  3. INTEGER num3
#

def find(num1, num2, num3):
    # Write your code here
    #print("{} {} {}".format(num1,num2,num3))
    if num1 < num2 and num2 >= num3:
        print("True",end=" ")
    else:
        print("False",end=" ")
    
    if num1 > num2 and num2 <= num3:
        print("True",end=" ")
    else:
        print("False",end=" ")
    
    if num3 == num1 and num1 != num2:
        print("True",end=" ")
    else:
        print("False",end=" ")
    

if __name__ == '__main__':


########### tuple
results=[]
    pivalue=math.pi
    radius=c/(pivalue*2)
    area=round(pivalue*radius**2,2)
    radius=round(radius,2)
    results.append(radius)
    results.append(area)
    return tuple(results)


#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Float_fun' function below.
#
# The function accepts following parameters:
#  1. FLOAT f1
#  2. FLOAT f2
#  3. INTEGER Power
#

def Float_fun(f1, f2, Power):
    # Write your code here
    print("#Add")
    print(f1+f2)
    print("#Subtract")
    print(f1-f2)
    print("#Multiply")
    print(f1*f2)
    print("#Divide")
    print(f2/f1)
    print("#Remainder")
    print(f1%f2)
    powval=f1**Power
    print("#To_The_Power_Of")
    print(powval)
    print("#Round")
    print(round(powval,4))

if __name__ == '__main__':


    value=input("Enter a STRING:\n")
    print(value)
    print(type(value))



def triangle(n1, n2, n3):
    # Write your code here
    listvalue=[]
    area=round((n1*n2)/2,n3)
    listvalue.append(area)
    listvalue.append(round(math.pi,n3))
    return tuple(listvalue)



def docstring(functionname):
    # Write your code here
    help(functionname)