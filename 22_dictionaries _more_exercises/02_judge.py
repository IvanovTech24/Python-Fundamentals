competition = {}
users = {}
while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in competition.keys():
        competition[contest] = {username: points}
    else:
        if username in competition[contest].keys():
            if competition[contest][username] < points:
                competition[contest][username] = points
        else:
            competition[contest][username] = points

for current_contest, current_student in competition.items():
    for key, value in current_student.items():
        if key not in users.keys():
            users[key] = 0
        users[key] += value

for current_contest, current_student in competition.items():
    print(f"{current_contest}: {len(current_student)} participants")
    sorted_participants = sorted(current_student.items(), key=lambda x: (-x[1], x[0]))
    for index, (username, points) in enumerate(sorted_participants, start=1):
        print(f"{index}. {username} <::> {points}")

print("Individual standings:")
sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
for index, (username, total_points) in enumerate(sorted_users, start=1):
    print(f"{index}. {username} -> {total_points}")