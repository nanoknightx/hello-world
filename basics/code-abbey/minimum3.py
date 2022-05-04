def main():
    """Finds the lowest among three numbers."""

    n = 3
    lst1 = [4, 5, 7]
    lst2 = [50, 34, 43]
    lst3 = [76, 76, 76]
    lst = [lst1, lst2, lst3]

    for i in range(n):
        if lst[i][0] == lst[i][1] == lst[i][2]:
            print("They are equal")
        else:
            if lst[i][0] < lst[i][1]:
                if lst[i][0] < lst[i][2]:
                    print("First one")
                else:
                    print("Third one")
            else:
                if lst[i][1] > lst[i][2]:
                    print("Third one")
                else:
                    print("Second one")

if __name__ == "__main__":
    main()