def main():
    """Calculates a checksum of provided array."""

    arr = [3, 1, 4, 1, 5, 9]
    result = 0

    for i in range(len(arr)):
        result += arr[i]
        result *= 113
        result %= 10000007

    print(result)

if __name__ == "__main__":
    main()