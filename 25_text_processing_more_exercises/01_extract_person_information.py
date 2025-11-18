repetition = int(input())

for _ in range(repetition):
    text = input()
    start_index_name = text.find("@") + 1
    end_index_name = text.find("|")
    name = text[start_index_name:end_index_name]

    start_index_age = text.find("#") + 1
    end_index_age = text.find("*")
    age = text[start_index_age:end_index_age]

    print(f"{name} is {int(age)} years old.")
