import random as rnd

class_list = [
    "Warrior",
    "Hunter",
    "Mage",
    "Rogue",
    "Priest",
    "Warlock",
    "Paladin",
    "Druid",
    "Shaman",
    "Monk",
    "Demon Hunter",
    "Death Knight",
    "Evoker",
]

race_list = [
    [ # warrior
        "orc", "undead", "tauren", "troll", "blood elf", "goblin",
        "nightborne", "highmountain tauren", "mag'nar orc", "zandalari troll",
        "vulpera", "pandaren (horde)", "pandaren (alliance)", "human", "dwarf",
        "night elf", "gnome", "draenei", "worgen", "void elf", "lightforged draenei",
        "dark iron dwarf", "kul tiran", "mechagnome"
    ],
    [ # hunter
        "Orc", "Undead", "Tauren", "Troll", "Blood elf", "Goblin",
        "Nightborne", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll",
        "Vulpera", "Pandaren(Horde)", "Pandaren(Alliance)", "Human", "Dwarf",
        "Night Elf", "Gnome", "Draenei", "Worgen", "Void Elf", "Lightforged Draenei",
        "Dark Iron Dwarf", "Kul Tiran", "Mechagnome"
    ],
    [ # mage
        "Orc", "Undead", "Tauren", "Troll", "Blood elf", "Goblin",
        "Nightborne", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll",
        "Vulpera", "Pandaren(Horde)", "Pandaren(Alliance)", "Human", "Dwarf",
        "Night Elf", "Gnome", "Draenei", "Worgen", "Void Elf", "Lightforged Draenei",
        "Dark Iron Dwarf", "Kul Tiran", "Mechagnome"
    ],
    [ # rogue
        "Orc", "Undead", "Tauren", "Troll", "Blood elf", "Goblin",
        "Nightborne", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll",
        "Vulpera", "Pandaren(Horde)", "Pandaren(Alliance)", "Human", "Dwarf",
        "Night Elf", "Gnome", "Draenei", "Worgen", "Void Elf", "Lightforged Draenei",
        "Dark Iron Dwarf", "Kul Tiran", "Mechagnome"
    ],
    [ # priest
        "Orc", "Undead", "Tauren", "Troll", "Blood elf", "Goblin",
        "Nightborne", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll",
        "Vulpera", "Pandaren(Horde)", "Pandaren(Alliance)", "Human", "Dwarf",
        "Night Elf", "Gnome", "Draenei", "Worgen", "Void Elf", "Lightforged Draenei",
        "Dark Iron Dwarf", "Kul Tiran", "Mechagnome"
    ],
    [ # warlock
        "Orc", "Undead", "Troll", "Blood Elf", "Goblin", "Nightborne", "Vulpera",
        "Human", "Dwarf", "Gnome", "Worgen", "Void Elf", "Dark Iron Dwarf","Mechagnome",
        "Orc", "Undead", "Troll", "Blood Elf", "Goblin", 
        "Human", "Dwarf", "Gnome", "Worgen", "Void Elf", 
    ],
    [ # paladin
        "Highmountain Tauren", "Blood Elf", "Zandalari Troll",
        "Human", "Dwarf", "Draenei", "Lightforged Draenei", "Dark Iron Dwarf", "Highmountain Tauren", "Blood Elf", "Zandalari Troll",
        "Human", "Dwarf", "Draenei", "Lightforged Draenei", "Dark Iron Dwarf", "Highmountain Tauren", "Blood Elf", "Zandalari Troll",
        "Human", "Dwarf", "Draenei", "Lightforged Draenei", "Dark Iron Dwarf"
    ],
    [ # druid
        "Tauren", "Troll", "Highmountain Tauren", "Zandalari Troll",
        "Night Elf", "Worgen", "Kul Tiran", "Tauren", "Troll", "Highmountain Tauren", "Zandalari Troll",
        "Night Elf", "Worgen", "Kul Tiran", "Tauren", "Troll", "Highmountain Tauren", "Zandalari Troll",
        "Night Elf", "Worgen", "Kul Tiran", "Tauren", "Troll", "Highmountain Tauren"
    ],
    [ # shaman
        "Orc", "Tauren", "Troll", "Goblin", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll", "Vulpera","Pandaren(Horde)",
        "Dwarf", "Draenei", "Dark Iron Dwarf", "Kul Tiran","Orc", "Tauren", "Troll", "Goblin", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll",
        "Vulpera","Pandaren(Horde)", "Dwarf", "Draenei"
        
    ],
    [ # monk
        "Orc", "Undead", "Tauren", "Troll", "Blood elf",
        "Nightborne", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll", "Orc",
        "Vulpera", "Pandaren(Horde)", "Pandaren(Alliance)", "Human", "Dwarf",
        "Night Elf", "Gnome", "Draenei", "Void Elf", "Dark Iron Dwarf", "Kul Tiran", "Mechagnome","Kul Tiran","Mechagnome"
    ],
    [ # demon hunter
        "Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", "Night Elf",
        "Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", "Night Elf","Blood Elf", 'Night Elf'
    ],
    [ # death knight
        "Orc", "Undead", "Tauren", "Troll", "Blood Elf", "Goblin",
        "Nightborne", "Highmountain Tauren", "Mag'nar Orc", "Zandalari Troll",
        "Vulpera", "Pandaren(Horde)", "Pandaren(Alliance)", "Human", "Dwarf",
        "Night Elf", "Gnome", "Draenei", "Worgen", "Void Elf", "Lightforged Braenei",
        "Dark Iron Dwarf", "Kul Tiran", "Mechagnome"
    ],
    [ # evoker
        "Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)",
        "Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)",
        "Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthyr(Horde)", "Dracthyr(Alliance)","Dracthry(Horde)", "Dracthyr(Alliance)","Dracthry(Horde)"
    ]
]
spec_list = [
    
        [ # warrior
            "Arms", "Fury", "Protection","Arms", "Fury", "Protection","Arms", "Fury", "Protection","Arms", "Fury", "Protection"
        ],
        [ # hunter
            "Marksmanship", "Beast Mastery", "Survival","Marksmanship", "Beast Mastery", "Survival","Marksmanship", "Beast Mastery", "Survival","Marksmanship", "Beast Mastery", "Survival"
        ],
        [ # mage
            "Arcane", "Frost", "Fire","Arcane", "Frost", "Fire","Arcane", "Frost", "Fire","Arcane", "Frost", "Fire"
        ],
        [ # rogue
            "Assassination", "Outlaw", "Sublety","Assassination", "Outlaw", "Sublety","Assassination", "Outlaw", "Sublety","Assassination", "Outlaw", "Sublety"
        ],
        [ # priest
            "Discipline", "Holy", "Shadow","Discipline", "Holy", "Shadow","Discipline", "Holy", "Shadow","Discipline", "Holy", "Shadow"
        ],
        [ # warlock
            "Affliction", "Destruction", "Demonology","Affliction", "Destruction", "Demonology","Affliction", "Destruction", "Demonology","Affliction", "Destruction", "Demonology"
        ],
        [ # paladin
            "Holy", "Protection", "Retribution","Holy", "Protection", "Retribution","Holy", "Protection", "Retribution","Holy", "Protection", "Retribution"
        ],
        [ # druid
            "Balance", "Feral", "Guardian", "Restoration","Balance", "Feral", "Guardian", "Restoration","Balance", "Feral", "Guardian", "Restoration"
        ],
        [ # shaman
            "Elemental", "Enhancement", "Restoration","Elemental", "Enhancement", "Restoration","Elemental", "Enhancement", "Restoration","Elemental", "Enhancement", "Restoration"
        ],
        [ # monk
            "Brewmaster", "Mistweaver", "Windwalker", "Brewmaster", "Mistweaver", "Windwalker","Brewmaster", "Mistweaver", "Windwalker", "Brewmaster", "Mistweaver", "Windwalker"
        ],
        [ # demon hunter
            "Havoc", "Vengence", "Havoc", "Vengence","Havoc", "Vengence", "Havoc", "Vengence","Havoc", "Vengence", "Havoc", "Vengence"
        ],
        [ # death knight
            "Blood", "Frost", "Unholy","Blood", "Frost", "Unholy","Blood", "Frost", "Unholy","Blood", "Frost", "Unholy"
        ],
        [ # evoker
            "Augmentation", "Devastation", "Preservation","Augmentation", "Devastation", "Preservation","Augmentation", "Devastation", "Preservation","Augmentation", "Devastation", "Preservation",
        ]
]
rnd_class_index = rnd.randint(0, 12)
rnd_race_index = rnd.randint(0, 23)
rnd_spec_index = rnd.randint(0, 11)

print(f"{race_list[rnd_class_index][rnd_race_index]} {class_list[rnd_class_index]}({spec_list[rnd_class_index][rnd_spec_index]})")
