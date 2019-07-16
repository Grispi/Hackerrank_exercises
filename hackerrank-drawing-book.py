#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
# n = 6 p 2


def pageCount(n, p):
    if n == p:
        count = 0
        return (count)
    else:
        page = 1
        count_a = 0
        while page < p:
            page += 2
            count_a += 1
        if n % 2 == 0:
            page_r = n
        else:
            page_r = n-1
        count_r = 0
        while page_r > p:
            page_r -= 2
            count_r += 1
        return(min(count_a, count_r))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    pageCount(n, p)

    # fptr.write(str(result) + '\n')

    # fptr.close()

"""
Sample Input 0

6
2
Sample Output 0

1
Explanation 0

If Brie starts turning from page , she only needs to turn  page:

Untitled Diagram(6).png

If Brie starts turning from page , she needs to turn  pages:
"""
