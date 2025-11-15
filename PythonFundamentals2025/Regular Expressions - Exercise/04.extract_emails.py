import re
some_string = input()
pattern = r"\s(([a-z0-9]+)([a-z0-9\.\-_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
emails = re.findall(pattern, some_string)
for email in emails:
    print(email[0])