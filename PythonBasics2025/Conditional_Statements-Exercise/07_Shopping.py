budget = float(input())
N = int(input())
M = int(input())
P = int(input())

N_total = N*250
M_total = (0.35*N_total)*M
P_total = (0.1 * N_total)*P

total = N_total + M_total + P_total
if N>M:
    total = total*0.85

if budget>=total:
    print(f"You have {(budget-total):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total-budget):.2f} leva more!")