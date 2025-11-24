import re
pattern = r"([=\/])([A-Z]{1}[a-zA-z]{2,})\1"
text = input()
travel_points = 0
matches = re.findall(pattern, text)
destinations = []
for match in matches:
    destinations.append(match[1])
print("Destinations: ", end = "")
print(", ".join(destinations))
travel_points = sum(len(destination) for destination in destinations)
print(f"Travel Points: {travel_points}")