n = int(input())
musala_count = 0
mont_blanc_count = 0
kilimanjaro_count = 0
K2_count = 0
everest_count = 0
all = 0

for i in range(1, n+1):
    group = int(input())
    if group<=5:
        musala_count += group
        all += group

    elif 6<=group<=12:
        mont_blanc_count += group
        all += group

    elif 13<=group<=25:
        kilimanjaro_count += group
        all += group

    elif 26<=group<=40:
        K2_count += group
        all += group

    elif group>=41:
        everest_count += group
        all+=group

musala_percent = musala_count/all*100
mont_blanc_percent = mont_blanc_count/all*100
kilimanjaro_percent  = kilimanjaro_count/all*100
K2_percent = K2_count/all*100
everest_percent = everest_count/all*100

print(f"{musala_percent:.2f}%")
print(f"{mont_blanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{K2_percent:.2f}%")
print(f"{everest_percent:.2f}%")