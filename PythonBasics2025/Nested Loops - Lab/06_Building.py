floors = int(input())
rooms = int(input())
room_type = ""
for floor in range(floors, 0, -1):
    for room in range(rooms):
        if floor == floors:
            room_type = "L"
        elif floor % 2 == 0:
            room_type = "O"
        elif floor % 2 == 1:
            room_type = "A"

        print(f"{room_type}{floor}{room}", end=' ')

    print()
