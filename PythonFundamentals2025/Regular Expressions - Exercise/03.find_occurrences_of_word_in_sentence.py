import re
some_string = input()
word = input()
pattern = rf"\b{word}\b"
matches = re.findall(pattern, some_string, re.IGNORECASE)
print(len(matches))