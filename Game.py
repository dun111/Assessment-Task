import time
import random


def Ticktime():
    """Pause the game for a random short duration to simulate time passing."""
    time.sleep(random.randint(1, 5))

def PlayerData():
    player = {
        "name": "Username",
        "health": 100,
        "inventory": []
    }
    return player


def Death():
    print("You have died. Game over.")
    exit()  # This function handles the death scenario in the game, printing a message and exiting the game.        


def Scary_game():
    global Username
    input(
        "****************************\n"
        "    ⚔️ Tales Of Time ⚔️ \n"
        "****************************\n"
        "Press Enter to start..."
    )
    # This code starts the game by displaying a welcome message and waiting for the user to press Enter.
    Username = input("Enter your name: ")
    result = input(f"Hello {Username}, Type 'Enter' to continue: ")
    # This code prompts the user to enter their name and then greets them.
    if result.lower() == "enter":
        print("You woke up in a strange place, with no memory of how you got there. "
            "You look around and see a path leading into the distance. "
            "You decide to follow it, hoping to find some answers...")
        time.sleep(5)
        print("As you walk, you notice the surroundings changing. The path becomes narrower, "
            "and the trees around you grow taller and denser. You feel a sense of unease but continue on...")
        time.sleep(5)
        print('Suddenly, you hear a rustling sound behind you. You turn around quickly, but there is nothing there. '
              'You shake your head, trying to dismiss the feeling of being watched '
              '(To Leave Type "Leave" or to Continue Type "Continue")')
        choice = input("What do you want to do? ")
        if choice.lower() == "leave":
            Death()
        elif choice.lower() == "continue":
            print("You chose to continue. Moving forward...")
            Ryan_Chapter()
        else:
            Death()
    else:
        print("You chose not to continue. Exiting the game.")
        exit()
    # This code continues the story after the user has chosen to continue.

def Ryan_Chapter():
    global Companion
    time.sleep(2)
    print("Suddenly, out of the blue, A mysterious character jumps out from a bush holding a dagger ready to attack you.")
    RyanChoice = input("You can either type 'Kill' to kill him or type 'Reason' to reason with him: ")
    if RyanChoice.lower() == 'kill':
        print("You tried killing the mysterious character but he proceeds to sit on you")
        Death()
    elif RyanChoice.lower() == 'reason':
        print("Reasoning with the mysterious character, you explain that you mean no harm and are also lost in this strange place.")
        time.sleep(10)
        print("The mysterious character agrees and joins you on your journey to get out of this foreign place")
        time.sleep(5)
        print("The mysterious character is now your companion.")
        time.sleep(5)
        Companion = input("Before continuing, you ask the mysterious character his name.")
        First_Chapter()
    else:
        Death()
        Death()
def First_Chapter():
    global Companion, Username
    print(f"Chapter 1: The {Companion}'s Problem")
    time.sleep(2)
    print(f'You and {Companion} continue down the path, discussing your situation. ')
    time.sleep(5)
    print("You know, I know a way out of here, but I need your help first. ")
    time.sleep(5)
    DaggerChoice = input("During our little scuffle, I lost my dagger. Can you help me find it? (Yes/No): ")
    if DaggerChoice.lower() == "yes":
        print("Thank you! I knew I could count on you.")
        time.sleep(2)
        print(f"you and {Companion} start searching the area for the lost dagger.")
        time.sleep(10)
        print("After a while, you find the dagger hidden under some leaves.")
        time.sleep(5)
        print(f"You hand the dagger back to {Companion}, who looks relieved.")
        time.sleep(5)
        print(f"Now that I have my dagger back, I can show you the way out. Follow me, {Username}.")
        time.sleep(5)
    else:
        print("Too bad, I guess you don't want to leave this place.")
        time.sleep(10)
        print("The mysterious character turns away and walks off into the darkness, leaving you alone.")
        print("You died of loneliness and despair.")
        Death()
    time.sleep(5)
