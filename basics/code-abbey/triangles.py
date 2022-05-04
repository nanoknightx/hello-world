def main():
    """Checks whether a triangle can be build using provided side lengths."""

    lst = [1, 2, 4]

    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print("You can build this triangle")
    else:
        print("You can't build this triangle")

if __name__ == "__main__":
    main()