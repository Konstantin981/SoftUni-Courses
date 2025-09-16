figure = input()
shape_area = 0.0

from math import pi

if figure=="square":
    side = float(input())
    shape_area = side*side
elif figure=="rectangle":
    lenght = float(input())
    width = float(input())
    shape_area = lenght*width
elif figure == "circle":
    radius = float(input())
    shape_area = pi*radius*radius
elif figure == "triangle":
    base = float(input())
    height = float(input())
    shape_area = base*height/2

print(f"{shape_area:.3f}")