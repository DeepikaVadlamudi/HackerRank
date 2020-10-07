#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum1 = sum(arr[i]for i in range(len(arr)-1))
    sum2 = sum(arr[i] for i in range(1,len(arr)))
    print(sum1,sum2)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
