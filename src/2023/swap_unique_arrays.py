#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMaximumDistinctCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#  3. INTEGER k
#

def getMaximumDistinctCount(a, b, k):
    # Write your code here
    unique_history_a = {}
    duplicate_index_a = {}
    n = len(a)
    for i, item in enumerate(a):
        if item not in unique_history_a:
            unique_history_a[item] = i
        else:
            duplicate_index_a[i] = item
    print("unique", unique_history_a)
    print("dupe", duplicate_index_a)
    count = 0  # swapped count
    print("original", a, b)
    for i, item in enumerate(b):

        if item not in list(unique_history_a.keys()):
            if k == 0:
                break

            # swap
            # check for k
            print(i, item)
            dup_index = list(duplicate_index_a.keys())[count]
            print(dup_index)
            temp = a[dup_index]
            a[dup_index] = item
            b[i] = temp
            print(a, b)

            unique_history_a[item] = dup_index
            duplicate_index_a.pop(dup_index)
            count += 1
            k = -1
    print(unique_history_a, duplicate_index_a)
    return len(unique_history_a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    k = int(input().strip())

    result = getMaximumDistinctCount(a, b, k)

    fptr.write(str(result) + '\n')

    fptr.close()