string = input()
encrypted_message = ""
for char in string:
    encrypted_message+=chr(ord(char)+3)
print(encrypted_message)