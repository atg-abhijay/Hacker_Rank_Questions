def main():
    # enter a number 'n' as an argument
    # and the program will print a
    # 'staircase' of size n
    # example - staircase of size 5
    #     *
    #    **
    #   ***
    #  ****
    # ***** (no extra space before first *)
    n = int(raw_input().strip())
    arr = [" "] * n
    for i in range(n):
        # print(i)
        arr[n-1-i] = "*"
        print(str(''.join(arr)))

main()