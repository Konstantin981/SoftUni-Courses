secret_message = input().split()
deciphered_message = []
for message in secret_message:
    message = list(message)
    numbers_as_string = ""
    for i in range(len(message)):
        if message[i].isdigit():
            numbers_as_string += message[i]
        else:
            index = i
            break
    encoded_letter = chr(int(numbers_as_string))
    message = [encoded_letter] + message[index:]
    message[1], message[-1] = message[-1], message[1]
    deciphered_message.append("".join(message))
print(" ".join(deciphered_message))