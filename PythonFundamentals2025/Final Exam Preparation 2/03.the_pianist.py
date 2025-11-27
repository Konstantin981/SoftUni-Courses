def Add(pieces_dict:dict, command:list)->dict:
    piece,composer,key = command[1], command[2], command[3]
    if piece not in pieces_dict:
        pieces_dict[piece] = []
        pieces_dict[piece].append(composer)
        pieces_dict[piece].append(key)
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return pieces_dict

def Remove(pieces_dict:dict, piece:str)->dict:
    if piece in pieces_dict:
        del pieces_dict[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces_dict

def ChangeKey(pieces_dict:dict, command:list)->dict:
    piece, new_key = command[1], command[2]
    if piece in pieces_dict:
        pieces_dict[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces_dict

n = int(input())
pieces = {}
for i in range(n):
    command = input().split("|")
    piece,composer,key = command[0], command[1], command[2]
    pieces[piece] = []
    pieces[piece].append(composer)
    pieces[piece].append(key)

command = input()
while command!="Stop":
    command = command.split("|")
    action = command[0]
    if action=="Add":
        pieces = Add(pieces, command)
    elif action=="Remove":
        pieces = Remove(pieces, command[1])
    elif action=="ChangeKey":
        pieces = ChangeKey(pieces, command)
    command = input()

for piece, lst in pieces.items():
    print(f"{piece} -> Composer: {lst[0]}, Key: {lst[1]}")