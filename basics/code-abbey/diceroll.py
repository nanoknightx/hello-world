import random

def main():
    """Generates a random dice roll."""

    dice = random.random()
    dice *= 6
    dice = int(dice + 1)

if __name__ == "__main__":
    main()