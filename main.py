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
        if enemy != "" and enemy != "D":
            health_after_fight = fight(stats, enemy, True)
            input("Type anything to continue: ")
            if health_after_fight <= 0:
                lives -= 1
        elif enemy == "D":
            while lives > 0:
                from cold_warm_hot import main
                end_game = main()
                if end_game:
                    print('''
                                                     _        __    ___    _        _____        __     ___    _     ___
                                                    (__    __) \  |   |  / \    ___)    \    ___) |    \  |  | |    \ 
                                                       |  |     |  \_/  |   |  (__       |  (__   |  |\ \ |  | |  |  | 
                                                       |  |     |   _   |   |   __)      |   __)  |  | \ \|  | |  |  | 
                                                       |  |     |  / \  |   |  (___      |  (___  |  |  \    | |  |  | 
                                                    ___|  |____/  |___|  \_/       )____/       )_|  |___\   |_|    /___

                                                You have defetad the evil dwarf! Thank you so much! Here is 500+ gold coins!''')
                    exit("Game won!")
                else:
                    lives -= 1
            print('''
                                 _        __    ___    _        _____        __     ___    _     ___
                                (__    __) \  |   |  / \    ___)    \    ___) |    \  |  | |    \  
                                   |  |     |  \_/  |   |  (__       |  (__   |  |\ \ |  | |  |  | 
                                   |  |     |   _   |   |   __)      |   __)  |  | \ \|  | |  |  | 
                                   |  |     |  / \  |   |  (___      |  (___  |  |  \    | |  |  | 
                                ___|  |____/  |___|  \_/       )____/       )_|  |___\   |_|    /___

                                        You are dead... so you can't really see it, shame.''')
            exit("Game lost :(")
    exit("You have lost all your lives! Game lost.")
