ACCOMMODATION_PRICE = 20
TRANSPORT_CARD = 1.60
MUSEUM_TICKET = 6
UNEXPECTED_FEES = 0.25

people = int(input())
nights = int(input())
transport_cards_per_person = int(input())
museum_tickets_per_person = int(input())

total_per_person = ((nights * ACCOMMODATION_PRICE)
                    + (museum_tickets_per_person * MUSEUM_TICKET)
                    + (TRANSPORT_CARD * transport_cards_per_person))

total = total_per_person * people

total += total*UNEXPECTED_FEES
print(f"{total:.2f}")