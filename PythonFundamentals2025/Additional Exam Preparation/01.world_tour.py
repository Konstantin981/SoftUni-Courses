stops = input()
command = input()
while command!="Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0<=index<=len(stops)-1:
            left_part = stops[:index]
            right_part = stops[index:]
            stops = left_part + string+ right_part
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0<=start_index<=len(stops)-1 and 0<=end_index<=len(stops)-1 and start_index <= end_index:
            left_part = stops[:start_index]
            right_part = stops[end_index+1:]
            stops = left_part + right_part
    elif action == "Switch":
        old_string= command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")