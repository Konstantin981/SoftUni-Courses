student = input()
score = 0
max_tries = 0
grade = 1

while True:
    new_score = float(input())
    if new_score < 4.00:
        max_tries += 1
        if max_tries > 1:
            print(f"{student} has been excluded at {grade} grade")
            break
        continue

    score += new_score
    if grade == 12:
        avg_grade = score/12
        print(f"{student} graduated. Average grade: {avg_grade:.2f}")
        break
    grade += 1