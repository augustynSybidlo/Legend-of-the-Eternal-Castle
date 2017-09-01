def character_creation():
    stats = []
    while True:
        print("""
           Choose your character class:

           Class:               Warrior (type "w")         Assassin (type "a")
           Strength:               5                       3
           Agility :               4                       6
           Vitality:               20                      18
           Special ability: Adds 1 to every attack     May attempt to assassinate
                            dice roll                  if he is the one attacking first
                                                       Then his first attack will couse
                                                       double damage and cannot be blocked

           Class:                Looter  (type "l")        Knight (type "k")
           Strength:               3                       4
           Agility                 5                       3
           Vitality                18                      24
           Special ability:   May use 2 weapons        May use two pieces of armor
                              at the same time         at the same time""")
        character_class = input("Select your character class (w,a,l,k): ")
        if character_class == "w":
            stats.append(5)
            stats.append(4)
            stats.append(20)
            stats.append(1)
            stats.append("w")
            break
        elif character_class == "a":
            stats.append(3)
            stats.append(6)
            stats.append(18)
            stats.append(1)
            stats.append("a")
            break
        elif character_class == "l":
            stats.append(3)
            stats.append(5)
            stats.append(18)
            stats.append(1)
            stats.append("l")
            break
        elif character_class == "k":
            stats.append(4)
            stats.append(3)
            stats.append(24)
            stats.append(1)
            stats.append("k")
            break
        else:
            print("Please type one of following latters: w,a,l,k to choose your characters class")
    return stats


def show_stats_and_level_up(stats, level_up=False):
    print("Current stats: \n", )
    if stats[4] == "w":
        character_class = "Warrior"
    elif stats[4] == "a":
        character_class = "Assassin"
    elif stats[4] == "l":
        character_class = "Looter"
    elif stats[4] == "k":
        character_class = "Knight"
    print("character class: ", character_class, "Level: ", str(stats[3]), "\n Strength: ", str(stats[0]), "\n Agility: "
          ,str(stats[1]), "\n Vitality: ", str(stats[2]))
    if level_up:
        stats[3] += 1
        for x in range(3):
            while True:
                improve = input("Which statistic would you like to improve? s - strength, a - agility, v - vitality")
                if improve == "s":
                    stats[0] += 1
                    print("Current stats: \n", )
                    print("character class: ", character_class, "Level: ", str(stats[3]), "\n Strength: ",
                          str(stats[0]), "\n Agility: "
                          , str(stats[1]), "\n Vitality: ", str(stats[2]))
                    break
                elif improve == "a":
                    stats[1] += 1
                    print("Current stats: \n", )
                    print("character class: ", character_class, "Level: ", str(stats[3]), "\n Strength: ",
                          str(stats[0]), "\n Agility: "
                          , str(stats[1]), "\n Vitality: ", str(stats[2]))
                    stats[1] += 1
                    break
                elif improve == "v":
                    stats[2] += 4
                    print("Current stats: \n", )
                    print("character class: ", character_class, "Level: ", str(stats[3]), "\n Strength: ",
                          str(stats[0]), "\n Agility: "
                          , str(stats[1]), "\n Vitality: ", str(stats[2]))
        input("Press anything to close...")
        return stats
    input("Press anything to close...")
    return stats
