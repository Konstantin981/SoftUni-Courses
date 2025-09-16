country = input()
tool = input()
score = 0

if country == "Russia":
    if tool == "ribbon":
        score = 9.100 + 9.400
    elif tool == "hoop":
        score = 9.300 + 9.800
    elif tool == "rope":
        score = 9.600 + 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        score = 9.600 + 9.400
    elif tool == "hoop":
        score = 9.550 + 9.750
    elif tool == "rope":
        score = 9.500 + 9.400
elif country == "Italy":
    if tool == "ribbon":
        score = 9.200 + 9.500
    elif tool == "hoop":
        score = 9.450 + 9.350
    elif tool == "rope":
        score = 9.700 + 9.150


percent_scored = (score/20) * 100
percent_needed = 100 - percent_scored
print(f"The team of {country} get {score:.3f} on {tool}.")
print(f"{percent_needed:.2f}%")