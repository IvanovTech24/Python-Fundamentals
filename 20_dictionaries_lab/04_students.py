command = input()
student_data = {}
while ":" in command:
    command = command.split(":")
    student_name, student_id, course = command[0], command[1], command[2]
    if course not in student_data:
        student_data[course] = {}
    student_data[course][student_id] = student_name
    command = input()
course = " ".join(command.split("_"))
for current_course, nested_dict in student_data.items():
    if current_course == course:
        for student_id, student_name in nested_dict.items():
            print(f"{student_name} - {student_id}")











# command = input()
# students_dict = {}
# while ":" in command:
#     command = command.split(':')
#     student_name, student_id, course = command[0], command[1], command[2]
#     if course not in students_dict:
#         students_dict[course] = {}
#     students_dict[course][student_id] = student_name
#     command = input()
#
# course = " ".join(command.split("_"))
# for key, value in students_dict.items():
#     if key == course:
#         for student_id, student_name in value.items():
#             print(f"{student_name} - {student_id}")





# students_dict = {
#     'programming basics': {'123': 'Peter'},
#     'fundamentals': {'5622': 'John', '89': 'Maya', '633': 'Lilly'}
# }