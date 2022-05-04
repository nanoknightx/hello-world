def main():
    """Converts degrees Fahrenheit to Celsius."""

    fahrenheit = 69
    result = (fahrenheit - 32) * (5 / 9)

    if result > 0:
        result = int(result + 0.5)
    else:
        result = int(result - 0.5)

    print(fahrenheit, "degrees Fahrenheit is", result, "degrees Celsius.")

if __name__ == "__main__":
    main()