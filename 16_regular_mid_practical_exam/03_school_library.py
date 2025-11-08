shelf_books = input().split("&")

while True:
    command = input().split(" | ")
    current_command = command[0]
    if current_command == "Done":
        break
    if current_command == "Add Book":
        book_name = command[1]
        if book_name not in shelf_books:
            shelf_books.insert(0, book_name)
        elif book_name in shelf_books:
            continue
    if current_command == "Take Book":
        book_name = command[1]
        if book_name in shelf_books:
            shelf_books.remove(book_name)
        elif book_name not in shelf_books:
            continue
    if current_command == "Swap Books":
        book_name_1 = command[1]
        book_name_2 = command[2]
        if (book_name_1 not in shelf_books) or (book_name_2 not in shelf_books):
            continue
        elif (book_name_1 in shelf_books) and (book_name_2 in shelf_books):
            index_1 = shelf_books.index(book_name_1)
            index_2 = shelf_books.index(book_name_2)
            shelf_books[index_1], shelf_books[index_2] = shelf_books[index_2], shelf_books[index_1]
    if current_command == "Insert Book":
        book_name = command[1]
        if book_name in shelf_books:
            continue
        else:
            shelf_books.append(book_name)
    if current_command == "Check Book":
        index = int(command[1])
        if index in range(len(shelf_books)):
            print(shelf_books[index])
        elif index not in range(len(shelf_books)):
            continue
#print(", ".join(map(str, shelf_books)))
#print(*shelf_books, sep=", ")
print(", ".join([str(x) for x in shelf_books]))
