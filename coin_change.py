# import math
# import os
# import random
# import re
# import sys

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
    c = sorted(c)
    R = [ [] ] * (n+1)
    for change in range(1,n+1):
        possibilities_per_change = []
        for coin in c:
            if coin == change:
                possibilities_per_change.append([coin])
            elif coin < change and len(R[change-coin]) > 0:
                prev_list = R[change-coin].copy()
                if len(prev_list) > 0:
                    for p in prev_list:
                        p_copy = p.copy()
                        p_copy.append(coin)
                        p_copy = sorted(p_copy)
                        if p_copy not in possibilities_per_change:
                            possibilities_per_change.append(p_copy)
        R[change] = possibilities_per_change
    print(R[change])
    return int(len(R[n]))

if __name__ == '__main__':

    first_multiple_input = '''
    10 4
    2 5 3 6
    '''
    n, m, *c = map(int,first_multiple_input.split())

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # first_multiple_input = input().rstrip().split()
    # n = int(first_multiple_input[0])
    # m = int(first_multiple_input[1])
    # c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    # X = [[1, 2], [2, 1]]
    # Y = [1]
    # Z = [x + Y for x in X]
    # subset_Z = [frozenset(z) for z in Z]
    # Z = set(subset_Z)
    # print('x: ', X)
    # print('y: ', Y)
    # print('z: ', Z)
    # print('set_z: ', subset_Z)
    # print('Z: ', list(Z))
    
    ways = getWays(n, c)
    # fptr.write(str(ways) + '\n')
    # fptr.close()
