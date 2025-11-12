import re
text = input()
pattern = r"\+359([ -])2\1\d{3}\1\d{4}\b"
matches = re.findall(pattern, text)
print(", ".join([m.group(0) for m in re.finditer(pattern, text)]))
