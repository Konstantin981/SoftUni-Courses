parking = {}
n = int(input())
for i in range(n):
    command = input().split()
    action = command[0]
    username = command[1]
    if action == "register":
        license_plate = command[2]
        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")
    elif action == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for key,value in parking.items():
    print(f"{key} => {value}")