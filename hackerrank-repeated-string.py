#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    result = 0
    for i in s:
        if i == 'a':
            result += 1

    repetitions = n // len(s)
    result = result * repetitions
    # cantidad de letras q me faltan
    modulo = n % len(s)

    for x in range(0, modulo):
        if s[x] == 'a':
            result += 1
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    # fptr.write(str(result) + '\n')

    # fptr.close()

# input:
# aba
# 10
# output
# 7
