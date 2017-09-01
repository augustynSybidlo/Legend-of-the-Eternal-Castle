import random


def dice_roll(sides):
    dice_result = random.randint(1, sides)
    return dice_result


def enemy_basic_stats(enemy_type):
    enemy_stats = []
    if enemy_type == "wolf":
        enemy_stats.append(2)
        enemy_stats.append(5)
        enemy_stats.append(10)
        enemy_stats.append("w")
    if enemy_type == "knight":
        enemy_stats.append(4)
        enemy_stats.append(3)
        enemy_stats.append(16)
        enemy_stats.append("k")
    if enemy_type == "ogre":
        enemy_stats.append(7)
        enemy_stats.append(1)
        enemy_stats.append(20)
        enemy_stats.append("og")
    if enemy_type == "orc":
        enemy_stats.append(2)
        enemy_stats.append(2)
        enemy_stats.append(14)
        enemy_stats.append("or")
    return enemy_stats


def enemy_level_system(enemy_stats, enemy_level):
    for level_up in range(0, enemy_level):
        if enemy_stats[3] == "w":
            enemy_stats[1] += 1
            enemy_stats[2] += 2
        elif enemy_stats[3] == "k":
            stat_up = random.randint(1, 2)
            if stat_up == 1:
                enemy_stats[0] += 1
            else:
                enemy_stats[1] += 1
            enemy_stats[2] += 2
        elif enemy_stats[3] == "og":
            enemy_stats[0] += 2
            enemy_stats[2] += 3
        elif enemy_stats[3] == "or":
            stat_up = random.randint(1, 2)
            if stat_up == 1:
                enemy_stats[0] += 2
            else:
                enemy_stats[0] += 1
            enemy_stats[2] += 2
        return enemy_stats


def fight(player_stats, enemy_type, inventory_items, attack=False):
    enemy_level = player_stats[3]
    enemy_stats = enemy_basic_stats(enemy_type)
    enemy_stats = enemy_level_system(enemy_stats, enemy_level)
    enemy_strength = enemy_stats[0]
    enemy_agility = enemy_stats[1]
    enemy_health = enemy_stats[2]
    player_strength = player_stats[0]
    player_agility = player_stats[1]
    player_health = player_stats[2]
    player_level = player_stats[3]
    player_character = player_stats[4]
    if attack:
        print("You have attacked: ", enemy_type, "level: ", enemy_level)
        first_attack = True
        while True:
            attack_type = input("Choose action: s - simple attack, h - heavy attack")
            enemy_health, player_health = player_attack(player_strength, player_health, enemy_agility, enemy_level,
                                                        enemy_health, player_character, first_attack, inventory_items,
                                                        attack_type)
            if player_health <= 0 or enemy_health <= 0:
                break
            first_attack = False
            player_health = enemy_attack(player_agility, enemy_strength, player_health, player_character,
                                         inventory_items)
            if player_health <= 0 or enemy_health <= 0:
                break
        if player_health <= 0:
            print("You have lost the fight! Lives - 1")
        elif player_health >= 0:
            print("You have won the fight!")
        return player_health

    else:
        print("You have been attacked by: ", enemy_type, "level: ", enemy_level)
        while True:
            first_attack = False
            player_health = enemy_attack(player_agility, enemy_strength, player_health, player_character,
                                         inventory_items)
            if player_health <= 0 or enemy_health <= 0:
                break
            attack_type = input("Choose action: s - simple attack, h - heavy attack")
            enemy_health, player_health = player_attack(player_strength, player_health, enemy_agility, enemy_level,
                                                        enemy_health, player_character, first_attack, inventory_items,
                                                        attack_type)
            if player_health <= 0 or enemy_health <= 0:
                break

    if player_health <= 0:
        print("You have lost the fight! Lives - 1")
    elif player_health >= 0:
        print("You have won the fight!")
    return player_health


