first_player = [int(x) for x in input().split()]
second_player = [int(x) for x in input().split()]
third_player = [int(x) for x in input().split()]
board = [first_player, second_player, third_player]
winner = None
is_winner = False

for row in board:
    if row.count(1) == 3:
        winner = "First player won"
        is_winner = True
    elif row.count(2) == 3:
        winner = "Second player won"
        is_winner = True

for col_index in range(3):
    if board[0][col_index] == 1 and board[1][col_index] == 1 and board[2][col_index] == 1:
        winner = "First player won"
        is_winner = True
    elif board[0][col_index] == 2 and board[1][col_index] == 2 and board[2][col_index] == 2:
        winner = "Second player won"
        is_winner = True

if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
    winner = "First player won"
    is_winner = True
elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
    winner = "First player won"
    is_winner = True
elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
    winner = "First player won"
    is_winner = True
elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
    winner = "First player won"
    is_winner = True

if is_winner:
    print(f"{winner}")
else:
    print("Draw!")
