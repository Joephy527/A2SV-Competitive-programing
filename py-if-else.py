#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    weird = set()
    for i in range(6, 21):
        weird.add(i)

    if n % 2 == 0 and n not in weird:
        print("Not Weird")
    else:
        print("Weird")
