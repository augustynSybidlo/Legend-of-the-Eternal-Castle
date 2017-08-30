def movement(board, player_x, player_y, current_tile=""):
    board[3][3] = "X"
    blocking_tiles = ["X"]
    if current_tile == "":
        current_tile = board[player_y][player_x]
    board[player_y][player_x] = "@"
    for line in board:
        print("".join(line))
    move = input()
    if move == "w":
        if board[player_y - 1][player_x] in blocking_tiles:
            print("Error, blocking tile")
            movement(board, player_x, player_y, current_tile)
        board[player_y][player_x] = current_tile
        player_y -= 1
        movement(board, player_x, player_y)
    if move == "s":
        if board[player_y + 1][player_x] in blocking_tiles:
            print("Error, blocking tile")
            movement(board, player_x, player_y, current_tile)
        board[player_y][player_x] = current_tile
        player_y += 1
        movement(board, player_x, player_y)
    if move == "a":
        if board[player_y][player_x - 1] in blocking_tiles:
            print("Error, blocking tile")
            movement(board, player_x, player_y, current_tile)
        board[player_y][player_x] = current_tile
        player_x -= 1
        movement(board, player_x, player_y)
    if move == "d":
        if board[player_y][player_x + 1] in blocking_tiles:
            print("Error, blocking tile")
            movement(board, player_x, player_y, current_tile)
        board[player_y][player_x] = current_tile
        player_x += 1
        movement(board, player_x, player_y)