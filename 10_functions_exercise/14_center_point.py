from math import floor

def closest_point(x_num1: float, y_num1: float, x_num2 : float, y_num2: float) -> float:
    first_distance = x_num1 ** 2 + y_num1 ** 2
    second_distance = x_num2 ** 2 + y_num2 ** 2

    if first_distance <= second_distance:
        print(f"({floor(x_num1)}, {floor(y_num1)})")
    else:
        print(f"({floor(x_num2)}, {floor(y_num2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


closest_point(x1, y1, x2, y2)
