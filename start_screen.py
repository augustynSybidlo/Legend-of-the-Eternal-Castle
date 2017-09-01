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


how_to_play = """
Movement:
                w = move up
a = move left   s = move down   d = move right

Enemies:

W -wolf K - knight O-ogre o - orc

Special tiles:

$- chest

Interaction:               Weapons:                        Armor:
i = show inventory         Give you random damage bonus:   Gives you a chance to deflect enemy attack:
                           Sword 1-8                       Breastplate - 40%
Combat:                    Mace 1-6                        Shield - 30%     
s = simple attack          Axe  1-5                        Helmet - 10%
h = heavy attack           Knife 1-3
                            
Characters can use only one weapon and one pice of armor with an exception of Warrior (2 weapons)
and Looter (2 pices of armor)
You can't use 2 pices of the same armor

Other commands appear at the terminal when you avaliable."""

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
            elif start == "a":
                print(about)
            
        except:
            print("Wrong input! Only s/c characters available")


main()
