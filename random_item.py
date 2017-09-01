import random


def random_item_generator(items):
    new_item = random.choice(items) 
    return new_item
    

def main():
    items = [
        ["Sword", "Weapon", 15],
        ["Axe", "Weapon", 10],
        ["Knife", "Weapon", 5],
        ["Mace", "Weapon", 15],
        ["Breastplate", "Armor", 40],
        ["Shield", "Armor", 20],
        ["Helmet", "Armor", 15]
    ]
    item = random_item_generator(items)
    items.remove(item)
    return item


main()
