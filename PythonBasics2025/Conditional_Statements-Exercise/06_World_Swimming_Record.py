record = float(input())
meters = float(input())
speed = float(input())

slowed = meters //15 * 12.5
Ivan_time = meters*speed + slowed
if Ivan_time<record:
    print(f" Yes, he succeeded! The new world record is {Ivan_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(Ivan_time-record):.2f} seconds slower.")