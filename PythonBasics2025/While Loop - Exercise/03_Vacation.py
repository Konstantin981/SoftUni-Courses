vacation_money = float(input())
money_owned = float(input())
days_passed = 0
consecutive_spend = 0

while True:
    action = input()
    money = float(input())
    days_passed += 1
    if action == "spend":
        consecutive_spend += 1
        if consecutive_spend == 5:
            print("You can't save the money.")
            print(days_passed)
            break
        if money>money_owned:
            money_owned = 0
        else:
            money_owned -= money

    elif action == "save":
        money_owned += money
        consecutive_spend = 0

    if money_owned >= vacation_money:
        print(f"You saved the money for {days_passed} days.")
        break