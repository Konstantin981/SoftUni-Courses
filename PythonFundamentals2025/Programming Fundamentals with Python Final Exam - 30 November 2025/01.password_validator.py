def MakeUpper(password:str, index:int)->str:
    left_part = password[:index]
    right_part = password[index+1:]
    password = left_part + password[index].upper() + right_part
    print(password)
    return password
def MakeLower(password:str, index:int)->str:
    left_part = password[:index]
    right_part = password[index+1:]
    password = left_part + password[index].lower() + right_part
    print(password)
    return password
def Insert(password:str, index:int, char:chr)->str:
    left_part = password[:index]
    right_part = password[index:]
    password = left_part + char + right_part
    print(password)
    return password
def Replace(password:str, char:chr, value:int)->str:
    new_char = chr(ord(char) + value)
    password = password.replace(char, new_char)
    print(password)
    return password
def Validation(password:str):
    if len(password)<8:
        print("Password must be at least 8 characters long!")
    is_other = False
    uppercase_letters = 0
    lowercase_letters = 0
    digits = 0
    for char in password:
        if (not char.isalnum()) and char!="_":
            is_other = True
        if char.isupper():
            uppercase_letters+=1
        if char.islower():
            lowercase_letters+=1
        if char.isdigit():
            digits+=1
    if is_other:
        print("Password must consist only of letters, digits and _!")
    if uppercase_letters==0:
        print("Password must consist at least one uppercase letter!")
    if lowercase_letters==0:
        print("Password must consist at least one lowercase letter!")
    if digits==0:
        print("Password must consist at least one digit!")

password = input()
command = input()
while command!="Complete":
    command = command.split()
    if command[0] == "Validation":
        Validation(password)
    elif command[0] + " " + command[1] == "Make Upper":
        index = int(command[2])
        if not 0<=index<=len(password)-1:
            continue
        password = MakeUpper(password, index)
    elif command[0] + " " + command[1] == "Make Lower":
        index = int(command[2])
        if not 0<=index<=len(password)-1:
            continue
        password = MakeLower(password, index)
    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        if not 0<=index<=len(password)-1:
            continue
        password = Insert(password, index, char)
    elif command[0] == "Replace":
        char = command[1]
        value = int(command[2])
        if char not in password:
            continue
        password = Replace(password,char, value)
    command = input()