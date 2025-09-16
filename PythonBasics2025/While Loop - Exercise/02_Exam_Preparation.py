poor_grades_limit= int(input())
poor_grades = 0
grades_sum = 0
grades_count = 0

while True:
    problem_name = input()

    if problem_name == "Enough":
        avg_grade = grades_sum/grades_count
        print(f"Average score: {avg_grade:.2f}")
        print(f"Number of problems: {grades_count}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        poor_grades += 1
        if poor_grades_limit == poor_grades:
            print(f"You need a break, {poor_grades} poor grades.")
            break

    grades_sum += grade
    grades_count += 1
    last_problem = problem_name