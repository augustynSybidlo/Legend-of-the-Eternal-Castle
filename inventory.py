import random_item


def add_to_inventory(inventory):
    max_weight_of_inventory = 100
    weight_of_inventory = 0
    new_item = random_item.main()
    for i in inventory:
        weight_of_inventory += i[2] 
    weight_of_inventory += new_item[2]
    if weight_of_inventory >= max_weight_of_inventory:
        print("You have not enought space in your inventory!")
    else:
        inventory.append(new_item)
    return weight_of_inventory, inventory


def show_inventory(inventory):
    weight_of_items = 0
    width_1 = 7
    width_2 = 10
    width_3 = 35
    print("Inventory:\n")
    print("Weight".ljust(width_1), "Type".ljust(width_2), "Item name".ljust(width_3), "\n")
    for element in inventory:
        print(str(element[2]).ljust(width_1), element[1].ljust(width_2), element[0].ljust(width_3))
    print("Total weight of items: %d".rjust(width_3) % weight_of_items)
    input("Type anything to exit.")
