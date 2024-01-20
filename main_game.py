import os
import random
import character_info
import starting_equipment

# PLAYER ATTRIBUTES #####################################################
name = ""
character_class = ""
character_race = ""
level = 1
experience_points = 0
con_modifier = 0
inventory = ""

# VALID D&D CLASSES AND RACES ############################################
valid_classes = ["Fighter", "Rogue", "Wizard", "Warlock", "Paladin", "Ranger", "Bard", "Barbarian", "Druid", "Cleric", "Sorcerer", "Monk"]
valid_races = ["Human", "Elf", "Dwarf", "Half-Orc", "Halfling", "Tiefling", "Half-Elf", "Gnome", "Dragonborn"]
# If you wish to change these out for different races or classes make sure to do so in the character_info.py file as well! 


# MAIN MENU ##############################################################
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("#####  #   #  #####   ###   #####")
    print("#   #  #   #  #      #   #    #  ")
    print("#   #  #   #  #      #        #  ")
    print("#   #  #   #  #####   ###     #  ")
    print("#   #  #   #  #          #    #  ")
    print("#  #   #   #  #      #   #    #  ")
    print("### #  #####  #####   ###     #  ")
    print("")
    print("Start Game?")
    print("y/n")

    while True:
        user_input = input().lower()
        if user_input == "y":
            character_creation()
            break
        elif user_input == "n":
            print("You have chosen to forgo your adventure. Coward.")
            break
        else:
            print("I do not recognize that command.")

# CHARACTER CREATION ##################################################
def get_modifier(score):
    return (score - 10) // 2

def character_creation():
    global name, character_class, character_race, level, experience_points, con_modifier, valid_classes, valid_races

    clear_screen()

    name = input("Enter your character's name: ")

    while True:
        clear_screen()
        character_class = input("""
    ꧁ ঔৣ ☬Choose your class☬ঔৣ꧂
    ═════════⊹⊱≼≽⊰⊹═════════
            Barbarian ☠︎︎
            Bard 𓏢
            Cleric ✞
            Druid ⚚
            Fighter ⚔︎
            Monk ☾☼
            Paladin ⛉
            Ranger જ⁀➴
            Rogue 🗡
            Sorcerer 🕯
            Warlock 🕸
            Wizard ✧˖°
    ═════════⊹⊱≼≽⊰⊹═════════ 
    """)
        print("")
        if character_class in valid_classes:
            break
        else:
            print("Invalid class.")

    while True:
        clear_screen()
        character_race = input("""
    ꧁ ঔৣ ☬Choose your race☬ঔৣ꧂
    ═════════⊹⊱≼≽⊰⊹═════════
            Dragonborn
            Dwarf
            Elf
            Gnome
            Half-Elf
            Half-Orc
            Halfling
            Human
            Tiefling
    ═════════⊹⊱≼≽⊰⊹═════════
    """)
        print("")
  
        if character_race in valid_races:
            break
        else:
            print("Invalid race.")

    while True:
        clear_screen()
        print(f"\nName: {name}")
        print(f"Character race: {character_race}")
        print(f"Character class: {character_class}")
        print("")
        character_confirm = input("Does everything look good? (y/n)").lower()
        if character_confirm == "y":
            roll_for_stats()
            break
        elif character_confirm == "n":
            continue
        else:
            print("Invalid input, please use 'y' for yes or 'n' for no.")

def roll_for_stats():
    global strength, dexterity, constitution, intelligence, wisdom, charisma, con_modifier
    while True:
        clear_screen()
        print("Let's roll for your stats!\n")
        stats = roll_stats()
        strength, dexterity, constitution, intelligence, wisdom, charisma = stats
        modifiers = {
            "strength": get_modifier(strength),
            "dexterity": get_modifier(dexterity),
            "constitution": get_modifier(constitution),
            "intelligence": get_modifier(intelligence),
            "wisdom": get_modifier(wisdom),
            "charisma": get_modifier(charisma),
        }
        print("Stats with Modifiers:")
        print(f"Strength: {strength} (Mod: {modifiers['strength']})")
        print(f"Dexterity: {dexterity} (Mod: {modifiers['dexterity']})")
        print(f"Constitution: {constitution} (Mod: {modifiers['constitution']})")
        print(f"Intelligence: {intelligence} (Mod: {modifiers['intelligence']})")
        print(f"Wisdom: {wisdom} (Mod: {modifiers['wisdom']})")
        print(f"Charisma: {charisma} (Mod: {modifiers['charisma']})")
        print("")
        confirmation = input("\nDoes everything look good? (y/n)").lower()
        if confirmation == "y":
            con_modifier = get_modifier(constitution)
            display_character_sheet()
            break
        elif confirmation != "n":
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        

def roll_stats():
    return [random.randint(3, 18) for _ in range(6)]

# EXPERIENCE POINTS #################################################
def gain_experience(points):
    experience_points += points
    print(f"{name} gained {points} experience points!")
    if experience_points >= 100 * level:
        level += 1
        print(f"{name} leveled up to level {level}!")

# FULL CHARACTER SHEET #############################################
def display_character_sheet():
    clear_screen()
    hit_dice = character_info.get_hit_dice(character_class)
    health = character_info.calculate_health(hit_dice, get_modifier(constitution))
    class_skills = character_info.get_class_skills(character_class)
    race_skills = character_info.get_race_skills(character_race)

    print(f"\n[NAME: {name}]    [LEVEL: {level} ]    [CLASS: {character_class}]    [RACE: {character_race}]\n")
    print(f"\n[HEALTH: {health}] [ARMOR CLASS: ]\n")
    print("⊰⊹════════════════════════⊹⊱≼≽⊰⊹════════════════════════⊹⊱")
    print("Stats:")
    print(f"Strength: {strength} (Mod: {get_modifier(strength)})")
    print(f"Dexterity: {dexterity} (Mod: {get_modifier(dexterity)})")
    print(f"Constitution: {constitution} (Mod: {get_modifier(constitution)})")
    print(f"Intelligence: {intelligence} (Mod: {get_modifier(intelligence)})")
    print(f"Wisdom: {wisdom} (Mod: {get_modifier(wisdom)})")
    print(f"Charisma: {charisma} (Mod: {get_modifier(charisma)})")
    print("")
    print("⊰⊹════════════════════════⊹⊱≼≽⊰⊹════════════════════════⊹⊱")
    print(f"{character_class} Class Skills: {', '.join(class_skills)}")
    print(f"{character_race} Racial Abilities: {', '.join(race_skills)}")
    print("")
    print("⊰⊹════════════════════════⊹⊱≼≽⊰⊹════════════════════════⊹⊱")
    print(f"Your inventory contains: {', '.join(inventory)}")
    print("")

# ACT_ONE #########################################################
def level_one():
    clear_screen()
    print("""
    ______________________________
      .     ✦       .       o
     ˚       *  .     ˚   *    
    ✦  .   . ˚      . ✦     ★⋆.
    . ˚    *       .      ✦    ˚
    ______________________________
    A C T  I: A W A K E N I N G 
    ______________________________
    """)
    print("")
    print("Sample Text Here ")

def level_two():
    clear_screen()
    print("You find yourself face to face with a rusted iron door.")

# Start the game
main_menu()
