import re
text = input()
pattern = "(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
results = re.finditer(pattern, text)
for result in results:
    print(result.group(), end = " ")