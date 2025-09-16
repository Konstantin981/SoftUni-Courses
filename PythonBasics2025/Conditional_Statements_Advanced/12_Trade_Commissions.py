city = input()
sales = float(input())

trade_commission = -1

if city == "Sofia":
    if 0 <= sales <= 500:
        trade_commission = 0.05*sales
    elif 500 < sales <= 1000:
        trade_commission = 0.07*sales
    elif 1000 < sales <= 10000:
        trade_commission = 0.08*sales
    elif sales > 10000:
        trade_commission = 0.12*sales
    else:
        print("error")
elif city == "Varna":
    if 0 <= sales <= 500:
        trade_commission = 0.045*sales
    elif 500 < sales <= 1000:
        trade_commission = 0.075*sales
    elif 1000 < sales <= 10000:
        trade_commission = 0.1*sales
    elif sales > 10000:
        trade_commission = 0.13*sales
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        trade_commission = 0.055*sales
    elif 500 < sales <= 1000:
        trade_commission = 0.08*sales
    elif 1000 < sales <= 10000:
        trade_commission = 0.12*sales
    elif sales > 10000:
        trade_commission = 0.145*sales
    else:
        print("error")
else:
    print("error")

if trade_commission != -1:
    print(F"{trade_commission:.2f}")
