import re
pattern = r">>(\w+)<<(\d+\.*\d*)!(\d+)"
furniture = []
total_price = 0
command = input()
results = re.findall(pattern, command)
while command!="Purchase":
    results = []
    results = re.findall(pattern, command)
    if results:
        furniture.append(results[0][0])
        total_price += float(results[0][1]) * int(results[0][2])
    command = input()
print("Bought furniture:")
for piece in furniture:
    print(piece)
print(f"Total money spend: {total_price:.2f}")