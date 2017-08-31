from movement import movement
import maps
from fighting import fight
import character_creator
import os


if __name__ == "__main__":
    import start_screen
    from inventory import show_inventory
    inventory = []
    os.system('clear')
    stats = character_creator.character_creation()
    width = 60
    height = 20
    board = maps.create_board_from_string()
    lives = 3
    coordinates = []
    coordinates.append(13)
    coordinates.append(1)
    direction = ""
    board[3][3] = "X"
    board[4][3] = "K"
    while lives > 0:
        os.system('clear')
        current_tile = "."
        board[coordinates[0]][coordinates[1]] = "@"
        for line in board:
            print("".join(line))
        direction = input("w/s/a/d for moving i - show inventory ")
        if direction == "e":
            break
        elif direction == "i":
            show_inventory(inventory)
        coordinates, board, enemy = movement(direction, coordinates, board, current_tile)
        if enemy != "":
            health_after_fight = fight(stats, enemy, True)
            input("Type anything to continue: ")
            if health_after_fight <= 0:
                lives -= 1
