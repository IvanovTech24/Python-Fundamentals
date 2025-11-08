from math import sqrt

def line_length(x1: int, y1: int, x2: int, y2: int) -> float:
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def distance_to_center(x: int, y: int) -> float:
    return sqrt(x ** 2 + y ** 2)


first_x1 = float(input())
first_y1 = float(input())
first_x2 = float(input())
first_y2 = float(input())
second_x1 = float(input())
second_y1 = float(input())
second_x2 = float(input())
second_y2 = float(input())

#find the lengths of the two points
first_line = line_length(first_x1, first_y1, first_x2, first_y2)
second_line = line_length(second_x1, second_y1, second_x2, second_y2)

#check witch line is longer
if first_line >= second_line:
    if distance_to_center(first_x1, first_y1) <= distance_to_center(first_x2, first_y2):
        print(f"({int(first_x1)}, {int(first_y1)})({int(first_x2)}, {int(first_y2)})")
    else:
        print(f"({int(first_x2)}, {int(first_y2)})({int(first_x1)}, {int(first_y1)})")
else:
    if distance_to_center(second_x1, second_y1) <= distance_to_center(second_x2, second_y2):
        print(f"({int(second_x1)}, {int(second_y1)})({int(second_x2)}, {int(second_y2)})")
    else:
        print(f"({int(second_x2)}, {int(second_y2)})({int(second_x1)}, {int(second_y1)})")




