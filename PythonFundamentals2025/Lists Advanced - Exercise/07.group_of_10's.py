numbers = list(map(int, input().split(", ")))
boundary = 0
current_group = []
while numbers:
    boundary +=10
    current_group = [num for num in numbers if num<=boundary]
    numbers = [x for x in numbers if x not in current_group]
    print(f"Group of {boundary}'s: {current_group}")