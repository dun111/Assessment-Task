import time
import random

# Global variables
Username = ""
Companion = ""
player = None  # Will be initialized with PlayerData()

def Ticktime():
    time.sleep(random.randint(1, 5))

def lower_health(amount):
    global player
    player["health"] -= amount
    print(f"Your health is now {player['health']}")
    if player["health"] <= 0:
        Death()

def PlayerData(name):
    return {
        "name": name,
        "health": 100,
        "inventory": []
    }

def Death():
    print("You have died. Game over.")
    exit()

def Scary_game():
    global Username, player
    input(
        "****************************\n"
        "    ⚔️ Tales Of Time ⚔️ \n"
        "****************************\n"
        "Press Enter to start..."
    )
    Username = input("Enter your name: ")
    player = PlayerData(Username)
    result = input(f"Hello {Username}, Type 'Enter' to continue or just press Enter: ")
    if result.lower() == "enter" or result.strip() == "":
        print("You woke up in a strange place, with no memory of how you got there. "
            "You look around and see a path leading into the distance. "
            "You decide to follow it, hoping to find some answers...")
        time.sleep(5)
        print("As you walk, you notice the surroundings changing. The path becomes narrower, "
            "and the trees around you grow taller and denser. You feel a sense of unease but continue on...")
        time.sleep(5)
        print('Suddenly, you hear a rustling sound behind you. You turn around quickly, but there is nothing there. '
              'You shake your head, trying to dismiss the feeling of being watched. '
              'You can leave or continue on your journey.')
        choice = input("What do you want to do (Leave/Continue)? ")
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

def Ryan_Chapter():
    global Companion
    time.sleep(2)
    print("Suddenly, out of the blue, a mysterious character jumps out from a bush holding a dagger ready to attack you.")
    RyanChoice = input("You can either type 'Kill' to kill him or type 'Reason' to reason with him: ")
    if RyanChoice.lower() == 'kill':
        print("You tried killing the mysterious character but he proceeds strike you in the stomach.")
        time.sleep(5)
        print("You fall to the ground, bleeding out and unable to move.")
        time.sleep(5)
        print("The mysterious character stands over you, looking down with a mix of pity and regret.")
        time.sleep(5)
        print("You realize that you have made a grave mistake, and your life is now forfeit.")
        time.sleep(5)
        lower_health(5)
        print("You pass out from the pain and lose consciousness.")
        time.sleep(10)
        print("When you wake up you find yourself in a cave resting on the floor with the mysterious character standing nearby.")
        print("He notices you are awake and")
    elif RyanChoice.lower() == 'reason':
        print("Reasoning with the mysterious character, you explain that you mean no harm and are also lost in this strange place.")
        time.sleep(10)
        print("The mysterious character agrees and joins you on your journey to get out of this foreign place.")
        time.sleep(5)
        print("The mysterious character is now your companion.")
        time.sleep(5)
        print("Before continuing, you ask the mysterious character his name.")
        Companion = input("Enter Companion's name: ")
        First_Chapter()
    else:
        Death()

