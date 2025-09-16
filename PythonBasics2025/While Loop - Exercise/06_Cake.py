cake_width = int(input())
cake_lenght = int(input())

pieces_left = cake_lenght * cake_width

while True:
    new_input = input()
    if new_input == "STOP":
        print(f"{pieces_left} pieces are left.")
        break

    else:
        pieces = int(new_input)
        if pieces >= pieces_left:
            print(f"No more cake left! You need {pieces-pieces_left} pieces more.")
            break
        else:
            pieces_left -= pieces