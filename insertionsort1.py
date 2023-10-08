#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    def print_arr(arr):
        for i in arr:
            print(i, end=" ")
        print()
        
    key = arr[-1]
    for i in range(n - 1, -1, -1):
        if i > 0 and key < arr[i - 1]:
            arr[i] = arr[i - 1]
            print_arr(arr)
        else:
            arr[i] = key
            print_arr(arr)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
