budget = int(input())
total_price = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break

    purchase = int(command)
    if total_price + purchase > budget:
        print("You went in overdraft!")
        break

    total_price += purchase