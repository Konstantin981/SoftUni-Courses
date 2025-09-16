PRICE_PACKAGES_PENS = 5.80
PRICE_PACKAGES_MARKERS = 7.20
PRICE_CLEANING = 1.20

number_packages_pens = int(input())
number_packages_markers = int(input())
liters_cleaning = int(input())
percent_discount = int(input())/100

sum_materials = (number_packages_pens * PRICE_PACKAGES_PENS) \
                + (number_packages_markers * PRICE_PACKAGES_MARKERS) \
                + (liters_cleaning * PRICE_CLEANING)

sum_materials = sum_materials - (sum_materials * percent_discount)
print(sum_materials)