import activities
import classes

def main():
    """Enters gameloop and lets the player decide what they want to do."""

    PC = classes.Player()

    while True:
        choice = input("What do you want to do: work, sleep, fight, heal, status? >>> ")
        if choice == 'work':
            activities.working(PC)
        elif choice == "sleep":
            activities.sleeping(PC)
        elif choice == "fight":
            activities.fighting(PC)
        elif choice == "heal":
            activities.healing(PC)
        elif choice == "status":
            activities.status(PC)

if __name__ == "__main__":
    main()