number_of_rows = int(input())
rows = []
actions = []
destroyed_ships = 0
hit = 0
row_len = 0
for _ in range(number_of_rows):
    rows += input().split()
row_len = int(len(rows)) // number_of_rows
rows = [int(x) for x in rows]
total_actions = input().split(" ")
for index in range(len(total_actions)):
    actions = "-".join(total_actions[index].split())
    hit = int(actions[0]) * row_len + int(actions[2])
    rows[hit] = int(rows[hit]) - 1
    if rows[hit] == 0:
        destroyed_ships += 1
print(destroyed_ships)