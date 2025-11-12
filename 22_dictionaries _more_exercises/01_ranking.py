contest = {}
users = {}
while True:
     command = input()
     if command == "end of contests":
         break
     current_contest, password_for_contest = command.split(":")
     if current_contest not in contest.keys():
         contest[current_contest] = password_for_contest
while True:
    data = input()
    if data == "end of submissions":
        break
    data = data.split("=>")
    course_name = data[0]
    course_password = data[1]
    student_name = data[2]
    points = int(data[3])
    if course_name in contest.keys():
        if contest[course_name] == course_password:
            if student_name not in users.keys():
                users[student_name] = [[course_name, points]]
            else:
                is_found = False
                for value in users[student_name]:
                    if course_name == value[0]:
                        is_found = True
                        if value[1] < points:
                            value[1] = points
                            break
                if not is_found:
                    users[student_name].append([course_name, points])
best_student_point = 0
best_student_name = ""
for name_of_student, student_data in users.items():
    sum_of_points = 0
    for index in range(len(student_data)):
        sum_of_points += student_data[index][1]
    if sum_of_points > best_student_point:
        best_student_point = sum_of_points
        best_student_name = name_of_student
print(f"Best candidate is {best_student_name} with total {best_student_point} points.")
print("Ranking:")
users = dict(sorted(users.items()))#, key=lambda x: x[0]))
for key, value in users.items():
    print(key)
    value = sorted(value, key= lambda x: x[1], reverse=True)
    for results in value:
        print(f"#  {results[0]} -> {results[1]}")