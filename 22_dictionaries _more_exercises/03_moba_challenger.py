players_dictionary = {}
challengers_dictionary = {}
while True:
    command = input()
    if command == "Season end":
        break
    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in players_dictionary.keys():
            players_dictionary[player] = {position: skill}
        else:
            if position not in players_dictionary[player]:
                players_dictionary[player][position] = skill
            else:
                if players_dictionary[player][position] < skill:
                    players_dictionary[player][position] = skill

    elif " vs " in command:
        player1, player2 = command.split(" vs ")
        if player1 in players_dictionary.keys() and player2 in players_dictionary.keys():
            position_player1 = players_dictionary[player1]
            position_player2 = players_dictionary[player2]
            # finding a common position, by intersection() method
            common_position = set(position_player1.keys()).intersection(set(position_player2.keys()))

            if common_position:
                # finding a total point per player, by generator expression
                total_skill_player1 = sum(position_player1[position] for position in common_position)
                total_skill_player2 = sum(position_player2[position] for position in common_position)
                if total_skill_player1 > total_skill_player2:
                    del players_dictionary[player2]
                elif total_skill_player2 > total_skill_player1:
                    del players_dictionary[player1]
# sum, the total points of each player
for name, position_points in players_dictionary.items():
    for key, value in position_points.items():
        if name not in challengers_dictionary.keys():
            challengers_dictionary[name] = 0
        challengers_dictionary[name] += value
# printing the name and total skill
sorted_challengers_dictionary = sorted(challengers_dictionary.items(), key=lambda x: (-x[1], x[0]))
for name, total_skills in sorted_challengers_dictionary:
    print(f"{name}: {total_skills} skill")
    sorted_players_dictionary = sorted(players_dictionary[name].items(), key=lambda x: (-x[1], x[0]))
    for position, skill in sorted_players_dictionary:
        print(f"- {position} <::> {skill}")