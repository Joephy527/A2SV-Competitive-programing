#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    weird = set()
    for number in range(6, 21):
        weird.add(number)

    if n % 2 == 0 and n not in weird:
        print("Not Weird")
    else:
        print("Weird")
