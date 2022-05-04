def main():
    """Counts vowels in a given string."""

    str = "o a kak ushakov lil vo kashu kakao"
    sum = 0

    vowels = ('a', 'o', 'u', 'i', 'e', 'y')

    for i in range(len(str)):
        if str[i] in vowels:
            sum += 1

    print(sum)

if __name__ == "__main__":
    main()