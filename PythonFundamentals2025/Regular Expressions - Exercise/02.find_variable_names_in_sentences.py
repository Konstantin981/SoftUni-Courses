import re

some_string = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
results = re.findall(pattern, some_string)
print(",".join(results))