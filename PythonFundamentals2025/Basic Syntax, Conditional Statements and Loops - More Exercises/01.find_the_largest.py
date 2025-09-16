command = input()
for i in range (len(command)-1):
        for j in range (len(command)-1):
            left_part = command[j:j+1]
            right_part = command[j+1:j+2]
            start =command[:j]
            rest = command[j+2:]
            if ord(command[j]) < ord(command[j+1]):
                command = start + right_part + left_part + rest

print(command)