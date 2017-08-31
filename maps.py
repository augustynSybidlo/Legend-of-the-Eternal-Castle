def create_board(width, height):
    w = "."
    width_of_board = [w] * width
    board = []
    for i in range(height):
        board.append(list(width_of_board))
    return board

map_1 = '''