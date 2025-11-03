force_book = {}
command = input()
while command!="Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        force_user_is_part_of_the_force = False
        for force_user_list in force_book.values():
            if force_user in force_user_list:
                force_user_is_part_of_the_force = True
                break

        if not force_user_is_part_of_the_force:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)
    elif "->" in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]
        force_user_is_part_of_the_force = False
        for force_user_list in force_book.values():
            if force_user in force_user_list:
                force_user_is_part_of_the_force = True
                force_user_list.remove(force_user)
                break

        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for key, value in force_book.items():
    if value == []:
        continue
    else:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")