import time
import random

# Global variables
Username = ""
Companion = ""
player = None  # Will be initialized with PlayerData()

Bull=("""
      
             _.-````'-,_
   _,.,_ ,-'`           `'-.,_
 /)     (\                   '``-.
((      ) )                      `\
 \)    (_/                        )\
  |       /)           '    ,'    / \
  `\    ^'            '     (    /  ))
    |      _/\ ,     /    ,,`\   (  "`
     \Y,   |  \  \  | ````| / \_ \
       `)_/    \  \  )    ( >  ( >
                \( \(     |/   |/
               /_(/_(    /_(  /_( 
      
""")

Flame = ("""    
         
                  __~a~_
                  ~~;  ~_
    _                ~  ~_                _
   '_\;__._._._._._._]   ~_._._._._._.__;/_`
   '(/'/'/'/'|'|'|'| (    )|'|'|'|'\'\'\'\)'
   (/ / / /, | | | |(/    \) | | | ,\ \ \ \)
  (/ / / / / | | | ^(/    \) ^ | | \ \ \ \ \)
 (/ / / / /  ^ ^ ^   (/  \)    ^ ^  \ \ \ \ \)
(/ / / / ^          / (||)|          ^ \ \ \ \)
^ / / ^            M  /||\M             ^ \ \ ^
 ^ ^                  /||\                 ^ ^
                     //||\\
                     //||\\
                     //||\\         
                     '/||\'

""")

Golem = ("""
         
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
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⠉⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀

""")


