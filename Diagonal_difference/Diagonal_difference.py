import sys
import math

def main():
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)

    left_diag = 0
    right_diag = 0
    counter = 0
    for row in a:
        left_diag += row[counter]
        right_diag += row[n-1-counter]
        counter+=1

    return int(math.fabs(left_diag - right_diag))

main()
