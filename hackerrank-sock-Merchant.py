
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    dicc = {}
    for i in range(0, n):
        dicc[ar[i]] = dicc.get(ar[i], 0) + 1
    count = 0
    for j, v in dicc.items():
        count += (v/2)
    return count


if __name__ == '__main__':

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    print(result)

# input:
# 10
# 1 1 3 1 2 1 3 3 3 3
