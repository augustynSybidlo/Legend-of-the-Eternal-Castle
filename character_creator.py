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
