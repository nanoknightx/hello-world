def main():

    str = ("four score and seven years ago")
    newstr = ("")

    for i in range(len(str)):
        newstr += str[-i - 1]

    print(newstr)

if __name__ == "__main__":
    main()