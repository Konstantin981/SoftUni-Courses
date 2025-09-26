key = int(input())
letters = int(input())
secret_message = ""
for i in range(letters):
    letter = input()
    new_letter = chr(ord(letter) + key)
    secret_message += new_letter

print(secret_message)
