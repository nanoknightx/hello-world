from tempfile import tempdir


def main():

    test = [1, 4, 3, 2, 6, 5]
    temp = 0

    for i in range(len(test) - 1):
        if test[i] > test[i+1]:
            temp = test[i+1]
            test[i+1] = test[i]
            test[i] = temp

    print(test)

if __name__ == "__main__":
    main()