students = int(input())
top_students = 0
between_4_and_499 = 0
between_3_and_399 = 0
failed = 0
total_grades = 0

for i in range(students):
    grade = float(input())
    if grade >= 5.00:
        top_students += 1
    elif 4.00<=grade<=4.99:
        between_4_and_499 += 1
    elif 3.00<=grade<=3.99:
        between_3_and_399 += 1
    elif grade<=2.99:
        failed += 1

    total_grades += grade

percent_top = (top_students / students) * 100
percent_between_4_and_499 = (between_4_and_499 / students) * 100
percent_between_3_and_399 = (between_3_and_399 / students) * 100
percent_failed = (failed / students) * 100
avg_grade = total_grades / students

print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_4_and_499:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_3_and_399:.2f}%")
print(f"Fail: {percent_failed:.2f}%")
print(f"Average: {avg_grade:.2f}")
