command = input()
students_dictionary = {}
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in students_dictionary.keys():
        students_dictionary[course_name] = []
    students_dictionary[course_name].append(student_name)
    command = input()
for course_name, registered_students in students_dictionary.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")