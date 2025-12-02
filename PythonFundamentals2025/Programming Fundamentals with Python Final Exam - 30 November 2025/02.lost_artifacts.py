import re
pattern = r"[*^]+([A-Za-z\ ]{6,})[*^][^A-Za-z\d]*[+]+([-]{0,1}[\d]+[.][\d]+[,][-]{0,1}[\d]+[.][\d]+)[+]+"
text = input()
matches = re.findall(pattern, text)
if not matches:
    print("No valid artifacts found.")
for match in matches:
    artifact_name = match[0]
    coordinates = match[1]
    print(f"Found {artifact_name} at coordinates {coordinates}.")