phonebook = {}
entry = input()
while "-" in entry:
    name, number = entry.split("-")
    phonebook[name] = number
    entry = input()
searches = int(entry)
for search in range(searches):
    search_by_name = input()
    if search_by_name in phonebook.keys():
        print(f"{search_by_name} -> {phonebook[search_by_name]}")
    else:
        print(f"Contact {search_by_name} does not exist.")