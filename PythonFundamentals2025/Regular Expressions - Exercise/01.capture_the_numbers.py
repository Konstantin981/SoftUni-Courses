import re
all_matches = []
pattern = r"\d+"
line = input()
while line:
    result = re.findall(pattern, line)
    if result:
        all_matches.append(result)
    line = input()

for match in all_matches:
    print(*match,end = " ")