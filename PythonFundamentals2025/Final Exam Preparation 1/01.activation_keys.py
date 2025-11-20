raw_activation_key = input()
command = input()
while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        way = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if way == "Upper":
            raw_activation_key = (raw_activation_key[0:start_index]
                                  + raw_activation_key[start_index:end_index].upper()
                                  + raw_activation_key[end_index:])
            print(raw_activation_key)
        elif way == "Lower":
            raw_activation_key = (raw_activation_key[0:start_index]
                                  + raw_activation_key[start_index:end_index].lower()
                                  + raw_activation_key[end_index:])
            print(raw_activation_key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[0:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
    command = input()
print(f"Your activation key is: {raw_activation_key}")