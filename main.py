from movement import movement
import maps
from fighting import fight
import character_creator



if __name__ == "__main__":
    import start_screen
    from inventory import show_inventory
    inventory = []
    stats = character_creator.character_creation()
    width = 60
    height = 20
    board = maps.create_board(width, height)
    lives = 3
    coordinates = []
    coordinates.append(0)
    coordinates.append(0)
    direction = ""
    while lives > 0:
        current_tile = board[coordinates[0]][coordinates[1]]
        board[coordinates[0]][coordinates[1]] = "@"
        board[3][3] = "X"
        board[4][3] = "K"
        for line in board:
            print("".join(line))
        direction = input("w/s/a/d for moving i - show inventory")
        if direction == "e":
            break
        elif direction == "i":
            show_inventory(inventory)
        if direction == "w" or direction == "a" or direction == "s" or direction == "d" or direction == "i":
            coordinates, board, enemy = movement(direction, coordinates, board, current_tile)
            if enemy != "":
                health_after_fight = fight(stats, enemy, True)
                if health_after_fight <= 0:
                    lives -= 1