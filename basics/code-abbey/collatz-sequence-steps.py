def main():
    """Calculates the number of steps for a Collatz Sequence of a given number."""
    
    counter = 0
    number = 97

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        counter += 1

    print(counter)

if __name__ == "__main__":
    main()