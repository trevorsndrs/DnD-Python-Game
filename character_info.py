import random

def get_class_skills(character_class):
  class_skills = {
    "Barbarian": ["Rage", "Unarmored Defense"],
    "Bard": ["Bardic Inspiration", "Spellcasting"],
    "Cleric": ["Divine Domain", "Spellcasting"],
    "Druid": ["Wild Shape", "Druidic"],
    "Fighter": ["Fighting Style", "Second Wind"],
    "Monk": ["Unarmored Defense", "Martial Arts"],
    "Paladin": ["Divine Sense", "Lay on Hands"],
    "Ranger": ["Favored Enemy", "Natural Explorers"],
    "Rogue": ["Expertise", "Sneak Attack"],
    "Sorcerer": ["Sorcerous Origin," "Spellcasting"],
    "Warlock": ["Otherworldly Patron", "Pact Magic"],
    "Wizard": ["Arcane Recovery", "Spellcasting"]
  }
  return class_skills.get(character_class, [])

def get_race_skills(character_race):
  race_skills = {
    "Dragonborn": ["Breath Weapon", "Damage Resistance"],
    "Dwarf": ["Dwarven Resilience", "Stonecunning"],
    "Elf": ["Darkvision", "Keen Senses"],
    "Gnome": ["Gnome Cunning", "Artificer's Lore"],
    "Half-Elf": ["Fey Ancestry", "Skill Versatility"],
    "Half-Orc": ["Relentless Endurance", "Savage Attacks"],
    "Halfling": ["Lucky", "Brave"],
    "Human": ["Versatility, Bonus Feat"],
    "Tiefling": ["Darkvision", "Hellish Resistance"]
  }
  return race_skills.get(character_race, [])

  ############################################################################

def roll_hitpoints(hit_dice):
    """
    Rolls hit points based on the provided hit dice.
    """
    return random.randint(1, hit_dice)

def calculate_health(con_modifier, hit_dice):
    """
    Calculates the character's health based on the constitution modifier and hit dice.
    """
    return roll_hitpoints(hit_dice) + con_modifier
  
def get_hit_dice(character_class):
  class_hit_dice = {
      "Fighter": 10,
      "Wizard": 6,
    }
  default_hit_dice = 8
  return class_hit_dice.get(character_class, default_hit_dice)