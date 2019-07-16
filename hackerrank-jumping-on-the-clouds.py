#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c, n):
    jumps = 0
    x = 0
    while x < (n):
        if x+2 < len(c) and c[x+2] == 0:
            jumps += 1
            x += 2
        elif x+1 < len(c) and c[x+1] == 0:
            jumps += 1
            x += 1
        else:
            break
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()

# input:
# 7
# 0 0 1 0 0 1 0

# output:
# 4
