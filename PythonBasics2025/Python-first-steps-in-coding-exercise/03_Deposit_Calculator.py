deposited = float(input())
term = int(input())
annual_rate = float(input()) / 100
amount = deposited + term * ((deposited * annual_rate) / 12)
print(amount)