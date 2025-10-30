students = {}
command = input()
while ":" in command:
    tokens = command.split(":")
    name = tokens[0]
    id = tokens[1]
    course = tokens[2]
    students[name] = {}
    students[name][id] = [course]
    command = input()

searched_course = command.replace("_", " ")
for name, inner_dict in students.items():
    for id, course_list in inner_dict.items():
        if course_list[0] == searched_course:
            print(f"{name} - {id}") 