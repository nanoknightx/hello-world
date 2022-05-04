def main():
    """Calculates the weighted sum of digits in a number."""

    number = 1776
    sum = 0

    for i in range(len(str(number))):

        current = number % 10
        sum += current * (len(str(number)))
        number //= 10

    print(sum)

if __name__ == "__main__":
    main()