Wraith = ("""
          
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⢠⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠄⠀⠀⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⠀⠀⠀⣸⣦⣸⣧⣼⣿⣦⣄⣀⣈⣴⣾⣿⣿⣦⡐⠄⠀⠀⠀⠀
⠀⢠⣶⣶⣦⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡌⡀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢠⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡙⢿⡿⠛⢿⣿⣿⣿⠀⠀⠀
⠀⠄⢿⣿⣿⣿⡿⠿⣿⡿⠉⠙⣿⣿⣿⣿⣿⡇⢘⠐⠨⠄⠁⠄⢻⣿⣿⠀⠀⠀
⠀⠀⡈⢿⣿⣿⡇⠆⠈⠃⠃⠁⠸⣿⣿⣿⣿⣷⢸⠀⠀⠀⠀⠈⡈⢿⡿⢀⠀⠀
⠀⠀⠀⠄⠻⣿⣇⠠⠀⠀⠀⠀⠂⢹⣿⣿⣿⣿⠈⠀⠀⠀⠀⠀⢀⠸⠋⠄⠀⠀
⠀⠀⠀⠀⠀⠈⠻⡆⠀⠀⠀⠀⠈⠄⢿⣿⣿⣿⡆⠂⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠈⠄⢻⣿⣿⣧⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠹⣿⣿⡆⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢿⣿⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡙⠳⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

Desbio = ("""

  .:'                                  `:.
 ::'                                    `::
:: :.                                  .: ::
 `:. `:.             .             .:'  .:'
   `::. `::          !           ::' .::'
      `::.`::.    .' ! `.    .::'.::'
        `:.  `::::'':!:``::::'   ::'
        :'*:::.  .:' ! `:.  .:::*`:
       :: HHH::.   ` ! '   .::HHH ::
      ::: `H TH::.  `!'  .::HT H' :::
      ::..  `THHH:`:   :':HHHT'  ..::
      `::      `T: `. .' :T'      ::'
        `:. .   :         :   . .:'
          `::'               `::'
            :'  .`.  .  .'.  `:
            :' ::.       .:: `:
            :' `:::     :::' `:
             `.  ``     ''  .'
              :`...........':
              ` :`.     .': '
               `:  `...'  :' 

""")


def lower_health(amount=None):
    global player
    global health
    if amount is None:
        amount = random.randint(10, 100)  # Random damage
    health -= amount
    print(f"You took {amount} damage! Your health is now {health}.")
    if health <= 0:
        print("You have died...")
        Death()
    if health <=10:
        print("Low Health!")



def increase_health(amount):
    global player
    if player is None:
        print("Error: Player not initialized.")
        Death()
        return
    player["health"] += amount
    print(f"Your health is now {player['health']}")

def reset_health():
    global player
    if player is None:
        print("Error: Player not initialized.")
        Death()
        return
    player["health"] = 100
    print("Your health has been reset to 100.")

def PlayerData(name):
    return {"name": name,
            "health": 100,
            "inventory": []}

def Death():
    print("You have died. Game over.")
    time.sleep(2)
    print("Do you want to restart the game? (Yes/No): ")
    choice = input().strip().lower()
    if choice == "yes":
        Restart()
    elif choice == "no":
        print("Thank you for playing!")
        exit()
    else:
        print("Bye! Exiting the game.")
        exit()

def Restart():
    global Username, player, Companion
    print("Restarting the game...")
    Username = ""
    player = None
    Companion = ""
    main()

def main():
    global Username, player, health
    print(r"""
  _____     _                    __   _____              
 |_   _|_ _| | ___  ___   / _ \ / _| |_   _|(_)_ __ ___   ___ 
   | |/ _` | |/ _ \/ __| | | | | |_    | |  | | '_ ` _ \ / _ |
   | | (_| | |  __/\__ \ | |_| |  _|   | |  | | | | | | |  __/
   |_|\__,_|_|\___||___/  \___/|_|     |_|  |_|_| |_| |_|\___|
   
 """)
    print("         Press Enter to start...")
    input()  # Wait for user to press Enter
    Username = input("Enter your name: ")
    player = PlayerData(Username)
    while True:
     result = input(f"Hello {Username}, Type 'Enter' to continue or just press Enter: ")
     match result.lower().strip():
        case "enter" | '':
            print("You woke up in a strange place, with no memory of how you got there... ")
            time.sleep(2)
            print("You look around and see a path leading into the distance... ")
            time.sleep(2)
            print("You decide to follow it, hoping to find some answers...")
            time.sleep(2)
            print("As you walk, you notice the surroundings changing. The path becomes narrower, "
                  "and the trees around you grow taller and denser. You feel a sense of unease but continue on...")
            time.sleep(2)
            print('Suddenly, you hear a rustling sound behind you. You turn around quickly, but there is nothing there... ')
            time.sleep(2)
            print('You shake your head, trying to dismiss the feeling of being watched... ')
            time.sleep(2)
            print('You can leave or continue on your journey...')
            choice = input("What do you want to do (Leave/Continue)? ")
            match choice.lower().strip():
                case "leave":
                    print("You chose not to continue. Exiting the game.")
                    Death()
                case "continue":
                    print("You chose to continue. Moving forward...")
                    Ryan_Chapter()
                case _:
                    print("Invalid Option")
                    print("Try Again")

def Ryan_Chapter():
    global Companion, Username, health
    time.sleep(2)
    print("Suddenly, out of the blue, a mysterious character jumps out from a bush holding a dagger ready to attack you...")
    time.sleep(5)
    RyanChoice = input("You can either type 'Kill' to kill him or type 'Reason' to reason with him: ")
    if RyanChoice.lower() == 'kill':
        print("You tried killing the mysterious character but they proceed to strike you in the stomach...")
        time.sleep(5)
        print("You fall to the ground, bleeding out and unable to move...")
        time.sleep(5)
        print("The mysterious character stands over you, looking down with a mix of pity and regret...")
        time.sleep(5)
        print("You realize that you have made a grave mistake, and your life is now forfeit...")
        time.sleep(5)
        lower_health(90)
        print("You pass out from the pain and lose consciousness...")
        time.sleep(10)
        print("When you wake up you find yourself in a cave resting on the floor with the mysterious character standing nearby...")
        time.sleep(5)
        print("He notices you are awake and runs off into the darkness, leaving you alone in the cave...")
        time.sleep(5)
        print("You died of loneliness and despair...")
        Death()
        return  # Prevent further execution
    elif RyanChoice.lower() == 'reason':
        print("Reasoning with the mysterious character, you explain that you mean no harm and are also lost in this strange place...")
        time.sleep(10)
        print("The mysterious character agrees and joins you on your journey to get out of this foreign place...")
        time.sleep(5)
        print("The mysterious character is now your companion...")
        time.sleep(5)
        print("Before continuing, you ask the mysterious character his name...")
        Companion = input("Enter Companion's name: ")
        Chapter_1()
        return
    else:
        Death()
        return

def Chapter_1():
    global Companion, Username, health
    print(f"***************************\n"
         f"Chapter 1: {Companion}'s Dilemma\n"
           "***************************\n")
    time.sleep(2)
    print(f'You and {Companion} continue down the path, discussing your situation... ')
    time.sleep(5)
    print(f"'You know, I know a way out of here, but I need your help first,' says {Companion}... ")
    time.sleep(5)
    DaggerChoice = input(f"During our little scuffle, I lost my dagger. Can you help me find it? (Yes/No): ")
    if DaggerChoice.lower() == "yes":
        print("Thank you! I knew I could count on you...")
        time.sleep(2)
        print(f"You and {Companion} start searching the area for the lost dagger...")
        time.sleep(10)
        print("After a while, you find the dagger hidden under some leaves...")
        time.sleep(5)
        print(f"You hand the dagger back to {Companion}, who looks relieved...")
        time.sleep(5)
        print(f"Now that I have my dagger back, I can show you the way out. Follow me, {Username}...")
        time.sleep(5)
        Chapter_2()
        return
    else:
        print("Too bad, I guess you don't want to leave this place...")
        time.sleep(10)
        print(f"{Companion} turns away and walks off into the darkness, leaving you alone...")
        time.sleep(5)
        print("You died of loneliness and despair.")
        Death()
        return

def Chapter_2():
    global Companion, Username, health
    print(f"***************************\n"
       "Chapter 2: The Lost Princess of Faron\n"
          f"***************************\n")
    time.sleep(5)
    print(f"Ok, so you see, This place is called Faron, it used to be a beautiful place, ruled by a princess. {Companion} says...")
    time.sleep(5)
    print("But now, it's just a shadow of its former self, plagued by dark creatures and monsters...")
    time.sleep(5)
    print(f"As you and {Companion} walk, you can feel the weight of the history around you...")
    time.sleep(5)
    print("You see ruins of old buildings, broken statues, and remnants of a once-thriving civilization in the distance...")
    time.sleep(5)
    print(f"You ask {Companion} about the princess and what happened to her...")
    time.sleep(5)
    print(f"{Companion} looks sad and says, 'The princess was taken by the monsters that consumed this place...")
    time.sleep(5)
    print("She was the last hope for Faron, but now she's gone...")
    time.sleep(5)
    print("You feel a sense of determination to find a way to save Faron and its lost princess...")
    time.sleep(5)
    print(f"You ask {Companion} where the princess is at now?")
    time.sleep(5)
    print(f"{Companion} replies, 'I don't know, but I have heard rumors of a hidden temple deep in the forest. "
          "It's said that the princess is trapped there, guarded by powerful creatures...'")
    time.sleep(5)
    princesschoice = input("You have a choice to make. Do you want to go to the temple and try to rescue the princess? (Yes/No): ")
    if princesschoice.lower() == "yes":
        print(f"You and {Companion} set off towards the hidden temple, determined to rescue the princess...")
        time.sleep(5)
        Chapter_3()
        return
    else:
        print("You decide not to take the risk and continue on your current path.")
        time.sleep(5)
        print("All of a sudden, you hear a loud roar and a bull appears out of nowhere.")
        time.sleep(5)
        print(Bull)
        time.sleep(5)
        bullfight = input("You can either type 'Run' to run away or type 'Fight' to fight the bull: ")
        if bullfight.lower() == "run":
            print("You turn and run as fast as you can, escaping the bull's charge.")
            time.sleep(5)
            print("Unfortunately, you run into a dead end and the bull catches up to you.")
            time.sleep(5)
            Death()
            return
        elif bullfight.lower() == "fight":
            print("You bravely stand your ground and prepare to fight the bull.")
            time.sleep(5)
            print("You regret your choice")
            time.sleep(5)
            Death()
            return
        else:
            print("Invalid choice. The bull charges at you!")
            Death()
            return
    time.sleep(5)

def Chapter_3():
    global Companion, Username, health
    while True:
        print("***************************\n"
              "Chapter 3: The Hidden Temple\n"
              "***************************\n")
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
        print(Golem)
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
                        Chapter_4()
                        return
            elif golemchoice.lower() == "attack":
                print("You charge at the golem, swinging your weapon with all your might.")
                time.sleep(5)
                print("The golem retaliates with a powerful punch, sending you flying across the room.")
                time.sleep(5)
                Death()
                return
            else:
                print("Invalid choice. The golem charges at you!")
                Death()
                return
        elif golem_choice.lower() == "reason":
            print("You try to reason with the golem, explaining that you mean no harm and are only looking for the princess.")
            time.sleep(5)
            print("Never do that again, the golem doesn't speak English, it does speak with fists")
            time.sleep(5)
            print("The golem knocks you out cold")
            time.sleep(5)
            Death()
            return
        else:
            print("Invalid choice. The golem charges at you!")
            time.sleep(5)
            Death()
            return

def Chapter_4():
    global Companion
    while True:
        print("***************************\n"
              "Chapter 4: The Path Ahead\n"
              "***************************\n")
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
            print(f"The path ahead changes to a lush green tropical forest but you and {Companion} are determined to find the other keys and rescue the princess.")
            Chapter_5()
            break
        elif askquestion.lower() == "continue":
            print("You decide to continue down the path, playing with the key you found.")
            print("The key feels warm in your hand, and you can sense its power.")
            print(f"The path ahead changes to a lush green tropical forest but you and {Companion} are determined to find the other keys and rescue the princess.")
            Chapter_5()
            break
        else:
            print("Invalid choice, Try again")
        



def Chapter_5():
    global Companion, Username, health
    print("***************************\n"
          "Chapter 5: The Goblin Camp\n"
          "***************************\n")
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
        rest_choice = input(f"Do you want to try to reason with the goblin chief or attack him? (Reason/Attack): ")
        if rest_choice.lower() == "reason":
            print(f"You and {Companion} approach the goblin chief, trying to reason with him.")
            time.sleep(5)
            print("The goblin chief listens to your plea, but he is not convinced.")
            time.sleep(5)
            print(f"'{Companion} says, 'We need to find another way to get the key.'")
            time.sleep(5)
            print("You nod in agreement and start to plan your next move.")
            time.sleep(5)
            print("You decide to explore the camp further, hoping to find some clues about the key.")
            time.sleep(5)
            Chapter_5()
        elif rest_choice.lower() == "attack":
            print(f"You and {Companion} decide to attack the goblin chief.")
            time.sleep(5)
            print("The goblin chief fights back fiercely, but you manage to defeat him after a tough battle.")
            time.sleep(5)
            print("You search the goblin chief's hut and find a map that leads to the next dungeon.")
            time.sleep(5)
            print(f"You and {Companion} take the map and prepare to continue your journey.")
            Chapter_6()
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
             print(f"You show {Companion} the map you found in the hut.")
             time.sleep(5)
             print(f"{Companion} examines the map and says, 'This looks like to the next dungeon It might help us find the key!'")
             Chapter_6()
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
             print(f"You tell {Companion} that you didn't find anything, but you feel like you might have missed something important.")
             time.sleep(5)
             print(f"{Companion} nods and says, 'We should keep looking. The goblins might have more information about the key.'")

         else:
            print("Invalid choice.")

    else:
        print("Invalid choice.")
        return

def Chapter_6():
    while True:
        global Companion, Username, health
        print("***************************\n"
            "Chapter 6: The Jungle Dungeon\n"
              "***************************\n")
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
        time.sleep(5)
        print("Before either of you could move, Serpus strikes you both in the back")
        lower_health(20)
        print(f"{Companion}'s health is low")
        time.sleep(5)  # <-- fix: was just 'time'
        serpentchoice = input("Serpus is charging up it's next attack, (Attack/Dodge)")
        if serpentchoice.lower() == "attack":
            print("Serpus strikes you in the stomach and injures you")
            time.sleep(5)
            lower_health(20)
            print(f"{Companion}'s health is low")
            time.sleep(5)
            print(f"You and {Companion} are both injured and need to find a way to defeat Serpus before it attacks again.")
            time.sleep(5)
            serpentchoice2 = input(f"You can either type 'Attack' to attack Serpus or type 'Heal' to heal yourself and {Companion}: ")
            if serpentchoice2.lower() == "attack":
                print(f"You and {Companion} attack Serpus with all your might, striking it with your weapons.")
                time.sleep(5)
                print("Serpus roars in pain, but it is not defeated yet.")
                time.sleep(5)
                serpentchoicesemi2 = input(f"Type 'Attack' to attack Serpus again or type 'Heal' to heal yourself and {Companion}: ")
                while True:
                 if serpentchoicesemi2.lower() == "attack":
                    print(f"You and {Companion} attack Serpus with all your might.")
                    time.sleep(5)
                    print("Serpus roars in pain, but it is not defeated yet.")
                    time.sleep(5)
                    print("You realize that you need to find a way to weaken it before you can defeat it.")
                    time.sleep(5)
                 elif serpentchoicesemi2.lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {Companion}.")
                    time.sleep(5)
                    print(f"{Companion} is back in the fight!")
                    time.sleep(5)
                    print("You both attack Serpus together, striking it with all your might.")
                    time.sleep(5)
                    print("Serpus roars in pain, but it is not defeated yet.")
                    time.sleep(5)
                    serpentchoicesemi3 = input(f"Type 'Attack' to attack Serpus again or type 'Heal' to heal yourself and {Companion}: ")
                    if serpentchoicesemi3.lower() == "attack":
                        print(f"You and {Companion} attack Serpus's core with all your might, striking it with your weapons.")
                        time.sleep(5)
                        print("Serpus roars in pain, and it crumbles to the ground, defeated.")
                        time.sleep(5)
                        print(f"You and {Companion} stand victorious, breathing heavily from the intense battle.")
                        time.sleep(5)
                        print("You search the serpent's remains and find a glimmering blue key that unlocks a hidden door in the cavern.")
                        time.sleep(5)
                        print(f"You and {Companion} enter the hidden door, hoping to find the next key inside.")
                        time.sleep(5)
                        print("As you step through the door, you find yourselves in a dimly lit chamber filled with ancient artifacts.")
                        time.sleep(5)
                        print("In the center of the room, you see a pedestal with a glowing blue key.")
                        time.sleep(5)
                        print("****************************\n"
                              "  2 Key Achieved 3 left. \n"
                              "****************************\n")
                        print(f"You and {Companion} take the key and prepare to continue your journey.")
                        break
            elif serpentchoice2.lower() == "heal":
                print(f"You use a healing potion to heal yourself and {Companion}.")
                time.sleep(5)
                print(f"{Companion} is back in the fight!")
                time.sleep(5)
                print("You both attack Serpus together, striking it with all your might.")
                time.sleep(5)
                print("Serpus roars in pain, but it is not defeated yet.")
                time.sleep(5)
            else:
                print("Invalid choice. Serpus attacks you again!")
                Death()
                return
        elif serpentchoice.lower() == "dodge":
            print("You quickly dodge Serpus's attack, narrowly avoiding its powerful strike.")
            time.sleep(5)
            print("You counterattack, striking Serpus with all your might.")
            time.sleep(5)
            print(f"The serpent staggers back, but it is not defeated yet. You and {Companion} must work together to defeat it.")
            time.sleep(5)
            while True:
                serpentchoice2 = input(f"You can either type 'Attack' to attack Serpus again or type 'Heal' to heal yourself and {Companion}: ")
                if serpentchoice2.lower() == "attack":
                    print(f"You and {Companion} attack Serpus with all your might.")
                    time.sleep(5)
                    print("Serpus roars in pain, but it is not defeated yet.")
                    time.sleep(5)
                    print("You realize that you need to find a way to weaken it before you can defeat it.")
                    break
                elif serpentchoice2.lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {Companion}.")
                    time.sleep(5)
                    print(f"{Companion} is back in the fight!")
                    time.sleep(5)
                    print("You both attack Serpus together, striking it with all your might.")
                    time.sleep(5)
        elif serpentchoice.lower() == "dodge":
            print("You quickly dodge Serpus's attack, narrowly avoiding its powerful strike.")
            time.sleep(5)
            print("You counterattack, striking Serpus with all your might.")
            time.sleep(5)
            print(f"The serpent staggers back, but it is not defeated yet. You and {Companion} must work together to defeat it.")
            time.sleep(5)
            while True:
                serpentchoice2 = input(f"You can either type 'Attack' to attack Serpus again or type 'Heal' to heal yourself and {Companion}: ")
                if serpentchoice2.lower() == "attack":
                    print(f"You and {Companion} attack Serpus with all your might.")
                    time.sleep(5)
                    print("Serpus roars in pain, but it is not defeated yet.")
                    time.sleep(5)
                    print("You realize that you need to find a way to weaken it before you can defeat it.")
                    break
                elif serpentchoice2.lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {Companion}.")
                    time.sleep(5)
                    print(f"{Companion} is back in the fight!")
                    time.sleep(5)
                    print("You both attack Serpus together, striking it with all your might.")
                    time.sleep(5)
                    print("Serpus roars in pain, but it is not defeated yet.")
                    time.sleep(5)
                    break
                else:
                    print("Invalid choice. Serpus attacks you again!")
                    Death()
                    return
        else:
            print("Invalid choice. Serpus attacks you again!")
            Death()
            return
        print(f"You and {Companion} must find a way to defeat Serpus and claim the key.")
        time.sleep(5)
        print("You both attack Serpus with all your might, striking it with your weapons.")
        time.sleep(5)
        print("Finally, with one last powerful blow, Serpus roars in pain and sinks back into the depths of the lake.")
        time.sleep(5)
        print(f"You and {Companion} stand victorious, breathing heavily from the intense battle.")
        time.sleep(5)
        print("You search the serpent's remains and find a glimmering blue key that unlocks a hidden door in the cavern.")
        time.sleep(5)
        print(f"You and {Companion} enter the hidden door, hoping to find the next key inside.")
        time.sleep(5)
        print("As you step through the door, you find yourselves in a dimly lit chamber filled with ancient artifacts.")
        time.sleep(5)
        print("In the center of the room, you see a pedestal with a glowing blue key.")
        time.sleep(5)
        print("****************************\n"
              "  2 Key Achieved 3 left. \n"
              "****************************\n")
        print(f"You and {Companion} take the key and prepare to continue your journey.")
        break

def Chapter_7():
    global Companion, Username, health
    print("***************************\n"
    "Chapter 7: The Path to the Fire Dungeon\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {Companion} exit the jungle cavern and continue down the path, the lush greenery giving way to rocky terrain.")
    time.sleep(5)
    print("The air grows hotter, and you can feel the heat radiating from the ground.")
    time.sleep(5)
    print(f"{Companion} says, 'The next key is said to be hidden in a fire dungeon, deep within the mountains according to the map.'")
    time.sleep(5)
    print("You nod in agreement, determined to find the next key and rescue the princess.") 
    time.sleep(5)
    print("As you continue down the path, you come across a group of goblins blocking your way.")
    time.sleep(5)
    print("The goblins are armed with crude weapons and look ready for a fight.")
    time.sleep(5)
    print(f"{Companion} whispers, 'We need to be careful. The goblins are known for their traps and ambushes.'")
    time.sleep(5)
    goblinchoice3 = input("Do you want to fight the goblins or try to reason with them? (Fight/Reason): ")
    if goblinchoice3.lower() == "fight":
        print(f"You and {Companion} charge at the goblins, weapons drawn.")
        time.sleep(5)
        print(f"The goblins fight back fiercely, but you and {Companion} are able to defeat them after a tough battle.")
        time.sleep(5)
        print("You search the goblins' remains and find a map that leads to the fire dungeon.")
        time.sleep(5)
        print(f"You and {Companion} take the map and prepare to continue your journey.")
        time.sleep(5)
    elif goblinchoice3.lower() == "reason":
        print("You try to reason with the goblins, explaining that you mean no harm and are only looking for the next key.")
        time.sleep(5)
        print("The goblins listen to your words, but they are still wary of you.")
        time.sleep(5)
        print(f"{Companion} suggests that you offer them something in exchange for safe passage.")
        time.sleep(5)
        offer = input("Do you want to offer them some of your supplies? (Yes/No): ")
        if offer.lower() == "yes":
            print("You offer the goblins some of your supplies, and they accept your offer.")
            time.sleep(5)
            print(f"The goblins allow you and {Companion} to pass safely, and you continue on your journey.")
        elif offer.lower() == "no":
            print("The goblins refuse to let you pass without a fight.")
            time.sleep(5)
            print(f"You and {Companion} are forced to fight the goblins, but you are able to defeat them after a tough battle.")
            time.sleep(5)
            print("You search the goblins' sacks and find a map that leads to the fire dungeon.")
            time.sleep(5)
            print(f"You and {Companion} take the map and prepare to continue your journey.")

def Chapter_8():
    global Companion, Username, health
    print("***************************\n"
          "Chapter 8: The Fire Dungeon\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {Companion} arrive at the entrance of the fire dungeon, a dark cave filled with molten lava and fire.")
    time.sleep(5)
    print("The heat is intense, and you can feel the sweat pouring down your face.")
    time.sleep(5)
    print(f"{Companion} says, 'Be careful. This place is known for its lava creatures'")
    time.sleep(5)
    print("You nod and start to explore the dungeon, searching for the key.")
    time.sleep(5)
    print("As you venture deeper, you come across a large underground chamber filled with lava.")
    time.sleep(5)
    print("In the center of the chamber, you see a small island with a pedestal on it.")
    time.sleep(5)
    print("On the pedestal, you can see a glowing red key.")
    time.sleep(5)
    print(f"You and {Companion} realize that this must be the third key you are looking for.")
    time.sleep(5)
    print(f"Before either of you could react, a giant beast emerges from the lava, its eyes glowing with a menacing light.")
    time.sleep(5)
    print("The beast is a massive fire phoenix, its body made of pure flame.")
    time.sleep(5)
    print("****************************\n"
          "  Flame The Beast of Fire \n"
          "****************************\n")
    print(Flame)
    time.sleep(5)
    dragonchoice1 = input("Before either of you could move, Flame strikes you both in the back, (Attack/Dodge): ")
    if dragonchoice1.lower() == "attack":
        print("Flame breathes fire at you, scorching your skin and leaving you in pain.")
        time.sleep(5)
        lower_health(20)
        print(f"{Companion}'s health is low")
        time.sleep(5)
        print(f"You and {Companion} are both injured and need to find a way to defeat Flame before it attacks again.")
        time.sleep(5)
        dragonchoice2 = input(f"You can either type 'Attack' to attack Flame or type 'Heal' to heal yourself and {Companion}: ")
        if dragonchoice2.lower() == "attack":
            print(f"You and {Companion} attack Flame with all your might, striking it with your weapons.")
            time.sleep(5)
            print("Flame roars in pain, but it is not defeated yet.")
            time.sleep(5)
            dragonchoicesemi2 = input(f"Type 'Attack' to attack Flame again or type 'Heal' to heal yourself and {Companion}: ")
            while True:
             if dragonchoicesemi2.lower() == "attack":
                print(f"You and {Companion} attack Flame with all your might.")
                time.sleep(5)
                print("Flame roars in pain, but it is not defeated yet.")
                time.sleep(5)
                print("You realize that you need to find a way to weaken it before you can defeat it.")
                time.sleep(5)
             elif dragonchoicesemi2.lower() == "heal":
                print(f"You use a healing potion to heal yourself and {Companion}.")
                increase_health(50)
                time.sleep(5)
                print(f"{Companion} is back in the fight!")
                time.sleep(5)
                print("You both attack Flame together, striking it with all your might.")
                time.sleep(5)
                print("Flame roars in pain, it's scales are starting to crack under your combined assault.")
                dragonchoicesemi3 = input(f"Type 'Attack' to attack Flame again or type 'Heal' to heal yourself and {Companion}: ")
                if dragonchoicesemi3.lower() == "attack":
                    print(f"You and {Companion} attack Flame's core with all your might, striking it with your weapons.")
                    time.sleep(5)
                    print("Flame roars in pain, and it crumbles to the ground, defeated.")
                    time.sleep(5)
                    print(f"You and {Companion} stand victorious, breathing heavily from the intense battle.")
                    time.sleep(5)
                    print("You search the dragon's remains and find a glowing red key that unlocks a hidden door in the dungeon.")
                    time.sleep(5)
                    print(f"You and {Companion} enter the hidden door, hoping to find the next key inside.")
                    time.sleep(5)
                    print("As you step through the door, you find yourselves in a dimly lit chamber filled with ancient artifacts.")
                    time.sleep(5)
                    print("In the center of the room, you see a pedestal with a glowing red key.")
                    time.sleep(5)
                    print("****************************\n"
                           "  3 Key Achieved 2 left. \n"
                          "****************************\n")
                    Chapter_4()
                    break
                elif dragonchoicesemi3.lower() == "heal":
                    print(f"You use a healing potion to heal yourself and {Companion}.")
                    time.sleep(5)
                    print(f"{Companion} is back in the fight!")
                    time.sleep(5)
                    print("Flame attacks you before you can attack again!")
                    time.sleep(5)
                    print(f"You and {Companion} are both injured and need to find a way to defeat Flame before it attacks again.")
                    lower_health(50)
                    time.sleep(5)
                    print(f"{Companion}'s health is low")
                    print("Try again")
                else:
                    print("Invalid choice. Flame attacks you again!")
                    Death()
                    return
             else:
                print("Invalid choice. Flame attacks you again!")
                Death()
                return
        elif dragonchoice2.lower() == "heal":
            print(f"You use a healing potion to heal yourself and {Companion}.")
            time.sleep(5)
            print(f"{Companion} is back in the fight!")
            time.sleep(5)
            print("You both attack Flame together, striking it with all your might.")
            time.sleep(5)
            print("Flame roars in pain, but it is not defeated yet.")
            time.sleep(5)
        else:
            print("Invalid choice. Flame attacks you again!")
            Death()
            return
    elif dragonchoice1.lower() == "dodge":
        print("You quickly dodge Flame's attack, narrowly avoiding its powerful strike.")
        time.sleep(5)
        print("You counterattack, striking Flame with all your might.")
        time.sleep(5)
        print(f"The dragon staggers back, but it is not defeated yet. You and {Companion} must work together to defeat it.")
        time.sleep(5)
        while True:
            dragonchoice2 = input(f"You can either type 'Attack' to attack Flame again or type 'Heal' to heal yourself and {Companion}: ")
            if dragonchoice2.lower() == "attack":
                print(f"You and {Companion} attack Flame with all your might.")
                time.sleep(5)
                print("Flame roars in pain, but it is not defeated yet.")
                time.sleep(5)
                print("You realize that you need to find a way to weaken it before you can defeat it.")
                break
            elif dragonchoice2.lower() == "heal":
                print(f"You use a healing potion to heal yourself and {Companion}.")
                increase_health(50)
                time.sleep(5)
                print(f"{Companion} is back in the fight!")
                time.sleep(5)
                print("You both attack Flame together, striking it with all your might.")
                time.sleep(5)
                print("Flame roars in pain, but it is not defeated yet.")
                time.sleep(5)
                break
            else:
                print("Invalid choice. Flame attacks you again!")
                Death()
                return
    else:
        print("Invalid choice. Flame attacks you again!")
        Death()
        return
   
def Chapter_9():
    global Companion, Username, health
    print('***************************\n'
    "Chapter 9: The Path to the Ice Dungeon\n"
          '***************************\n')
    time.sleep(2)
    print(f"You and {Companion} exit the fire dungeon and continue down the path, the heat giving way to a more relaxed meadow atmosphere.")
    time.sleep(5)
    print("You spot a small village in the distance, and you can decide to stop there to rest and gather supplies.")
    village_choice = input("Do you want to stop at the village? (Yes/No): ")
    if village_choice.lower() == "yes":
        print(f"You and {Companion} decide to stop at the village.")
        time.sleep(5)
        print("Before you you approach the villagers, you notice a small shop selling potions and supplies.")
        time.sleep(5)
        print("You decide to enter the shop and see what they have to offer.")
        time.sleep(5)
        print(f"{Companion} says, 'Hello, shopkeeper! Do you have any potions or supplies that could help us on our journey?'")
        time.sleep(5)
        print("The shopkeeper nods and shows you a selection of potions and supplies.")
        time.sleep(5)
        print("Maps, healing potions, and other useful items are available for purchase but one item catches your eye.")
        time.sleep(5)
        print("A dusty old map that seems to lead to the next dungeon.")
        time.sleep(5)
        print("You ask the shopkeeper about the map, and he tells you that it is a rare find, but he is willing to sell it to you for a fair price.")
        mapchoice = input(f"You can buy a map for 20 gold coins which {Companion} has offered to pay. Do you want to buy it? (Yes/No): ")
        if mapchoice.lower() == "yes":
            print(f"You buy the map and thank {Companion} for their help.")
        else:
            print("You decide not to buy the map and continue down the path without it.")
        time.sleep(5)
        print("As you enter the village, you are greeted by friendly villagers who offer you food and shelter.")
        time.sleep(5)
        print(f"{Companion} says, 'This is a nice place to rest and gather supplies before we continue our journey.'")
        time.sleep(5)
        print("You spend some time in the village, resting and preparing for the next part of your journey.")
        time.sleep(5)
        reset_health()
        print("You feel refreshed and ready to continue your journey.")
        time.sleep(5)
        print("You thank the villagers for their hospitality and prepare to leave the village.")
        time.sleep(5)
    elif village_choice.lower() == "no":
        print(f"You and {Companion} decide to continue down the path without stopping at the village.")
        time.sleep(5)
    else:
        print("Invalid choice. You continue down the path without stopping at the village.")
        time.sleep(5)
    
def Chapter_9Part2():
    global Companion, Username, health
    print("***************************\n"
     "Chapter 9 Part 2: The Journey Continues\n"
          "***************************\n")
    time.sleep(2)
    print(f"You and {Companion} follow the map's directions, navigating through the mountains.")
    time.sleep(5)
    print("After a long journey, you arrive at a crossroad.")
    time.sleep(5)
    print(f"{Companion} says, 'Where do we go now?'")
    crossroad_choice = input("Do you want to go left (snowy mountains) or right (icy cave)? (Left/Right): ")
    match crossroad_choice.lower().strip():
        case "left":
            print(f"You and {Companion} decide to go left towards the snowy mountains.")
            time.sleep(5)
            print("The temperature drops and you can see your breath in the cold air.")
            time.sleep(5)
            print(f"{Companion} says, 'We must be close to the ice dungeon.'")
            time.sleep(5)
            print("As you continue, the ground shakes and you are buried under a pile of snow.")
            Death()
        case "right":
            print(f"You and {Companion} decide to go right towards the icy cave.")
            time.sleep(5)
            print("Entering the cave, the temperature drops further and icicles hang from the ceiling.")
            time.sleep(5)
            print(f"{Companion} says, 'This must be the ice dungeon. We need to be careful.'")
            time.sleep(5)
            print("You explore the cave and find a locked underground chamber; you need a key to open it.")
            time.sleep(5)
            print(f"{Companion} says, 'We must find the key to unlock this door.'")
            time.sleep(5)
            print("Searching the chamber, you discover 2 small chests hidden behind a pile of ice.")
            time.sleep(5)
            frozen_cave = input("Do you want to open the left chest or the right chest? (Left/Right): ")
            match frozen_cave.lower().strip():
                case "left":
                    print("You open the left chest and find a shiny key inside!")
                    time.sleep(5)
                    print(f"{Companion} says, 'This must be the door key!'")
                    time.sleep(5)
                    print("You insert the key into the lock and the door creaks open, revealing the next part of the dungeon.")
                    time.sleep(5)
                    print(f"You and {Companion} step through, ready for further challenges.")
                    time.sleep(5)
                    print("An icicle hits you on the head, and you black out.")
                    time.sleep(5)
                    print("When you wake up, you're in a giant icy cavern and your companion is missing.")
                    time.sleep(5)
                    print("A rag in the corner moves, and a ghoulish creature emerges.")
                    time.sleep(5)
                    print("*****************************\n"
                              "Morjun the Ice Wraith\n"
                          "*****************************\n")
                    time.sleep(5)
                    print(Wraith)
                    time.sleep(5)
                    print("Morjun lunges at you, slashing with icy claws.")
                    time.sleep(5)
                    lower_health(20)
                    time.sleep(5)
                    print("Stumbling back, you notice a rusty sword nearby.")
                    time.sleep(5)
                    fightcavern = input("Do you want to pick up the sword and fight Morjun or try to escape the cavern? (Fight/Escape): ")
                    match fightcavern.lower().strip():
                        case "fight":
                            print("You pick up the sword and prepare to fight Morjun.")
                            time.sleep(5)
                            print("You dodge Morjun's attack and strike, hitting it in the side.")
                            time.sleep(5)
                            while True:
                                fightcavern2 = input("Do you want to attack again or heal yourself? (Attack/Heal): ")
                                match fightcavern2.lower().strip():
                                    case "attack":
                                        print("You attack Morjun with all your might, and it falls to the ground, defeated.")
                                        time.sleep(5)
                                        print(f"You search Morjun's remains and find a glowing ice key that unlocks a hidden door.")
                                        time.sleep(5)
                                        print(f"You free {Companion} from a nearby cage and carry them out of the cavern.")
                                        time.sleep(5)
                                        print("You step out into a dimly lit maze.")
                                        time.sleep(5)
                                        mazeorcavern = input("Would you like to explore the maze or return to the cavern? (Explore/Return): ")
                                        match mazeorcavern.lower().strip():
                                            case "explore":
                                                print(f"You and {Companion} decide to explore the maze for a way out.")
                                                time.sleep(5)
                                                mazechoice = input("Do you want to go left or right? (Left/Right): ")
                                                match mazechoice.lower().strip():
                                                    case "left":
                                                        print("You take the left path and find a small clearing.")
                                                        time.sleep(5)
                                                        print("In the clearing, a pedestal holds a glowing ice key.")
                                                        time.sleep(5)
                                                        print("****************************\n"
                                                                "4 Key Achieved 1 left.\n"
                                                              "****************************\n")
                                                        break
                                                    case "right":
                                                        print("You take the right path and end in a dead end. Go back!")
                                                        time.sleep(5)
                                                    case _:
                                                        print("Invalid choice. Returning to cavern.")
                                                        time.sleep(5)
                                                        return
                                                break
                                            case "return":
                                                print(f"You and {Companion} return to the cavern.")
                                                break
                                            case _:
                                                print("Invalid choice. Returning to cavern.")
                                                time.sleep(5)
                                                return
                                        break
                                    case "heal":
                                        print(f"You use a healing potion to heal yourself.")
                                        time.sleep(5)
                                        increase_health(50)
                                    case _:
                                        print("Invalid choice.")
                                        break
                        case "right":
                            print("You open the right chest and find a pile of gold coins.")
                            time.sleep(5)
                            print(f"{Companion} says, 'Nice find, but we still need the key.'")
                            time.sleep(5)
                        case _:
                            print("Invalid choice. Continuing down without a decision.")
                            time.sleep(5)
                            return
                case _:
                    print("Invalid choice. Continuing down the path.")
                    time.sleep(5)
                    return
        case _:
            print("Invalid choice. Returning to previous state.")
            time.sleep(5)
            return


def Chapter_10():
    global Companion, Username, health
    print("***************************\n"
    "Chapter 10: The Path to the Final Dungeon\n"
          "***************************\n")
    print(f"You and {Companion} exit the ice dungeon and continue down the path, the icy terrain giving way to rocky cliffs.")
    time.sleep(5)
    print("The air grows colder, and you can see your breath in the frigid air.")
    time.sleep(5)
    print(f"{Companion} says, 'The final key is said to be hidden in a dark dungeon, deep within the mountains according to the map.'")
    time.sleep(5)
    print("You nod in agreement, determined to find the final key and rescue the princess.")
    time.sleep(5)
    print("As you continue down the path, you come across a group of trolls blocking your way.")
    time.sleep(5)
    print("The trolls are armed with large clubs and look ready for a fight.")
    time.sleep(5)
    print(f"{Companion} whispers, 'We need to be careful. The trolls are known for their brute strength and cunning traps.'")
    time.sleep(5)
    trollchoice3 = input("Do you want to fight the trolls or try to reason with them? (Fight/Reason): ")
    if trollchoice3.lower() == "fight":
        print(f"You and {Companion} charge at the trolls, weapons drawn.")
        time.sleep(5)
        print(f"The trolls fight back fiercely, but you and {Companion} are able to defeat them after a tough battle.")
        time.sleep(5)
        print("You search the trolls' remains and find a map that leads to the final dungeon.")
        time.sleep(5)
        print(f"You and {Companion} take the map and prepare to continue your journey.")
        time.sleep(5)
    elif trollchoice3.lower() == "reason":
        print("You try to reason with the trolls, explaining that you mean no harm and are only looking for the final key.")
        time.sleep(5)
        print("The trolls listen to your words, but they are still wary of you.")
        time.sleep(5)
        print(f"{Companion} suggests that you offer them something in exchange for safe passage.")
        time.sleep(5)
        offer = input("Do you want to offer them some of your supplies? (Yes/No): ")
        while True:
         if offer.lower() == "yes":
            print("You offer the trolls some of your supplies, and they accept your offer.")
            time.sleep(5)
            print(f"The trolls allow you and {Companion} to pass safely, and you continue on your journey.")
         elif offer.lower() == "no":
            print("The trolls refuse to let you pass without a fight.")
            time.sleep(5)
            print(f"You and {Companion} are forced to fight the trolls, but you are able to defeat them after a tough battle.")
            time.sleep(5)
            print("You search the trolls' sacks and find a map that leads to the final dungeon.")
            time.sleep(5)
            print(f"You and {Companion} take the map and prepare to continue your journey.")
            time.sleep(5)
         else:
            print("Invalid choice. You continue down the path without making a decision.")
            time.sleep(5)
            return

def Chapter_11():
    print("***************************\n"
          "Chapter 11: The Final Dungeon\n"
          "***************************\n")
    global Companion, Username, health
    print(f"You and {Companion} arrive at the entrance of the final dungeon, a dark cave filled with ominous shadows.")
    time.sleep(5)
    print("The air is thick with tension, and you can feel the weight of the final challenge ahead.")
    time.sleep(5)
    print(f"{Companion} says, 'This is it. The final key is said to be hidden in this dungeon, guarded by a powerful monster.'")
    time.sleep(5)
    print("You nod, determined to find the final key and rescue the princess.")
    time.sleep(5)
    print("As you venture deeper into the dungeon, you come across a large underground chamber filled with darkness.")
    time.sleep(5)
    print("In the center of the chamber, you see a pedestal with a glowing black key.")
    time.sleep(5)
    print("But before you can approach the pedestal, a massive shadowy figure emerges from the darkness.")
    time.sleep(5)
    print("The figure is a giant shadow beast, its eyes glowing with a menacing light.")
    time.sleep(5)
    print("****************************\n"
            "  Desbio the Dark Beast \n"
          "****************************\n")
    time.sleep(5)
    print(Desbio)
    time.sleep(5)
    beastchoice1 = input("Before either of you could move, Desbio strikes you both in the back, (Attack/Dodge): ")
    if beastchoice1.lower() == "attack":
        print("Desbio lunges at you, its claws slashing through the air.")
        time.sleep(5)
        lower_health(20)
        print(f"{Companion}'s health is low")
        time.sleep(5)
        print(f"You and {Companion} are both injured and need to find a way to defeat Desbio before it attacks again.")
        time.sleep(5)
        beastchoice2 = input(f"You can either type 'Attack' to attack Desbio or type 'Heal' to heal yourself and {Companion}: ")
        if beastchoice2.lower() == "attack":
            print(f"You and {Companion} attack Desbio with all your might, striking it with your weapons.")
            time.sleep(5)
            print("Desbio roars in pain, but it is not defeated yet.")
            time.sleep(5)
            beastchoicesemi2 = input(f"Type 'Attack' to attack Desbio again or type 'Heal' to heal yourself and {Companion}: ")
            while True:
             if beastchoicesemi2.lower() == "attack":
                print(f"You and {Companion} attack Desbio with all your might.")
                time.sleep(5)
                print("Desbio roars in pain, but it is not defeated yet.")
                time.sleep(5)
                print("You realize that you need to find a way to weaken it before you can defeat it.")
                time.sleep(5)
             elif beastchoicesemi2.lower() == "heal":
                print(f"You use a healing potion to heal yourself and {Companion}.")
                increase_health(50)
                time.sleep(5)
                print(f"{Companion} is back in the fight!")
                time.sleep(5)
                print("You both attack Desbio together, striking it with all your might.")
                time.sleep(5)
                print("Desbio roars in pain, it's scales are starting to crack under your combined assault.")
                beastchoicesemi3 = input(f"Type 'Attack' to attack Desbio again or type 'Heal' to heal yourself and {Companion}: ")
                if beastchoicesemi3.lower() == "attack":
                    print(f"You and {Companion} attack Desbio's core with all your might, striking it with your weapons.")
                    time.sleep(5)
                    print("Desbio roars in pain, and it crumbles to the ground, defeated.")
                    time.sleep(5)
                    print(f"You and {Companion} stand victorious, breathing heavily from the intense battle.")
                    time.sleep(5)
                    print("You search the beast's remains and find a glowing black key that unlocks a hidden door in the dungeon.")
                    time.sleep(5)
                    print(f"You and {Companion} enter the hidden door, hoping to find the princess inside.")
                    time.sleep(5)
                    print("As you step through the door, you find yourselves in a dimly lit chamber filled with ancient artifacts.")
                    time.sleep(5)
                    print("In the center of the room, you see a pedestal with a glowing black key.")
                    time.sleep(5)
                    print("****************************\n"
                          "  5 Keys Achieved None left. \n"
                          "****************************\n")
                    print("You take the key and prepare to rescue the princess.")

def Chapter_12():
    global Companion, Username, health
    print("" 
          "***************************\n"
      "Chapter 12: The Calm Before The Storm"
          "***************************\n")
    time.sleep(2)
    print(f"You and {Companion} continue down the path, now with no clue where to go...")
    time.sleep(5)
    print(f"{Companion} says, I've heard rumours of the final beast that captured the princess, but never the location...")
    time.sleep(5)
    print("We may need to camp near a village for a few days as I try to gather some info, I'm also quite tired...")
    time.sleep(5)
    print(f"Wait {Username}!, I see another village over the in the horizon. Let's go!")
    time.sleep(5)
    print(f"You and {Companion} approach the village, but it looks off...")
    time.sleep(5)
    print("There were no villagers in sight, it was abandoned quite a few months ago by the looks of it...")
    time.sleep(5)
    MajorChoice = input("Would you like to stay or leave to find another village? (Stay/Leave): ")
    if MajorChoice.lower() == "stay":
        print(f"Ok, {Username} let's stay, we can gather info later! Says {Companion}")
    else:
        print("Ok, let's go, I'm kinda tired though...")
        time.sleep(5)
        print("You both travel along the path and reach a river...")
        time.sleep(5)
        print("You have no choice but to go back towards the village.")
        time.sleep(5)
        print(f"You arrived back at the village and sat down")
        Chapter_12Part2()
        time.sleep(5)
    
def Chapter_12Part2():
    global Companion,Username, health
    print(f"{Companion} approaches one of the abandoned houses and pulls out some goods")
    print(f"You set up the fire! Yells {Companion}")
    print("You oblige and went to go get firewood nearby")
    stick1 = input("Under a tree you find a piece. Type 'One' to pick up: ")
    if stick1.lower() == "one":
        print("Collected")
    else:
        print("Not collected")
    stick2 = input("Under a piece of bark you find a piece. Type 'Two' to pick up: ")
    if stick2.lower() == "two":
        print("Collected")
    else:
        print("Not collected")
    stick3 = input("Near the camp you find a piece. Type 'Three' to pick up: ")
    if stick3.lower() == "three":
        print("Collected")
    else:
        print("Not collected")
    stick4 = input("Near a tree you find a piece. Type 'Four' to pick up: ")
    if stick4.lower() == "four":
        print("Collected")
    else:
        print("Not collected")
    stick5 = input("Under a leaf you find a piece. Type 'Five' to pick up: ")
    if stick5.lower() == "five":
        print("Collected all 5")
    else:
        print("Not collected")
    print("You return to the camp carrying all the wood...")
    time.sleep(5)
    print(f"{Companion} appears around a corner carrying a stack of books and yells at you")
    time.sleep(5)
    print(f"Come here {Username}, says {Companion}")
    time.sleep(5)
    print("We found another clue, I believe the final creature could be dungeon somewhere underneath Fargon, potentially underneath the Capital ")
    time.sleep(5)
    print("The Capital? You ask")
    time.sleep(5)
    print("Yeah, according to this book, there's a capital located somewhere around here...")
    time.sleep(5)
    print("It's guarded by a forcefield, with 5 ancient machines guarding it")
    time.sleep(5)
    print("We should go find it, huh? Sounds like the princess could be located there!")
    time.sleep(5)
    print(f"You and {Companion} rest the night and leave tomorrow")
    time.sleep(5)
    print(f"You and {Companion} sleep the night")
    time.sleep(10)
    reset_health()
    
def Chapter_13():
    global Companion, health, Username
    print("***************************\n"
            "Chapter 13: The Capital"
          "***************************\n")
    time.sleep(2)
    print(f"You and {Companion} set off from the abandoned village...")
    time.sleep(5)
    print(f"Towards where {Companion} thinks where the capital is...")
    time.sleep(5)
    print(f"You and {Companion} walk for days")
    time.sleep(6)
    reset_health()
    print(f"{Companion} looks around, and says 'We should be here'")
    time.sleep(5)
    print("What, you reply, there's nothing here")
    time.sleep(5)
    print("All of a sudden, the ground beneath began to shake and split open")
    time.sleep(5)
    print(f"You and {Companion} drop into the cavern below")
    time.sleep(5)
    lower_health
    time.sleep(5)
    print(f"You and {Companion} faint")
    time.sleep(10)
    print("When you wake up you notice, that companion disappeared. In front of you is 5 tunnels")
    while True:
     tunnelchoice = int(input("Which tunnel would you proceed down: "))
     match tunnelchoice:
        case 1:
            print("You walk into the darkness of the tunnel...")
            time.sleep(5)
            print("You reach a dead end...")
            time.sleep(5)
            print("All of a sudden a skeleton attacks you from behind...")
            time.sleep(5)
            Death()
            break
        case 2:
            print("You walk into the darkness of the tunnel...")
            time.sleep(5)
            print("In the end, you reach a fountain...")
            time.sleep(5)
            print("Your deadly thirsty and drank from the fountain...")
            time.sleep(5)
            print("The fountain water was poisoned.")
            Death()
            break
        case 3:
            print("You walk into the darkness of the tunnel...")
            time.sleep(5)
            print(f"You notice, a shadow up ahead, it could be {Companion}...")
            time.sleep(5)
            print("You run towards the shadow...")
            time.sleep(5)
            print("You walk right past the shadow...")
            time.sleep(5)
            print(f"You arrive back at the village, alone, with no {Companion} in sight...")
            time.sleep(5)
            print("You died of loneliness and despair")
            time.sleep(5)
            Death()
            break
        case 4:
            print("You walk into the darkness of the tunnel...")
            time.sleep(5)
            print(f"You notice a shadow up ahead, it could be {Companion}...")
            time.sleep(5)
            print(f"Hey, come {Username}! {Companion} yells")
        case 5:
            print("You walk into the darkness of the tunnel...")
            time.sleep(5)
        case _:
            print("Enter a valid number")
            return




    

    
    
if __name__ == "__main__":
 main()
