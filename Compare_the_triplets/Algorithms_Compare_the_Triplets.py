def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    comp_a = 0
    comp_b = 0
    a_data = [a0, a1, a2]
    b_data = [b0, b1, b2]
    paired_up = zip(a_data, b_data)
    paired_list = list(paired_up)
    for pair in paired_list:
        if pair[0] > pair[1]:
            comp_a += 1
        elif pair[0] < pair[1]:
            comp_b += 1
        else:
            # used to make an empty block
            pass

    result = [comp_a, comp_b]
    return result

def main():
    a0, a1, a2 = raw_input().strip().split(' ')
    a0, a1, a2 = [int(a0), int(a1), int(a2)]
    b0, b1, b2 = raw_input().strip().split(' ')
    b0, b1, b2 = [int(b0), int(b1), int(b2)]
    result = solve(a0, a1, a2, b0, b1, b2)
    print(" ".join(map(str, result)))

main()
