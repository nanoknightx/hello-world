def main():
    """Calculates the linear equation."""

    test = (1, 0, 0, 1)

    a = (test[3] - test [1]) / (test[2] - test[0])

    b = test[1] - (a *  test[0])                        # y = ax + b

    print(int(a), int(b))

if __name__ == "__main__":
    main()