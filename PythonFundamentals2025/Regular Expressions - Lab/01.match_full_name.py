import re
text = input()
pattern = r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b"
result = re.findall(pattern, text)
print(" ".join(result))