def enemy_attack(agility, enemy_strength, health, player_character, inventory_items):
    hit_armor_chance = 0
    if player_character == "l":
        max_counter = 2
    else:
        max_counter = 1
    counter = 0
    for item in inventory_items:
        if item[1] == "Armor":
            if item[0] == "Breastplate" and hit_armor_chance != 40:
                hit_armor_chance += 40
                counter += 1
            elif item[0] == "Shield"and hit_armor_chance != 30:
                hit_armor_chance += 30
                counter += 1
            elif item[0] == "Helmet" and hit_armor_chance != 20:
                hit_armor_chance += 20
                counter += 1
            if max_counter == counter:
                break
    hit_accuracy = random.randint(1, 100)
    if hit_accuracy < hit_armor_chance:
        print("Your armor reflected the attack.")
        return health
    elif hit_armor_chance != 0:
        print("Armor did not stop the the attack.")
    damage = enemy_strength + dice_roll(4)
    hit_chance = (100 - (2 * agility))
    hit = hit_result(hit_chance)
    if hit:
        health -= damage
        print("Enemy hits you, damage: ", str(damage))
    else:
        print("You avoided the attack")
    return health


def player_attack(player_strength, player_health, enemy_agility, enemy_level, enemy_health, player_character,
                  first_attack, inventory_items, attack_type="s"):
    damage = player_strength
    if player_character == "k":
        max_counter = 2
    else:
        max_counter = 1
    counter = 0
    for item in inventory_items:
        if item[1] == "Weapon":
            if item[0] == "Sword":
                additional_damage = random.randint(1, 8)
                damage += additional_damage
                print("Weapon damage bonus: ", str(additional_damage))
                counter += 1
            elif item[0] == "Mace":
                additional_damage = random.randint(1, 6)
                damage += additional_damage
                print("Weapon damage bonus: ", str(additional_damage))
                counter += 1
            elif item[0] == "Axe":
                additional_damage = random.randint(1, 5)
                damage += additional_damage
                print("Weapon damage bonus: ", str(additional_damage))
                counter += 1
            elif item[0] == "Knife":
                additional_damage = random.randint(1, 3)
                damage += additional_damage
                print("Weapon damage bonus: ", str(additional_damage))
                counter += 1
            if max_counter == counter:
                break

    if player_character == "a" and first_attack:
        if attack_type == "s":
            enemy_health -= (2 * damage)
            print("Simple assassination attempt successfull, damage: ", str(2*damage))
            return enemy_health, player_health
        else:
            hit_chance = 80 - (enemy_agility + enemy_level)
            hit = hit_result(hit_chance)
            if hit:
                enemy_health -= (3 * damage)
                print("Heavy assassination attempt successfull, damage: ", str(3*damage))
            else:
                player_health -= damage
                print("Heavy assassination attempt unsuccesfull, counter attack damage: ", str(damage))

            return enemy_health, player_health

    else:
        if attack_type == "s":
            enemy_health = int(enemy_health)
            hit_chance = 100 - (enemy_agility + enemy_level)
            hit = hit_result(hit_chance)
            if hit:
                enemy_health -= damage
                print("Simple attack success, damage: ", str(damage))
                return enemy_health, player_health
            else:
                print("Simple attack missed")
                return enemy_health, player_health
        elif attack_type == "h":
            hit_chance = 80 - (enemy_agility + enemy_level)
            hit = hit_result(hit_chance)
            if hit:
                enemy_health -= abs(1.5 * damage)
                print("Heavy attack success, damage: ", str(abs(1.5 * damage)))
                return enemy_health, player_health
            else:
                player_health -= abs(0.5 * damage)
                print("Heavy attack unsuccessfull, counter damage: ", str(abs(0.5 * damage)))
                return enemy_health, player_health


def hit_result(hit_chance):
    random_int = random.randint(1, 100)
    if random_int > hit_chance:
        return False
    else:
        return True