def First_Chapter():
    global Companion, Username
    print(f"Chapter 1: {Companion}'s Problem")
    time.sleep(2)
    print(f'You and {Companion} continue down the path, discussing your situation. ')
    time.sleep(5)
    print(f"You know, I know a way out of here, but I need your help first says {Companion}. ")
    time.sleep(5)
    DaggerChoice = input(f"During our little scuffle, I lost my dagger. Can you help me find it? (Yes/No): ")
    if DaggerChoice.lower() == "yes":
        print("Thank you! I knew I could count on you.")
        time.sleep(2)
        print(f"You and {Companion} start searching the area for the lost dagger.")
        time.sleep(10)
        print("After a while, you find the dagger hidden under some leaves.")
        time.sleep(5)
        print(f"You hand the dagger back to {Companion}, who looks relieved.")
        time.sleep(5)
        print(f"Now that I have my dagger back, I can show you the way out. Follow me, {Username}.")
        time.sleep(5)
        Second_Chapter()
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
        time.sleep(5)
        First_Temple()
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
    while True:
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
        print(
            """
⠀⠀⠀⠀⠀⠀⢀⡀⣴⡄⢸⣀⣀⣈⣿⣿⣁⣀⣀⡇⢠⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠴⠾⠿⠿⠛⠃⠀⠛⠛⠛⠛⠛⠛⠛⠛⠀⠘⠛⠿⠿⠷⠦⠀⠀⠀⠀
⠀⠀⢀⣤⣤⣴⡆⢀⣶⣾⣿⣿⣷⣦⡀⢀⣴⣾⣿⣿⣷⣶⡀⢰⣦⣤⣤⡀⠀⠀
⠀⢠⣾⣿⣿⣿⠇⢸⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇⠸⣿⣿⣿⣷⡄⠀
⠀⠈⠛⣿⣿⣿⠀⠀⡉⠛⠿⠛⢉⣿⡇⢸⣿⡉⠛⠿⠛⢉⠀⠀⣿⣿⣿⣿⠁⠀
⠀⠀⣾⣿⣿⣿⠀⠀⢿⣷⣶⣿⣿⣿⡇⢸⣿⣿⣿⣄⣼⡿⠀⠀⣿⣿⣿⣿⠀⠀
⠀⠀⠘⢉⣉⣉⠀⠀⠸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠇⠀⠀⣉⣉⡉⠁⠀⠀
⠀⠀⠈⣿⣿⣿⡀⠀⠀⣄⣈⠉⠉⠙⠃⠘⠋⣉⣉⣁⣠⠀⠀⢀⣿⣿⣿⠀⠀⠀
⠀⠀⠀⢹⣿⣿⡇⠀⢠⣿⣿⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢸⣿⣿⡏⠀⠀⠀
⠀⠀⠀⠘⣿⣿⣇⠀⢸⣿⣿⣿⣿⣿⠏⠹⣿⣿⣿⣿⣿⡇⠀⣸⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠛⠛⠋⠀⣸⣿⣿⣿⣿⠏⠀⠀⠹⣿⣿⡿⣿⣇⠀⠙⠃⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀"""
        )
        time.sleep(5)
        print("You have a choice to make. Do you want to fight the golem or try to reason with it? (Fight/Reason): ")
        golem_choice = input("What do you want to do? ")
        if golem_choice.lower() == "fight":
            print("You bravely stand your ground and prepare to fight the golem.")
            time.sleep(5)
            print("It charges at you, swinging its massive fists.")
            golemchoice = input("You can either type 'Dodge' to dodge its attack or type 'Attack' to attack it: ")
            if golemchoice.lower() == "dodge":
                print("You quickly dodge the golem's attack, narrowly avoiding its powerful fists.")
                time.sleep(5)
                print("You counterattack, striking the golem with all your might.")
                time.sleep(5)
                print(f"The golem staggers back, but it is not defeated yet. You and {Companion} must work together to defeat it.")
                time.sleep(5)
                while True:
                    golemchoice2 = input(f"You can either type 'Attack' to attack the golem again or type 'Heal' to wake up {Companion}: ")
                    if golemchoice2.lower() == "attack":
                        print(f"You and {Companion} attack the golem with all your might.")
                        time.sleep(5)
                        print("The golem stands unfazed, cracks form but it is still standing.")
                        time.sleep(5)
                        print("You realize that you need to find a way to weaken it before you can defeat it.")
                        break
                    elif golemchoice2.lower() == "heal":
                        print(f"You use a healing potion to wake up {Companion}.")
                        time.sleep(5)
                        print(f"{Companion} is back in the fight!")
                        print("You both attack the golem together, striking it with all your might.")
                        time.sleep(5)
                        print("The golem staggers back, its stone body cracking under your combined assault.")
                        time.sleep(5)
                        print("You both continue to attack the golem, striking it with all your might.")
                        time.sleep(5)
                        print("Finally, with one last powerful blow, the golem crumbles to the ground, defeated.")
                        time.sleep(5)
                        print(f"You and {Companion} stand victorious, breathing heavily from the intense battle.")
                        time.sleep(5)
                        print("You search the golem's remains and find a rusty grey key that unlocks a hidden door in the temple.")
                        time.sleep(5)
                        print(f"You and {Companion} enter the hidden door, hoping to find the princess inside.")
                        time.sleep(5)
                        print("As you step through the door, you find yourselves in a dimly lit chamber filled with ancient artifacts.")
                        time.sleep(5)
                        print("In the center of the room, you see a pedestal with a glowing golden key.")
                        time.sleep(5)
                        print("****************************\n"
                              "  1 Key Achieved 4 left. \n"
                              "****************************\n")
                        Path1()
                        return
            elif golemchoice.lower() == "attack":
                print("You charge at the golem, swinging your weapon with all your might.")
                time.sleep(5)
                print("The golem retaliates with a powerful punch, sending you flying across the room.")
                time.sleep(5)
                Death()
            else:
                print("Invalid choice. The golem charges at you!")
                Death()
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

def Path1():
    global Companion
    while True:
        print("Chapter 4: The Path Ahead")
        time.sleep(2)
        print(f"You and {Companion} exit the temple past the pile of rubble and continue down the path.")
        time.sleep(5)
        askquestion = input(f"You can ask {Companion} a question about the other keys or continue down the path playing with the key. (Ask/Continue): ")
        if askquestion.lower() == "ask":
            print(f"You ask {Companion} about the other keys.")
            time.sleep(5)
            print(f"{Companion} tells you that there are five keys in total, each hidden in a different dungeon across Faron. I don't know the exact locations, but I have heard rumors of their existence.")
            time.sleep(5)
            print(f"You thank {Companion} for the information and continue down the path.")
            break
        elif askquestion.lower() == "continue":
            print("You decide to continue down the path, playing with the key you found.")
            print("The key feels warm in your hand, and you can sense its power.")
            break
        else:
            print("Invalid choice.")
    print(f"The path ahead changes to a lush green tropical forest but you and {Companion} are determined to find the other keys and rescue the princess.")



