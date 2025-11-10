string = input()
final_string = ""
for char in string:
    if char not in final_string:
        final_string += char
    elif char != final_string[-1]:
        final_string+=char
print(final_string)