#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):
    # Write your code here
    count = 0
    def merge(arr):
        if len(arr) > 1:
            left_arr = arr[:len(arr) // 2]
            right_arr = arr[len(arr) // 2:]
            merge(left_arr)
            merge(right_arr)
            
            i = 0
            j = 0
            k = 0
            nonlocal count
            
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                    count += 1
                    count += len(left_arr) - (i + 1)
                k += 1
            
                
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
                    
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
        return count
    return merge(arr)
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
