def main():
    """Counts the occurences of a given number in an array."""

    arr = [3, 2, 1, 2, 3, 1, 1, 1, 1, 3]
    arrcount = [0, 0, 0]

    for i in range(len(arr)):
        for j in range(len(arrcount)):
            if arr[i] == j + 1:
                arrcount[j] += 1

    print(arrcount)

if __name__ == "__main__":
    main()