def Second_Chapter():
    global Companion
    print(f"Chapter 2: The Lost Princess of Faron")
    print("Ok, so you see, This place is called Faron, it used to be a beautiful place, ruled by a princess.")
    time.sleep(5)
    print("But now, it's just a shadow of its former self, plagued by dark creatures and lost souls.")
    time.sleep(5)
    print(f"As you and {Companion} walk, you can feel the weight of the history around you.")
    print("You see ruins of old buildings, broken statues, and remnants of a once-thriving civilization in the distance.")
    print(f"You ask {Companion} about the princess and what happened to her.")
    time.sleep(5)
    print(f"{Companion} looks sad and says, 'The princess was taken by the monsters that consumed this place. "
          "She was the last hope for Faron, but now she's gone.")
    time.sleep(5)
    print("You feel a sense of determination to find a way to save Faron and its lost princess. ")
    print(f"You ask {Companion} where is the princess now?")
    time.sleep(5)
    print(f"{Companion} replies, 'I don't know, but I have heard rumors of a hidden temple deep in the forest. "
          "It's said that the princess is trapped there, guarded by powerful creatures.'")
    time.sleep(5)
    princesschoice = input("You have a choice to make. Do you want to go to the temple and try to rescue the princess? (Yes/No): ")
    if princesschoice.lower() == "yes":
        print(f"You and {Companion} set off towards the hidden temple, determined to rescue the princess.")
    else:
        print("You decide not to take the risk and continue on your current path.")
        print("All of a sudden, you hear a loud roar and a bull appears out of nowhere.")
        bullfight = input("You can either type 'Run' to run away or type 'Fight' to fight the bull: ")
        if bullfight.lower() == "run":
            print("You turn and run as fast as you can, escaping the bull's charge.")
            time.sleep(5)
            print("Unfortunately, you run into a dead end and the bull catches up to you.")
            time.sleep(5)
            Death()
        elif bullfight.lower() == "fight":
            print("You bravely stand your ground and prepare to fight the bull.")
            time.sleep(5)
            print("You regret your choice")
            time.sleep(5)
            Death()
        else:
            print("Invalid choice. The bull charges at you!")
            Death()
    time.sleep(5)
def First_Temple():
    global Companion
    print("Chapter 3: The Hidden Temple")
    time.sleep(2)
    print(f"You and {Companion} arrive at the hidden temple, its entrance shrouded in vines and darkness.")
    time.sleep(5)
    print("As you step inside, you feel a chill run down your spine. The air is thick with dust and the smell of decay.")
    time.sleep(5)
    print("You can hear the faint sound of water dripping in the distance, echoing through the empty halls.")
    time.sleep(5)
    print(f"You and {Companion} cautiously explore the temple, searching for any signs of the princess.")
    time.sleep(5)
    print("Suddenly, you hear a loud roar and a giant creature appears in front of you, blocking your path.")
    time.sleep(5)
    print("The creature is a massive stone golem, its eyes glowing with an eerie light.")
    time.sleep(5)
    print(f"All of a sudden, the golem charges at {Companion} and knocks them to the wall")
    time.sleep(5)
    print("****************************\n"
          " Forging The Beast of Stone \n"
          "****************************\n")
    time.sleep(5)
    print("You have a choice to make. Do you want to fight the golem or try to reason with it? (Fight/Reason): ")
    golem_choice = input("What do you want to do? ")
    if golem_choice.lower() == "fight":
        print("You bravely stand your ground and prepare to fight the golem.")
        time.sleep(5)
        print("You manage to defeat the golem, but not without sustaining some injuries.")
        time.sleep(5)
        print(f"You and {Companion} continue deeper into the temple, determined to find the princess.")
    elif golem_choice.lower() == "reason":
        print("You try to reason with the golem, explaining that you mean no harm and are only looking for the princess.")
        time.sleep(5)
        print("Never do that again, the golem doesn't speak English, it does speak with fists")
        time.sleep(5)
        print("The golem knocks you out cold")
        time.sleep(5)
        Death()
    else:
        print("Invalid choice. The golem charges at you!")
        time.sleep(5)
        Death()

if __name__ == "__main__":
    Scary_game()
