control_minutes = int(input())
control_seconds = int(input())
meters = float(input())
seconds_per_100_meters = int(input())
Marin_time = 0

control_seconds += control_minutes * 60
Marin_time = (meters/100) * seconds_per_100_meters
Marin_time -= (meters/120) * 2.5

if Marin_time <= control_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {Marin_time:.3f}.")

elif Marin_time > control_seconds:
    print(f"No, Marin failed! He was {(Marin_time-control_seconds):.3f} second slower.")