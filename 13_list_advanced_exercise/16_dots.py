def is_dot(current_row, current_col):
    return board[current_row][current_col] == "."

def in_bound(current_row, current_col):
    return 0 <= current_row < len(board) and 0 <= current_col < len(board[0])

def is_wall(current_row, current_col):
    return board[current_row][current_col] == "-"

def is_visited(current_row, current_col):
    return board[current_row][current_col] == "v"

def find_dots(current_row, current_col):
    if not in_bound(current_row, current_col) or is_wall(current_row, current_col) \
            or is_visited(current_row, current_col):
        return 0

    board[current_row][current_col] = "v"
    dots_count = 1
    for down_row, down_col in [(1,0), (-1,0), (0,1), (0,-1)]:
        dots_count += find_dots(current_row + down_row, current_col + down_col)
    return dots_count


# Input
number_of_rows = int(input())
board = [input().split() for x in range(number_of_rows)]

dots_count_connected = 0
for row in range(len(board)):
    for col in range(len(board[0])):
        if is_dot(row, col):
            dots_count_connected = max(dots_count_connected, find_dots(row, col))

print(dots_count_connected)