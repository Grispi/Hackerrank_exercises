#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    slist = s.replace("U", "1 ").replace("D", "-1 ").split()
    # slist = [map(int, i) for i in slist] error
    newlist = []
    for i in slist:
        newlist.append(int(i))
    count = 0
    valleys = 0
    for x in range(0, n):
        if newlist[x]+count == -1 and count == 0:
            valleys += 1
            count += newlist[x]
        else:
            count += newlist[x]
    return valleys

    # level = 0
    # valleys = 0
    # for i in s:
    #     if i == 'U':
    #         level += 1
    #         if level == 0:
    #             valleys += 1
    #     else:
    #         level -= 1
    # return valleys


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()

# input:
# 8
# UDDDUUDU

# answer: 2
