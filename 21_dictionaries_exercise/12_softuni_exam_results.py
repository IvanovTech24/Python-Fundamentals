students_dictionary = {}
submission_dictionary = {}
while True:
    command = input()
    if command == "exam finished":
        break
    command = command.split("-")
    if len(command) == 2: # when user is banned
        user = command[0]
        del students_dictionary[user]
    elif len(command) == 3:
        name, course, points = command[0], command[1], int(command[2])
        if name not in students_dictionary.keys():
            students_dictionary[name] = 0
        if points > students_dictionary[name]:
            students_dictionary[name] = points
        if course not in submission_dictionary.keys():
            submission_dictionary[course] = 0
        submission_dictionary[course] += 1

print("Results:")
for username, point in students_dictionary.items():
    print(f"{username} | {point}")

print("Submissions:")
for language, submissions_count in submission_dictionary.items():
    print(f"{language} - {submissions_count}")
