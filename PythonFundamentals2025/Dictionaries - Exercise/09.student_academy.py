student_academy = {}
n = int(input())
for i in range(n):
    student = input()
    grade = float(input())
    if student not in student_academy:
        student_academy[student] = grade
    else:
        student_academy[student] =(student_academy[student] + grade)/2

for key, value in student_academy.items():
    if value < 4.50:
        del key
    else:
        print(f"{key} -> {value:.2f}")