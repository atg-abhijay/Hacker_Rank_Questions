import math

def main():
    arr = [23, 13, 64, 34, 67]
    sums = [sum(arr)] *  len(arr)
    for x in range(len(arr)):
        sums[x] -= arr[x]

    print min(sums), max(sums)


# let array be -    a0      a1      a2      a3      a4
# let sums be -  (a3+ a4) (a4+a0) (a0+a1) (a1+a2) (a2+a3)
def own_question():
    arr = [1,2,3,4,5]
    sums = [sum(arr)] * len(arr)
    for x in range(len(arr)):
        first_indice = (x+3)%len(arr)
        second_indice = (x+4)%len(arr)
        sums[x] = arr[first_indice] + arr[second_indice]

    print(sums)

# main()
own_question()
