player_1 = input()
player_2 = input()
p1_points = 0
p2_points = 0

while True:
    p1_card = input()
    if p1_card == "End of game":
        print(f"{player_1} has {p1_points} points")
        print(f"{player_2} has {p2_points} points")
        break
    else:
        p1_card = int(p1_card)
        p2_card = int(input())
    if p1_card > p2_card:
        p1_points += (p1_card - p2_card)
    elif p2_card > p1_card:
        p2_points += (p2_card - p1_card)
    elif p1_card == p2_card:
        print("Number wars!")
        p1_card = input()
        p2_card = input()
        if p1_card > p2_card:
            print(f"{player_1} is winner with {p1_points} points")
        else:
            print(f"{player_2} is winner with {p2_points} points")
        break