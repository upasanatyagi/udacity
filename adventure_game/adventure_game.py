import time
import random
import sys


def print_pause(message):
    """This function print statements with a delay"""
    print(message)
    time.sleep(1)


def display_menu():
    """This function displays the menu options"""
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


def house(items):
    """This function groups the actions that happen in the house and
    requires `items` which is a list as input"""
    print_pause("You approach the front door")
    print_pause("The door opens and you hear someone sneaking closer")
    animals = ["dog", "cat", "tiger"]
    animal = random.choice(animals)
    print_pause(f'Suddenly you see an angry {animal} charging towards you')
    print_pause("You decide to fight or run")
    response = ""
    while response not in ["1", "2"]:
        response = input("(Options: 1 for fight and 2 for run.) ")

    if response == "1":
        animal_fight(animal, items)
        restart_game(items)
    elif response == "2":
        print_pause("You walk back to the field.")
        menu(items)


def field():
    """This function prints the introductory messages"""
    print_pause("You wake to find yourself in a grass field.")
    print_pause("On the corner is a house with a hidden cave entrance "
                "on its right side.")


def animal_fight(animal, items):
    """This function handles the fight sequence. The outcome is randomly
     chosen."""
    outcome = random.randint(0, 1)
    if outcome:
        print_pause(f'You put up a brave fight and killed {animal}')
        print_pause("Congratulations you've won")
        return "won"
    else:
        print_pause(f'{animal} hurt you. You cannot fight anymore')
        print_pause("You lost")
        return "lost"


def cave(items):
    print_pause("The cave is dark and smelly")
    if "sword" not in items:
        print_pause("Inside there is a sword on the far wall.")
        print_pause("You take the sword with you")
        items.append("sword")
    else:
        print_pause("You've been here before and have taken the sword.")

    print_pause("You walk back ot the field")
    menu(items)


def restart_game(items):
    print_pause("GAME OVER")
    response = input("Would you like to play again? (y/n)")
    if response.lower() == "y":
        menu(items)
    else:
        sys.exit(0)


def menu(items):
    response = ""
    while response not in ["1", "2"]:
        display_menu()
        response = input("(Please enter 1 or 2) ")
    if response == "1":
        house(items)
    elif response == "2":
        cave(items)


def play_game():
    items = []
    field()
    menu(items)


play_game()
