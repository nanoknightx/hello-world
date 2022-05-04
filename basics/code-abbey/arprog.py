def main():
    """Finds arithmetic progression of a given list."""

    lst = [2, 5, 8]
    sum = 0

    for i in range(len(lst)):
        sum += lst[i]

    print(sum)

if __name__ == "__main__":
    main()