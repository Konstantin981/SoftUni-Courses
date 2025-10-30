characters = input().split(", ")
chars_and_ascii = {char:ord(char) for char in characters}
print(chars_and_ascii)