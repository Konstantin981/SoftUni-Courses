name = input()
password = input()
while True:
    new_password = input()
    if new_password == password:
        print(f"Welcome {name}!")
        break