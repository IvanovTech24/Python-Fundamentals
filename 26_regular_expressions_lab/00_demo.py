import re
# email = input()
# pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
# email_validation = re.match(pattern, email)
# if email_validation:
#     print(f"{email} - is valid email")
# else:
#     print(f"{email} - not valid email")

#-------------------------------re.search(pattern, text)----------------------------
# text = "The quick brown fox jump over the lazy dog. Python is fun. Programming is fun!"
# match = re.search(r"\bp\w*", text, re.IGNORECASE)
# if match:
#     print(f"The first word that starts with 'P' is: {match.group()}")

#----------------------------re.sub(pattern, text)-----------------------
text = "There are 3 dogs and 4 cats"
# result = re.sub(r'\d', "NUMBER", text)
# print(result)
result = re.subn(r"\d", "number", text)
print(result)