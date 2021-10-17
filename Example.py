#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calen' function below.
#
# The function accepts TUPLE datetuple as parameter.
#
import datetime
import calendar
from collections import Counter,defaultdict
def get_most_common_days(year, month):
    days = []
    for daynum in range(29, 32):
        try:
            days.append(datetime.date(year, month, daynum).strftime('%A'))
        except ValueError:
            break
    return days

def usingcalendar(datetuple):
    # Write your code here
    month=datetuple[1]
    if calendar.isleap(datetuple[0]):
        month=2
    calObj=calendar.month(datetuple[0],month)
    print(calObj)
    listobj=[]
    ldate=list(datetuple)
    obj=calendar.Calendar()
    for day in obj.itermonthdates(ldate[0],month):
        listobj.append(day)
    rev=listobj[:-8:-1]
    rev.reverse()
    print(rev)      
    print(get_most_common_days(ldate[0],month)[0])

if __name__ == '__main__':
    qw1 = []

    for _ in range(3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
        
    tup=tuple(qw1)

    usingcalendar(tup)
