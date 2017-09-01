from movement import movement
import maps
from fighting import fight
import character_creator
import os
import random_item
import inventory


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def import_highscores(file_name="highscores.txt"):
    file = open(file_name, "r")
    highscores_list = [line.split(",") for line in file]
    file.close()
    return highscores_list


def show_highscores_and_play_again(highscores):
    os.system("clear")
    while True:
        action = input("h - highscores, p - play again, e - exit: ")
        if action == "p":
            main()
        elif action == "e":
            exit("Goodbye!")
        elif action == "h":
            print("Highscores: \n")
            for line in highscores:
                print(" ".join(line))


def main():
    import start_screen
    special_tiles = ["$", "=", "i", "e", "", "D"]
    score = 0
    inventory_items = []
    try:
        highscores = import_highscores()
    except FileNotFoundError:
        highscores = []
    os.system('clear')
    stats = character_creator.character_creation()
    board = maps.create_board_from_string()
    os.system("clear")
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
        if score % 50 == 0 and score != 0:
            stats = character_creator.show_stats_and_level_up(stats, True)
            score += 10
        print("Lives remaining: ", str(lives))
        for line in board:
            print("".join(line))
        print("w/s/a/d for moving, i - show inventory, c - show stats, e-exit " )
        direction = getch()
        if direction == "e":
            exit("Sad to see you go.")
        elif direction == "i":
            os.system(clear)
            inventory.show_inventory(inventory_items)
        elif direction == "c":
            character_creator.show_stats_and_level_up(stats)

        coordinates, board, enemy = movement(direction, coordinates, board, current_tile)
        if enemy not in special_tiles:
            health_after_fight = fight(stats, enemy, inventory_items, True)
            input("Type anything to continue: ")
            if health_after_fight > 0:
                score += 10
            if health_after_fight <= 0:
                lives -= 1
        elif enemy == "$":
            inventory_items = inventory.add_to_inventory(inventory_items)
            input("Type anything to continue...")
        elif enemy == "=":
            while True:
                os.system("clear")
                print("""
                To get into the castle, first you must solve this riddle:
                
                How do cows count?""")
                answer = input("""
                1 - Same way people do.
                2 - Bacwards.
                3 - They use cow'nter.""")
                if answer == "3":
                    break
                elif answer == "1" or answer == "2":
                    print("Answer was incorrect.")
                else:
                    print("Wrong input, choose 1, 2 or 3")
            board = maps.create_board_from_string(87, "2")
            coordinates[0] = 13
            coordinates[1] = 1
        elif enemy == "D":
            os.system('clear')
            while lives > 0:
                print("""   
                            ___
                           (   )
                           /|  |>
                          / |__| 
                            /  |
                You have finally found an evil dwarf!
                He is much stronger than you expected. 
                Since there is no point in fighting him 
                with your sword you decide to blow his
                mind by guessing random 3 digit number
                in 10 tries.""")
                from cold_warm_hot import main
                end_game, score = main(score)
                if end_game:
                    print('''
                                                     _        __    ___    _        _____        __     ___    _     ___
                                                    (__    __) \  |   |  / \    ___)    \    ___) |    \  |  | |    \ 
                                                       |  |     |  \_/  |   |  (__       |  (__   |  |\ \ |  | |  |  | 
                                                       |  |     |   _   |   |   __)      |   __)  |  | \ \|  | |  |  | 
                                                       |  |     |  / \  |   |  (___      |  (___  |  |  \    | |  |  | 
                                                    ___|  |____/  |___|  \_/       )____/       )_|  |___\   |_|    /___
                                                You have defetad the evil dwarf! Thank you so much! Here is 500+ gold coins!''')
                    while True:
                        username = input("Type in your username: ")
                        if len(username) > 8:
                            print("Username too long! (max. 8 char.)")
                        else:
                            break
                        highscore = []
                        highscore.append(username)
                        highscore.append(str(score))
                        if stats[4] == "w":
                            highscore.append("Warrior")
                        elif stats[4] == "a":
                            highscore.append("Assassin")
                        elif stats[4] == "l":
                            highscore.append("Looter")
                        elif stats[4] == "k":
                            highscore.append("Knight")
                        highscore.append("level:" + str(stats[3]))
                        highscores.append(highscore)
                    show_highscores_and_play_again(highscores)
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
            exit("Game over :(")
    exit("You have lost all your lives! Game over.")

main()