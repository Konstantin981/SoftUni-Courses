first_string = input()
second_string = input()
for character_index in range(0, len(first_string)):
    left_part = second_string[:character_index+1]
    right_part = first_string[character_index+1:]
    new_string = left_part + right_part
    if first_string[character_index] != second_string[character_index]:
        print(new_string)