QUARTER_FINAL_STANDARD = 55.50
QUARTER_FINAL_PREMIUM = 105.20
QUARTER_FINAL_VIP = 118.90

SEMI_FINAL_STANDARD = 75.88
SEMI_FINAL_PREMIUM = 125.22
SEMI_FINAL_VIP = 300.40

FINAL_STANDARD = 110.10
FINAL_PREMIUM = 160.66
FINAL_VIP = 400

PHOTO_WITH_CUP = 40

tournament_stage = input()
ticket_type = input()
ticket_count = int(input())
photo_with_cup = input()
total = 0

if tournament_stage == "Quarter final":
    if ticket_type == "Standard":
        total = QUARTER_FINAL_STANDARD * ticket_count
    elif ticket_type == "Premium":
        total = QUARTER_FINAL_PREMIUM * ticket_count
    elif ticket_type == "VIP":
        total = QUARTER_FINAL_VIP * ticket_count
elif tournament_stage == "Semi final":
    if ticket_type == "Standard":
        total = SEMI_FINAL_STANDARD * ticket_count
    elif ticket_type == "Premium":
        total = SEMI_FINAL_PREMIUM * ticket_count
    elif ticket_type == "VIP":
        total = SEMI_FINAL_VIP * ticket_count
elif tournament_stage == "Final":
    if ticket_type == "Standard":
        total = FINAL_STANDARD * ticket_count
    elif ticket_type == "Premium":
        total = FINAL_PREMIUM * ticket_count
    elif ticket_type == "VIP":
        total = FINAL_VIP * ticket_count

if total > 4000:
    total = 0.75 * total
elif total > 2500:
    total = 0.9 * total
    if photo_with_cup == "Y":
        total += ticket_count * PHOTO_WITH_CUP
else:
    if photo_with_cup == "Y":
        total += ticket_count * PHOTO_WITH_CUP


print(f"{total:.2f}")