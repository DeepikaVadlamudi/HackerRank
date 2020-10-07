#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal

# Complete the plusMinus function below.
def plusMinus(arr):
    negnum = 0
    posnum = 0
    zeronum=0
    n = len(arr)
    for i in arr:
        if i ==0:
            zeronum +=1
        if i>0:
            posnum+=1
        if i<0:
            negnum+=1
    print(round(Decimal(posnum/n),6))
    print(round(Decimal(negnum/n),6))
    print(round(Decimal(zeronum/n),6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
