string = input()
final_string = ""
strength = 0
for index in range(len(string)):
    if strength > 0  and string[index] != ">":
        strength-=1
    elif string[index] == ">":
        strength += int(string[index+1])
        final_string += string[index]
    else:
        final_string += string[index]
print(final_string)