#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'encrdecr' function below.
#
# The function is expected to return a LIST.
# The function accepts following parameters:
#  1. STRING keyval
#  2. STRING textencr
#  3. Byte-code textdecr
#
from cryptography.fernet import Fernet

def encrdecr(keyval, textencr, textdecr):
    # Write your code here
    mainlist=[]
    f=Fernet(keyval)
    encrmsg=f.encrypt(textencr)
    mainlist.append(encrmsg)
    output = f.decrypt(textdecr)
    output_decoded = output.decode('utf-8')
    mainlist.append(output_decoded)
    return mainlist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    file = open('key.key', 'rb')
    key = file.read()  # The key will be type bytes
    file.close()
    
    keyval = key

    textencr = str(input()).encode()

    textdecr = str(input()).encode()


    result = encrdecr(keyval, textencr, textdecr)
    bk=[]
    f = Fernet(key)
    val = f.decrypt(result[0])
    bk.append(val.decode())
    bk.append(result[1])

    fptr.write(str(bk) + '\n')

    fptr.close()
