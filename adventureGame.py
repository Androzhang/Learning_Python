import time
import random
import story_patch


def print_pause(msg):
    print(msg)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a dragon is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")


def start(devil, pack):
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2.)\n")
    if choice == "1":
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    " and out steps a " + devil + ".")
        print_pause("Eep! This is the " + devil + "'s house!")
        print_pause("The " + devil + " attacks you!")
        if pack == []:
            print_pause("You feel a bit under-prepared for this,"
                        " what with only having a tiny dagger.")
        house(devil, pack)
    elif choice == "2":
        print_pause("You peer cautiously into the cave.")
        cave(devil, pack)
    else:
        start(devil, pack)


def house(devil, pack):
    res_house = input("Would you like to (1) fight or (2) run away?\n")
    if res_house == "1":
        if pack == "":
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the pirate.")
            print_pause("You have been defeated!")
            replay(devil, pack)
        else:
            weapon = pack
            print_pause("As the " + devil + " moves to attack,"
                        " you unsheath your new " + weapon + ".")
            print_pause("The " + weapon + "shines brightly in your"
                        " hand as you brace yourself for the attack.")
            print_pause("But the " + devil + " takes one look at your"
                        " shiny new toy and runs away!")
            print_pause("You have rid the town of the " + devil +
                        ". You are victorious!")
            replay(devil, pack)
    elif res_house == "2":
        print_pause("You run back into the field. Luckily,"
                    " you don't seem to have been followed.")
        start(devil, pack)
    else:
        house(devil, pack)


def cave(devil, pack):
    if pack == "":
        weapon = random.choice(story_patch.weapons)
        pack = weapon
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical " + weapon + ".")
        print_pause("You discard your silly old dagger and take the "
                    + weapon + " with you.")
    else:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
    print_pause("You walk back out to the field.")
    start(devil, pack)


def replay(devil, pack):
    replay_res = input("Would you like to play again? (y/n)\n")
    if replay_res == "y":
        print_pause("Excellent! Restarting the game ...")
        start(devil, pack)
    elif replay_res == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        replay(devil, pack)


def play_game():
    devil = random.choice(story_patch.devils)
    pack = ""
    intro()
    start(devil, pack)


play_game()
