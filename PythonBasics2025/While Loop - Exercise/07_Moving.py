apartment_width = int(input())
apartment_length = int(input())
apartment_height = int(input())

apartmtent_space = apartment_height * apartment_length * apartment_width

while True:
    new_input = input()
    if new_input == "Done":
        print(f"{apartmtent_space} Cubic meters left.")
        break
    else:
        boxes = int(new_input)
        if boxes>apartmtent_space:
            print(f"No more free space! You need {boxes-apartmtent_space} Cubic meters more.")
            break
        else:
            apartmtent_space -= boxes