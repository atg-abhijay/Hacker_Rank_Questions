def birthdayCakeCandles(n, ar):
    # Complete this function
    tallest_candle = max(ar)
    num_tallest = 0
    for candle in ar:
        if candle == tallest_candle:
            num_tallest += 1

    return num_tallest

def main():
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    result = birthdayCakeCandles(n, ar)
    print(result)

main()
