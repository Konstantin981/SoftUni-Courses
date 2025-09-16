judges = int(input())
total_grades = 0
counter = 0
while True:
    presentation_name = input()

    if presentation_name == "Finish":
        break

    presentation_grades = 0
    for i in range(judges):
        grade = float(input())
        presentation_grades += grade
        total_grades += grade

    counter += judges
    presentaion_avg = presentation_grades / judges
    print(f"{presentation_name} - {presentaion_avg:.2f}.")

total_avg = total_grades / counter
print(f"Student's final assessment is {total_avg:.2f}.")
