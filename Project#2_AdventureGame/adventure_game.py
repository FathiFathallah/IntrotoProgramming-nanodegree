import time
import random
PAUSE_TIME = 2


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(PAUSE_TIME)


def play_again():
    while True:
        print("Would you like to play again? (y/n)")
        action = input()
        if action == 'y':
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif action == 'n':
            print_pause("Thanks for playing! See you next time.")
            break


def fight(random_enemy, random_weapon):
    if random_weapon == "Sword of Ogoroth":
        print_pause("As the {} moves to attack, \
        you unsheath your new sword.".format(random_enemy))
        print_pause("The {} shines brightly in your\
        hand as you brace yourself for the attack.".format(random_weapon))
        print_pause("But the {} takes one look \
        at your shiny new toy and runs away!".format(random_enemy))
        print_pause("You have rid the town of the {}. \
        You are victorious!".format(random_enemy))
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your {} is no \
        match for the {}.".format(random_weapon, random_enemy))
        print_pause("You have been defeated!")
        play_again()


def field(random_enemy, random_weapon):
    print_pause("You run back into the field.\
    Luckily, you don't seem to have been followed.")
    house_or_cave(random_enemy, random_weapon)


def cave(random_enemy, random_weapon):
    print_pause("You peer cautiously into the cave.")
    if random_weapon == "Sword of Ogoroth":
        print_pause("You've been here before, \
        and gotten all the good stuff. \
        It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        house_or_cave(random_enemy, random_weapon)
    else:
        print_pause("It turns out to be only \
        a very small cave.")
        print_pause("Your eye catches a glint \
        of metal behind a rock.")
        print_pause("You have found the magical\
        Sword of Ogoroth!")
        print_pause("You discard your silly old\
        {} and take the sword with you.".format(random_weapon))
        print_pause("You walk back out to the field.")
        random_weapon = "Sword of Ogoroth"
        house_or_cave(random_enemy, random_weapon)


def house(random_enemy, random_weapon):
    print_pause("You approach the door\
    of the house.")
    print_pause("You are about to knock when \
    the door opens and out steps a {}.".format(random_enemy))
    print_pause("Eep! This is the {}'s house!".format(random_enemy))
    print_pause("The {} attacks you!".format(random_enemy))
    if random_weapon != "Sword of Ogoroth":
        print_pause("You feel a bit under-prepared \
        for this, what with only having a tiny {}.".format(random_weapon))
    print_pause("Would you like to (1) fight or (2) run away?")
    action = input()
    if action == '1':
        fight(random_enemy, random_weapon)
    elif action == '2':
        field(random_enemy, random_weapon)
    else:
        play_again()


def house_or_cave(random_enemy, random_weapon):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n(Please enter 1 or 2)")
    while True:
        action = input()
        if action == '1':
            return house(random_enemy, random_weapon)
        elif action == '2':
            return cave(random_enemy, random_weapon)
        else:
            print("(Please enter 1 or 2.)")


def intro(random_enemy, random_weapon):
    print_pause("You find yourself standing in an open field,\
    filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a {} is somewhere\
    around here, and has been \
    terrifying the \
    nearby village.".format(random_enemy))
    print_pause("In front of you is a house.")
    print_pause("To your right \
    is a dark cave.")
    print_pause("In your hand you hold your\
    trusty (but not very effective) {}.".format(random_weapon))
    house_or_cave(random_enemy, random_weapon)


def play_game():
    enemy_creature = ["troll", "pirate", "gorgon", "wicked fairie", "dragon"]
    random_enemy = random.choice(enemy_creature)
    random_weapon = random.choice(["little sword", "dagger", "axe"])
    intro(random_enemy, random_weapon)


play_game()
