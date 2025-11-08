def is_exit(current_row, current_col):
    on_edge = current_row == 0 or current_row == rows_in_maze - 1\
              or current_col == 0 or current_col == len(maze[current_row]) - 1

    return on_edge and (maze[current_row][current_col] == " "
                        or maze[current_row][current_col] == "k")


rows_in_maze = int(input())
maze = []
kate_row = 0
kate_col = 0

for index in range(rows_in_maze):
    current_rows = input()
    maze.append(list(current_rows))
for row_index in range(len(maze)):
    for col in range(len(maze[row_index])):
        if maze[row_index][col] == "k":
            kate_row = row_index
            kate_col = col
            break
stack = [[kate_row, kate_col, 0]]
max_moves = 0
while len(stack) > 0:
    current = stack.pop()
    row = current[0]
    col = current[1]
    steps = current[2]

    if maze[row][col] == "x":
        continue
    if is_exit(row, col):
        if steps > max_moves:
            max_moves = steps
    # maze[row] = maze[row][:col] + "x" + maze[row][col + 1:]
    maze[row][col] = "x"
    # проверяваме за свободно пространство
    # нагоре
    if row - 1 >= 0 and maze[row - 1][col] == " ":
        stack.append([row - 1, col, steps + 1])
    # надолу
    if row + 1 < rows_in_maze and maze[row + 1][col] == " ":
        stack.append([row + 1, col, steps + 1])
    # наляво
    if col - 1 >= 0 and maze[row][col - 1] == " ":
        stack.append([row, col - 1, steps + 1])
    # надясно
    if col + 1 < len(maze[row]) and maze[row][col + 1] == " ":
        stack.append([row, col + 1, steps + 1])
if max_moves == 0:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {max_moves + 1} moves")
