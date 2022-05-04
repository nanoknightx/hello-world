def main():
    """Finds the lowest and biggest number in a list."""

    lst = [1, 23, 34, 23, 256, 0, 43, 657, 632, 197, 3]
    currentmax = lst[0]
    currentmin = currentmax

    for i in range(10):
        if lst[i] > currentmax:
            currentmax = lst[i]

    print(currentmax)

    for i in range(10):
        if lst[i] < currentmin:
            currentmin = lst[i]

    print(currentmin)

if __name__ == "__main__":
    main()