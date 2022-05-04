def main():
    """Finds the lower of two numbers."""

    n = 3
    lst1 = [4, 5]
    lst2 = [50, 34]
    lst3 = [76, 76]
    lst = [lst1, lst2, lst3]

    for i in range(n):
        if lst[i][0] > lst[i][1]:
            print("First one is bigger")
        elif lst[i][0] < lst[i][1]:
            print("Second one is bigger")
        else:
            print("They are equal")
            

if __name__ == "__main__":
    main()