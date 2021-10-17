import itertools
import operator

def tupleparse(tupleObj):
    mainlist=[]
    sublist=[]
    subtuple=tupleObj[0]
    result=itertools.cycle(subtuple)
    count=1
    for val in result:
        sublist.append(val)
        if count == 4:
            break
        count+=1
    mainlist.append(tuple(sublist))
    subtuple=tupleObj[1]
    sublist=[]
    result=list(itertools.repeat(subtuple,4))
    for val in result:
 #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'usingiter' function below.
#
# The function is expected to return a TUPLE.
# The function accepts following parameters:
#  1. TUPLE tupb
#
import itertools
import operator

def performIterator(tupleObj):
    # Write your code here
    mainlist=[]
    sublist=[]
    subtuple=tupleObj[0]
    result=itertools.cycle(subtuple)
    count=1
    for val in result:
        sublist.append(val)
        if count == 4:
            break
        count+=1
    mainlist.append(tuple(sublist))
    subtuple=tupleObj[1]
    sublist=[]
    result=list(itertools.repeat(subtuple,len(subtuple)))
    for val in result:
        sublist.append(val[0])
    mainlist.append(tuple(sublist))
    subtuple=tupleObj[2]
    sublist=[]
    result=list(itertools.accumulate(subtuple,operator.add))
    for val in result:
        sublist.append(val)
    mainlist.append(tuple(sublist))
    subtuple=tupleObj[3]
    sublist=[]
    result=list(itertools.chain(tupleObj))
    for val in result:
        for cval in val:
            sublist.append(cval)
    sublist=itertools.chain(sublist)
    mainlist.append(tuple(sublist))
    filterlist=mainlist[3]
    sublist1=itertools.filterfalse(lambda x: x%2==0,filterlist)
    mainlist.append(tuple(sublist1))
    return tuple(mainlist)

if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
   
if __name__ == "__main__":
    tuplerec=((1,10,5,2),(8,48,14,63),(59,47,49,22),(19,60,1,40))
    tupleparse(tuplerec)