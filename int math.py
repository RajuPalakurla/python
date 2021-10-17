#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Integer_Math' function below.
#
# The function accepts following parameters:
#  1. INTEGER Side
#  2. INTEGER Radius
#

def Integer_Math(Side, Radius):
    # Write your code here
    print("Area of Square is {}".format(Side*Side))
    print("Volume of Cube is {}".format(Side*Side*Side))
    value = (3.14*Radius*Radius) * 1000
    value = round(value/1000,2)
    print("Area of Circle is {}".format(value))
    value = ((4/3)*3.14*Radius**3) * 1000
    value = round(value/1000,2)
    print("Volume of Sphere is {}".format(value))
    

if __name__ == '__main__':