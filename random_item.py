import random


def random_item_generator(items):
    new_item = random.choice(items) 
    return new_item
    

def main():
    items = [
        ["Sword", "Weapon", 15],
        ["Bow", "Weapon", 5],
        ["Health Potion", "Potion", 1],
        ["Spear", "Weapon", 20],
        ["Long Bow", "Weapon", 10],
        ["Heavy Sword", "Weapon", 25],
        ["Armor", "Defence", 40],
        ["Shield", "Defence", 20],
        ["Big Health Potion", "Potion", 2],
        ["Helmet", "Defence", 15]
    ]
    item = random_item_generator(items)
    items.remove(item)
    return item


main()
