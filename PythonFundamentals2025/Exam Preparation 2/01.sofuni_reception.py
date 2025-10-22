employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
questions_per_hour = employee1 + employee2 + employee3
questions_left = int(input())
current_hour = 0
while questions_left > 0:
    current_hour += 1
    if current_hour % 4 == 0:
        continue
    else:
        questions_left -= questions_per_hour
print(f"Time needed: {current_hour}h.")