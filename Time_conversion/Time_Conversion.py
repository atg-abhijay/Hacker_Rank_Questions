def timeConversion(s):
    # Complete this function
    morning_evening = s[-2]
    time = s[0:len(s)-2]
    time_list = list(map(int, time.split(":")))
    hours = time_list[0]
    if morning_evening == 'P':
        if hours != 12:
            hours += 12
    else:
        if hours == 12:
            hours = 0

    time_list[0] = hours
    for i in range(len(time_list)):
        # number occupies 2 spaces
        # put leading zeroes according
        # to empty spaces
        time_list[i] = format(time_list[i], '02d')

    return ':'.join(map(str, time_list))


def main():
    s = raw_input().strip()
    # example
    # s = "01:05:01PM"
    result = timeConversion(s)
    print(result)

main()
