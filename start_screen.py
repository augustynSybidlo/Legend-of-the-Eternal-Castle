import os

start_screen = '''
       \   |    \    ___)   )  ____)  \    ___) |    \  |  | |    \       )   (   \    ___)
        |  |     |  (__    /  /  __    |  (__   |  |\ \ |  | |     |     /     \   |  (__
        |  |     |   __)  (  (  (  \   |   __)  |  | \ \|  | |     |    (       )  |   __)
        |  |__   |  (___   \  \__)  )  |  (___  |  |  \    | |     |     \     /   |  (
       /      )_/       )___)      (__/       )_|  |___\   |_|    /_______)   (___/    \____
                                 _        __    ___    _        __
                                 (__    __) \  |   |  / \    ___)
                                    |  |     |  \_/  |   |  (__
                                    |  |     |   _   |   |   __)
                                    |  |     |  / \  |   |  (___
                                 ___|  |____/  |___|  \_/       )_
                      ___        __        __     ___     ___    _____  _____     ____
              \    ___) (__    __) \    ___) |    \  |    \  |  |    /  \    \   |
               |  (__      |  |     |  (__   |     ) |  |\ \ |  |   /    \    |  |
               |   __)     |  |     |   __)  |    /  |  | \ \|  |  /  ()  \   |  |
               |  (___     |  |     |  (___  | |\ \  |  |  \    | |   __   |  |  |__
              /       )____|  |____/       )_| |_\ \_|  |___\   |_|  (__)  |_/      )_
                    __    ______  ______       ___        __     ____        __
                     /  __)    /  \     )  ____) (__    __) \   |    \    ___)
                    |  /      /    \   (  (___      |  |     |  |     |  (__
                    | |      /  ()  \   \___  \     |  |     |  |     |   __)
                    |  \__  |   __   |  ____)  )    |  |     |  |__   |  (___
                    _\    )_|  (__)  |_(      (_____|  |____/      )_/       )_by_Nikodem&Augustyn

                                         Hello brave warrior!
                                 Our land is under oppressive rule of
                            a dwarf who  steers our King and his ministers
                            from his castle.  Everyone is doing  what  the
                            dwarf tells them.  Last hope in you! Go to the
                            castle and kill the dwarf! Release our kingdom.'''


how_to_play = '''\nMovement:
                w = move up
a = move left   s = move down   d = move right

Interaction:
i = show inventory

Combat:
s = simple attack
h = heavy attack'''  # sterowanie


def main():
    print(start_screen)
    while True:
        start = input('''To start the game press: s
How to play: c  ''')
        try:
            if start == 's':
                break
            elif start == 'c':
                os.system('clear')
                print(how_to_play)
        except:
            print("Wrong input! Only s/c characters available")


main()
