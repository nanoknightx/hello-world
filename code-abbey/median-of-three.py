def main():
    """Finds the median among three numbers."""

    lst = [300, 550, 137]

    if lst[0] < lst[1] < lst[2] or lst[2] < lst[1] < lst[0]:
        print(lst[1])
    elif lst[1] < lst[0] < lst[2] or lst[2] < lst[0] < lst[1]:
        print(lst[0])
    elif lst[0] < lst[2] < lst[1] or lst[1] < lst[2] < lst[0]:
        print(lst[2])

if __name__ == "__main__":
    main()