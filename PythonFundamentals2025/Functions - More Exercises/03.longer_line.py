import math
def center_point(x1, y1, x2, y2):
    coordinates = ()
    length1 = math.sqrt(x1**2 + y1**2)
    length2 = math.sqrt(x2**2 + y2**2)
    x1 = math.floor(x1)
    y1 = math.floor(y1)
    x2 = math.floor(x2)
    y2 = math.floor(y2)
    if length1 <= length2:
        return 1
    elif length1 > length2:
        return 2
def longer_line(x1, y1, x2, y2, x3, y3, x4, y4) ->tuple:
    coordinates1 = ()
    coordinates2 = ()
    line1 = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    line2 = math.sqrt(abs(x3 - x4)**2 + abs(y3 - y4)**2)
    if line1 >= line2:
        if (center_point(x1, y1, x2, y2) == 1):
            x1 = math.floor(x1)
            y1 = math.floor(y1)
            x2 = math.floor(x2)
            y2 = math.floor(y2)
            coordinates1 = (x1, y1)
            coordinates2 = (x2, y2)
        else:
            x1 = math.floor(x1)
            y1 = math.floor(y1)
            x2 = math.floor(x2)
            y2 = math.floor(y2)
            coordinates1 = (x2, y2)
            coordinates2 = (x1, y1)
    else:
        if (center_point(x3, y3, x4, y4) == 1):
            x3 = math.floor(x3)
            y3 = math.floor(y3)
            x4 = math.floor(x4)
            y4 = math.floor(y4)
            coordinates1 = (x3, y3)
            coordinates2 = (x4, y4)
        else:
            x3 = math.floor(x3)
            y3 = math.floor(y3)
            x4 = math.floor(x4)
            y4 = math.floor(y4)
            coordinates1 = (x4, y4)
            coordinates2 = (x3, y3)
    return coordinates1, coordinates2
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
coord1,coord2 = longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
print(coord1, end = "")
print(coord2)
