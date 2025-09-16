coffees = 0
while True:
    string = input()
    if string == "END":
        break
    if string == "coding":
        coffees += 1
    elif string == "CODING":
        coffees += 2
    elif string == "cat":
        coffees += 1
    elif string == "CAT":
        coffees += 2
    elif string == "dog":
        coffees += 1
    elif string == "DOG":
        coffees += 2
    elif string == "movie":
        coffees += 1
    elif string == "MOVIE":
        coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)