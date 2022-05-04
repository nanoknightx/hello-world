def main():
    """Calculates Body Mass Index of a person with given weight and height."""

    weight = 49
    height = 1.91
    bmi = weight / height**2

    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    else:
        print("Obese")

if __name__ == "__main__":
    main()