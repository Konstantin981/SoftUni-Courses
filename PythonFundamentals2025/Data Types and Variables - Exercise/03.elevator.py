people = int(input())
capacity = int(input())
full_courses = people // capacity
people_left = people - capacity * full_courses
if full_courses <= 1 and people_left == 0:
    print("1")
elif people_left == 0:
    print(full_courses)
else:
    print(full_courses+1)