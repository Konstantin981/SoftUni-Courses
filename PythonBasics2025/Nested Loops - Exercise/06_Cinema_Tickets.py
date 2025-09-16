kids_tickets = 0
student_tickets = 0
standard_tickets = 0
total_tickets = 0

while True:
    film_name = input()

    if film_name == "Finish":
        break

    capacity = int(input())
    counter = 0
    while counter < capacity:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "kid":
            kids_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1

        counter += 1
        total_tickets += 1

    percent = counter / capacity * 100
    print(f"{film_name} - {percent:.2f}% full.")

print(f"Total tickets: {total_tickets}")
student_percent = student_tickets / total_tickets * 100
standard_percent = standard_tickets / total_tickets * 100
kids_percent = kids_tickets / total_tickets * 100
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kids_percent:.2f}% kids tickets.")

