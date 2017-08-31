import Movement
import Maps


def main():
    width = 60
    height = 20
    board = Maps.create_board(width, height)
    Movement.movement(board, 0, 0)


main()