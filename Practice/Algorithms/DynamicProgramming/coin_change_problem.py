#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    M = [[0 for i in range (n+1)] for j in range(len(c)+1)]
    c = sorted(c)
    for i in range(len(c)+1):
        M[i][0] = 1
    for j in range(1,n+1):
        M[0][j] = 0
    for i in range(1,(len(c)+1)):
        for j in range(1,n+1):
            if j < c[i-1]:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = M[i-1][j] + M[i][j-c[i-1]]
    return M[len(c)][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
