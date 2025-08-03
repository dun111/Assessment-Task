"""
All functions used throughout the game
"""
import json
import random
import ascii_art
from chapters import CHAPTERS

GAME_STATE = {
      "PLAYER": None,
      "USERNAME": "",
      "COMPANION": "",
      "CURRENT_CHAPTER": ""
}

SAVE_FILE = "TalesOfTime.json"

def save_game():
    """
    Used to save game data to a json file
    """
    data = {
        "PLAYER": GAME_STATE["PLAYER"],
        "USERNAME": GAME_STATE["USERNAME"],
        "COMPANION": GAME_STATE["COMPANION"],
        "CURRENT_CHAPTER": GAME_STATE["CURRENT_CHAPTER"]
    }
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("Waypoint set!")

def load_game(chapters, fallback):
    """
    Used to extract data from the Json file and load the last saved chapter
    """
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            GAME_STATE["PLAYER"] = data["PLAYER"]
            GAME_STATE["USERNAME"] = data["USERNAME"]
            GAME_STATE["COMPANION"] = data["COMPANION"]
            GAME_STATE["CURRENT_CHAPTER"] = data.get(["CURRENT_CHAPTER"], "main")
        print("Waypoint loaded!")
        # Resumes at the correct chapter
        chapters[GAME_STATE["CURRENT_CHAPTER"]]()
    except FileNotFoundError:
        print("No saved waypoint found.")
        fallback()
        return
#This loads the json file data and if there is an error will show No saved waypoint


def resume_game():
    """
    Resumes the game based on the current chapter.
    Falls back to main if chapter is invalid.
    """
    chapter = GAME_STATE.get("CURRENT_CHAPTER", "main")
    CHAPTERS.get(chapter, CHAPTERS["main"]())()


# This function is used to go back to the GAME_STATE["PLAYER"]'s
# chapter when the game saved by saving the current chapter
# into the variable CURRENT_CHAPTER


def decrease_health(amount=None):
    """
    Used to decrease the player's health.
    If amount is not provided, it will randomly choose a value between 10 and 80.
    """
    player = GAME_STATE.get("PLAYER")
    if not isinstance(player, dict):
        print("Error: PLAYER not initialized or invalid.")
        death()
        return
    if amount is None:
        amount = random.randint(10, 80)
    reduced = max(1, amount - player.get("defence", 0) // 3)
    player["health"] -= reduced
    print(f"You took {reduced} damage! (Reduced by defence) Your health is now {player['health']}.")
    if player["health"] <= 0:
        print("You have died...")
        death()
    elif player["health"] <= 10:
        print("Low Health!")

def increase_health(amount):
    """
    Used to increase the player's health.
    """
    player = GAME_STATE.get("PLAYER")
    if not isinstance(player, dict):
        print("Error: PLAYER not initialized or invalid.")
        death()
        return
    player["health"] += amount
    print(f"Your health is now {player['health']}")

def reset_health():
    """
    Used to reset the player's health.
    """
    player = GAME_STATE.get("PLAYER")
    if not isinstance(player, dict):
        print("Error: PLAYER not initialized or invalid.")
        death()
        return
    player["health"] = 100
    print("Your health has been reset to 100.")


def playerdata(name):
    """
    The player's data for their stats by default
    """
    return {"name": name,
            "health": 100,
            "gold": 200,
            "strength": 20,
            "defence": 20,
            "luck": 20,}
#This function shows the GAME_STATE["PLAYER"]'s stats. Still in work


def decrease_gold(amount):
    """
    Used to decrease the player's gold.
    """
    player = GAME_STATE.get("PLAYER")
    if not isinstance(player, dict):
        print("Error: PLAYER not initialized or invalid.")
        death()
        return

    player["gold"] -= amount
    print(f"You spent {amount} gold. Your gold is now {player['gold']}.")

#This function lowers the PLAYERs gold

def increase_gold(amount):
    """
    Used to increase the player's gold.
    """
    player = GAME_STATE.get("PLAYER")
    if not isinstance(player, dict):
        print("Error: PLAYER not initialized or invalid.")
        death()
        return
    player["gold"] += amount
    print(f"You gained {amount} gold. Your gold is now {player['gold']}.")

def death():
    """
    Used to kill the player then prompt them to restart or exit the game
    """
    print("You have died. Game over.")
    input()
    print("Do you want to restart the game? (Yes/No): ")
    choice = input().strip().strip().lower()
    if choice == "yes":
        restart()
    elif choice == "no":
        print("Thank you for playing!")
        exit()
    else:
        print("Bye! Exiting the game.")
        exit()
#This function manages the death sequence

def restart():
    """
    Used to restart the game and go to main
    """
    print("restarting the game...")
    GAME_STATE["USERNAME"] = ""
    GAME_STATE["PLAYER"] = None
    GAME_STATE["COMPANION"] = ""
    CHAPTERS["main"]()
#This function restarts the game

def dark_sword_story():
    """
    Used to upgrade sword and to show backstory
    """
    print("Before you leave, you notice a bottle of ominous energy.")
    input()
    print("Suddenly your sword flies out your hand and forges with the ominous energy")
    input()
    print("'You have acquired 'The Corrupted Sword'")
    input()
    print(ascii_art.DARK_SWORD)
    learn_more2 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more2.strip().lower().strip():
        case "yes":
            print("This sword, now corrupted by dark energy. " \
                  "Has increased sharpness and toughness allowing " \
                  "it attack against even the strongest of enemies.")
            input()
            CHAPTERS["chapter_10"]()
            return
        case "no":
            print("Ok, skipping backstory")
            input()
            CHAPTERS["chapter_10"]()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_sword_story()
            return
#This is for the upgrade of the sword


def dark_shield_story():
    """
    Used to upgrade shield and to show backstory
    """
    print("Before you leave, you notice a bottle of ominous energy.")
    input()
    print("Suddenly your shield flies out your hand and forges with the ominous energy")
    input()
    print("'You have acquired 'The Dark Shield'")
    input()
    print(ascii_art.DARK_SHIELD)
    learn_more3 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more3.strip().lower().strip():
        case "yes":
            print("This shield, now corrupted by dark energy. " \
                  "Has increased defence and toughness allowing it defend " \
                  "against even the strongest of enemies.")
            input()
            CHAPTERS["chapter_12"]()
            return
        case "no":
            print("Ok, skipping backstory")
            input()
            CHAPTERS["chapter_12"]()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_shield_story()
            return
#This is for the upgrade of the shield

def dark_dagger_story():
    """
    Used to upgrade dagger and to show backstory
    """
    print("Before you leave, you notice a bottle of ominous energy.")
    input()
    print("Suddenly your Dagger flies out your hand and forges with the ominous energy")
    input()
    print("'You have acquired 'The Dark Dagger'")
    input()
    print(ascii_art.DARK_SHIELD)
    learn_more3 = input("Would you like to hear about the backstory of this weapon (Yes/No)?")
    match learn_more3.strip().lower().strip():
        case "yes":
            print("This dagger, now corrupted by dark energy. " \
                  "Has increased sharpness and power allowing it attack " \
                  "against even the strongest of enemies.")
            input()
            CHAPTERS["chapter_7"]()
            return
        case "no":
            print("Ok, skipping backstory")
            input()
            CHAPTERS["chapter_7"]()
            return
        case _:
            print("Invalid Option")
            print("Try Again")
            dark_dagger_story()
            return
#This is for the upgrade of the shield
