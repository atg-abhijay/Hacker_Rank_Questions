import math

def main():
    arr = [23, 13, 64, 34, 67]
    sums = [sum(arr)] *  len(arr)
    for x in range(len(arr)):
        sums[x] -= arr[x]

    print min(sums), max(sums)

main()
