import random
import time
import classes

def working(PlChar):
    """Asks for the number of hours that player wants to spend working, then rewards them with denars.
    They also lose energy every hour of work"""

    how_long = int(input("How many hours would you like to work? (You earn 5 denars per hour per level) >>> "))
    
    for i in range(how_long):
        time.sleep(1)
        PlChar.denars += 5 * PlChar.level
        PlChar.energy -= 1
        print("You work for 1 hour. You have", PlChar.denars, "denars. You have", PlChar.energy, "/ 100 energy left.")

def sleeping(PlChar):
    """Asks for the number of hours that player wants to spend sleeping,
    which regenerates energy lost through working"""

    how_long = int(input("How many hours would you like to sleep? >>> "))

    for i in range(how_long):
        if PlChar.energy < 100:
            PlChar.energy += 1
        time.sleep(1)
        print("You sleep for 1 hour. You have", PlChar.energy, "/ 100 energy.")

def fighting(PlChar):
    """Throws the player into a fight with generic enemy."""

    EnChar = classes.Enemy(PlChar.level)

    while PlChar.hp > 0 and EnChar.hp > 0:

        pc_damage = random.randrange(5, 10)
        enemy_damage = random.randrange(1, 3)
        EnChar.hp -= pc_damage
        PlChar.hp -= enemy_damage
        if EnChar.hp < 0:
            print("You have", PlChar.hp, "hp left. Enemy has 0 hp left.\n")
            break
        if PlChar.hp < 0:
            print("You lose. Quitting the game.")
            quit()
        print("You have", PlChar.hp, "hp left. Enemy has", EnChar.hp, "hp left.")
        time.sleep(1)


def healing(PlChar):
    """Asks for the number of hours that player wants to spend healing, which costs two denars for every hour."""

    how_long = int(input("How many hours would you like to heal (each hour costs 2 denars)? >>> "))

    for i in range(how_long):
        if PlChar.hp < PlChar.max_hp:
            if PlChar.denars > 2:
                PlChar.hp += 1
                PlChar.denars -= 2
            else:
                print("Not enough denars.")
                break
        time.sleep(1)
        print("You heal for 1 hour. You have", PlChar.hp, "hp. You have", PlChar.denars, "denars left.")

def status(PlChar):
    """Shows player status"""
    
    print("Denars: ", PlChar.denars, "\nEnergy: ", PlChar.energy, "/100 \nHit Point: ", PlChar.hp, "/100")
