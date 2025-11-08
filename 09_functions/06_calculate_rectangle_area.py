def calculate_rectangle_area(height: float, width: float):
    result = height * width
    return result

height_input = int(input())
width_ = int(input())
result_ = calculate_rectangle_area(height_input, width_)
print(result_)