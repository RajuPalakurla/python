#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'tria' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. FLOAT n1
#  2. FLOAT n2
#  3. INTEGER n3
#
import math

def triangle(n1, n2, n3):
    # Write your code here
    firstvalue=(n1*n2)/2
    pivalue=round(math.pi,n3)
    print("({}, {})".format(firstvalue,pivalue))

if __name__ == '__main__':