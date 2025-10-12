notes = [0]*10
while True:
    command = input()
    if command == "End":
        break
    note = command.split("-")
    index = int(note[0]) - 1
    task = note[1]
    notes.pop(index)
    notes.insert(index, task)
new_notes = [note for note in notes if note!=0]
print(new_notes)
