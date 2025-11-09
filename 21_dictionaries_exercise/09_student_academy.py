# def get_average_grade(grades: list) -> float:
#     return sum(grades) / len(grades)


number = int(input())
students = {}
minimum_grade = 4.50
for _ in range(number):
    student_name = input()
    student_grade = float(input())
    if student_name not in students.keys():
        students[student_name] = []
    students[student_name].append(student_grade)
students_average_grades = {name: sum(grades) / len(grades) for name, grades in students.items()}

#using dictionary comprehension with if...and function for average grade
# students_average_grades = {name: get_average_grade(grades)  for name, grades in students.items()
#                            if get_average_grade(grades) >= minimum_grade}

for name, average in students_average_grades.items():
    if average >= minimum_grade:
        print(f"{name} -> {average:.2f}")