MENS_HAIRCUT = 15
LADIES_HAIRCUT = 20
KIDS_HAIRCUT = 10
TOUCH_UP = 20
FULL_COLOR = 30

goal = int(input())
earned = 0
while True:
    service = input()
    if service == "closed":
        if earned >= goal:
            print("You have reached your target for the day!")
        else:
            left = goal - earned
            print(f"Target not reached! You need {left}lv. more.")
        break

    if service == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            earned += MENS_HAIRCUT
        elif haircut_type == "ladies":
            earned += LADIES_HAIRCUT
        elif haircut_type == "kids":
            earned += KIDS_HAIRCUT
    elif service == "color":
        color_type = input()
        if color_type == "touch up":
            earned += TOUCH_UP
        elif color_type == "full color":
            earned += FULL_COLOR

    if earned >= goal:
        print("You have reached your target for the day!")
        break

print(f"Earned money: {earned}lv.")