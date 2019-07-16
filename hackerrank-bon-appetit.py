
import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    total = 0
    for i in bill:
        total += i
    total = (total - bill[k])/2
    if total == b:
        print('Bon Appetit')
    else:
        overcharged = round(b - total)
        print(overcharged)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

"""
Sample Input 0

4 1
3 10 2 9
12
Sample Output 0

5
Explanation 0 
Anna didn't eat item , but she shared the rest of the items with Brian. The total cost of the shared items is  and, split in half, the cost per person is . Brian charged her  for her portion of the bill. We print the amount Anna was overcharged, , on a new line.

Sample Input 1

4 1
3 10 2 9
7
Sample Output 1

Bon Appetit
Explanation 1 
Anna didn't eat item , but she shared the rest of the items with Brian. The total cost of the shared items is  and, split in half, the cost per person is . Because , we print Bon Appetit on a new line.
"""
