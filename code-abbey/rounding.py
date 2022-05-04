def main():
    """Rounds a floating point number to the nearest integer."""

    lst1 = [12, 8]
    lst2 = [11, -3]
    lst3 = [400, 5]
    lst = [lst1, lst2, lst3]

    for i in range(3):
        number = lst[i][0] / lst[i][1]
        if number > 0:
            result = int(number + 0.5)
        else:
            result = int(number - 0.5)
        print(result)

if __name__ == "__main__":
    main()