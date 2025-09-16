annual = int(input())
basketball_sneakers = 0.6*annual
basketball_clothes = 0.8*basketball_sneakers
basketball = 0.25*basketball_clothes
basketball_accessories = 0.2*basketball

total=basketball_accessories+basketball+basketball_clothes+basketball_sneakers+annual
print (f"{total:.2f}")