def Third_Chapter():
    global Companion
    print("Chapter 5: The Goblin Camp")
    time.sleep(2)
    print(f"You and {Companion} arrive at the goblin camp, a makeshift settlement hidden deep in the forest.")
    time.sleep(5)
    print("As you enter, you can feel the tension in the air. The goblins eye you suspiciously, their weapons at the ready.")
    time.sleep(5)
    print("You know that this will be a difficult challenge, but you are determined to find the next key.")
    time.sleep(5)
    print(f"{Companion} whispers, 'We need to be careful. The goblins are known for their traps and ambushes.'")
    time.sleep(5)
    print("You nod in agreement and start to plan your approach.")
    time.sleep(5)
    print(f"{Companion} whispers, 'Stay here, I'll go talk to the camp chief and see if they know anything about the key.'")
    time.sleep(5)
    print(f"{Companion} disappears around the corner of a hut, leaving you alone in the camp.")
    time.sleep(5)
    goblinchoice = input(f"Now you have a choice to make. Do you want to wait for {Companion} to return or explore the camp on your own? (Wait/Explore): ")
    if goblinchoice.lower() == "wait":
        print(f"You decide to wait for {Companion} to return.")
        time.sleep(5)
        print(f"{Companion} returns after a while, looking worried.")
        time.sleep(5)
        print(f"'{Companion} says, 'The goblin chief knows about the key, but he won't give it up easily.'")
        time.sleep(5)
    elif goblinchoice.lower() == "explore":
        while True:
        print("You decide to explore the camp on your own.")
        time.sleep(5)
        print("As you look around, you notice a few goblins eyeing you suspiciously.")
        time.sleep(5)
        print("Nonetheless, you continue to explore, hoping to find some clues about the key.")
        time.sleep(5)
        print("You find a small hut with a sign that reads 'Storage Space'.")
        goblinchoice2 = input("Do you want to enter the hut? (Yes/No): ")
        if goblinchoice2.lower() == "yes":
            while True:
            time.sleep(5)
            print("You enter the hut and find a chest in the corner.")
            time.sleep(5)
            print("You open the chest and find a dusty yellow map inside.")
            time.sleep(5)
            print("You take the map and return to the main camp area.")
            print(f"You find {Companion} waiting for you, looking relieved.")
            time.sleep(5)
            print(f"'{Companion} says, 'I was worried about you. Did you find anything useful?'")
            time.sleep(5)
            print("You show {Companion} the map you found in the hut.")
            time.sleep(5)
            print(f"{Companion} examines the map and says, 'This looks like to the next dungeon It might help us find the key!'")
            break
        elif goblinchoice2.lower() == "no":
            print("You decide not to enter the hut and continue exploring the camp.")
            time.sleep(5)
            print("You wander around, but you don't find anything else of interest.")
            time.sleep(5)
            print(f"You return to the main camp area, where you find {Companion} waiting for you.")
            time.sleep(5)
            print(f"'{Companion} says, 'Did you find anything useful?'")
            time.sleep(5)
            print("You tell {Companion} that you didn't find anything, but you feel like you might have missed something important.")
            time.sleep(5)
            print(f"{Companion} nods and says, 'We should keep looking. The goblins might have more information about the key.'")
        else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")

def Dungeon2()
    global Companion
    print("Chapter 6: The Jungle Dungeon")
    time.sleep(2)
    print(f"You and {Companion} arrive at the entrance of the lush green cavern, the second dungeon.")
    time.sleep(5)
    print("The air is thick with moisture, and you can hear the sound of dripping water echoing through the darkness.")
    time.sleep(5)
    print("You light a torch and step inside, the flickering light revealing jagged rocks and narrow passages.")
    time.sleep(5)
    print(f"{Companion} says, 'Be careful. This place is known for its traps and dangerous creatures.'")
    time.sleep(5)
    print("You nod and start to explore the cavern, searching for the key.")
    time.sleep(5)
    print("As you venture deeper, you come across a large underground lake.")
    time.sleep(5)
    print("In the center of the lake, you see a small island with a pedestal on it.")
    time.sleep(5)
    print("On the pedestal, you can see a glimmering blue key.")
    time.sleep(5)
    print(f"You and {Companion} realize that this must be the second key you are looking for.")
    time.sleep(5)
    print(f"Before either of you could react, a giant beast emerges from the water, its eyes glowing with a menacing light.")
    time.sleep(5)
    print("The beast is a massive serpent, its scales glistening in the torchlight.")
    time.sleep(5)
    print("****************************\n"
          "Serpus The Beast of the Lake \n"
          "****************************\n")
    

if __name__ == "__main__":
    Scary_game()
