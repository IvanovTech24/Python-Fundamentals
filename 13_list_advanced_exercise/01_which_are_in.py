#----------------------------------list comprehension-----------------
first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring = [first_element for first_element in first_sequence
             if any(first_element in
             second_element for second_element in second_sequence)]
print(substring)

#--------------------------------for loops-------------------------------
first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring = []
for first_element in first_sequence:
    for second_element in second_sequence:
        if first_element in second_element:
            substring.append(first_element)
            break
print(substring)