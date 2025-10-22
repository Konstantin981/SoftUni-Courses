shelf = input().split("&")
while True:
    command = input().split(" | ")
    if command[0] == "Done":
        print(", ".join(shelf))
        break
    action = command[0]
    if action == "Add Book":
        book = command[1]
        if book not in shelf:
            shelf.insert(0, book)
    elif action == "Take Book":
        book = command[1]
        if book in shelf:
            shelf.remove(book)
    elif action == "Swap Books":
        book1 = command[1]
        book2 = command[2]
        if book1 in shelf and book2 in shelf:
            index1=shelf.index(book1)
            index2=shelf.index(book2)
            shelf[index1], shelf[index2] = shelf[index2], shelf[index1]
    elif action == "Insert Book":
        book = command[1]
        if book not in shelf:
            shelf.append(book)
    elif action == "Check Book":
        index = int(command[1])
        if 0<=index<len(shelf)-1:
            book = shelf[index]
            print(book)