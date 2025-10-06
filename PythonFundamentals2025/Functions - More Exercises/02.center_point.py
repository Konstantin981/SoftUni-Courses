import math
def center_point(x1, y1, x2, y2) ->tuple:
    coordinates = ()
    length1 = math.sqrt(x1**2 + y1**2)
    length2 = math.sqrt(x2**2 + y2**2)
    x1 = math.floor(x1)
    y1 = math.floor(y1)
    x2 = math.floor(x2)
    y2 = math.floor(y2)
    if length1 <= length2:
        coordinates = (x1, y1)
    elif length1 > length2:
        coordinates = (x2, y2)
    return coordinates
xone = float(input())
yone = float(input())
xtwo = float(input())
ytwo = float(input())
result = center_point(xone, yone, xtwo, ytwo)
print(result)