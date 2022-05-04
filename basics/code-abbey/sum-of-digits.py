def main():
    """Sums the digits of a given number."""

    number = 1234
    sum = 0

    for i in range(len(str(number))):

        current = number % 10
        sum += current
        number //= 10

    print(sum)

if __name__ == "__main__":
    main()