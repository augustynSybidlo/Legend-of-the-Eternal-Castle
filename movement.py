def movement(direction, coordinates, board, current_tile):
    position_y = coordinates[0]
    position_x = coordinates[1]
    if current_tile != "@":
        board[position_y][position_x] = current_tile
    if direction == "w":
        position_y -= 1
    elif direction == "s":
        position_y += 1
    elif direction == "a":
        position_x -= 1
    elif direction == "d":
        position_x += 1
    position_y, position_x, board, enemy = check_tile_and_move(position_y, position_x, board, direction)
    coordinates[0] = position_y
    coordinates[1] = position_x
    return coordinates, board, enemy


def check_tile_and_move(position_y, position_x, board, direction):
    blocking_tiles = ["X", "|", "_", "#", "/"]
    enemies = ["W", "K", "O", "o", "D"]

    if board[position_y][position_x] in blocking_tiles:
        print("Error, blocking tile")
        if direction == "w":
            position_y += 1
        elif direction == "s":
            position_y -= 1
        elif direction == "a":
            position_x += 1
        elif direction == "d":
            position_x -= 1
        return position_y, position_x, board, ""

    elif board[position_y][position_x] in enemies:
        enemy = board[position_y][position_x]
        if enemy == "W":
            return position_y, position_x, board, "wolf"
        elif enemy == "K":
            return position_y, position_x, board, "knight"
        elif enemy == "O":
            return position_y, position_x, board, "ogre"
        elif enemy == "o":
            return position_y, position_x, board, "orc"
        if enemy == "D":
            return position_y, position_x, board, "D"

    else:
        return position_y, position_x, board, ""
