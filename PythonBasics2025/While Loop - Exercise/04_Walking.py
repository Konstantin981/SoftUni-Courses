steps_total = 0
while True:
    new_input = input()
    if new_input == "Going home":
        steps = int(input())
        steps_total += steps
        if steps_total >= 10000:
            print("Goal reached! Good job!")
            print(f"{steps_total - 10000} steps over the goal!")
            break
        else:
            print(f"{10000-steps_total} more steps to reach goal.")
            break
    else:
        steps = int(new_input)
        steps_total += steps
    if steps_total >= 10000:
        print("Goal reached! Good job!")
        print(f"{steps_total-10000} steps over the goal!")
        break