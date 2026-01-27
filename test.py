from ArcTrigH import trig, Degrees
from math import sqrt

def getAngle(target: str, a=None, b=None, c=None):
    h = c
    if target == 'a':
        o, a = b, a
    elif target == 'c':
        o, a = a, b
    else:
        print("Invalid target")
        return
    
    if o and h:
        angle_a = trig.arccosecant(h/o).to_degrees()
    elif a and h:
        angle_a = trig.arcsecant(h/a).to_degrees()
    elif o and a:
        angle_a = trig.arccot(a/o).to_degrees()

    angle_c = 90 - angle_a

    return (angle_a, angle_c)

def RightTriangle(side_a=None, side_b=None, side_c=None, angle_a=None, angle_c=None):
    if not angle_a and not angle_c:
        angle_a, angle_c = getAngle('a', side_a, side_b, side_c)

    if angle_a and side_a:
        side_b = side_a * trig.tan(Degrees(angle_a).to_radians())
        side_c = sqrt(side_a**2 + side_b**2)
    elif angle_a and side_b:
        side_a = side_b * trig.cot(Degrees(angle_a).to_radians())
        side_c = sqrt(side_a**2 + side_b**2)
    elif angle_a and side_c:
        side_b = side_c * trig.sin(Degrees(angle_a).to_radians())
        side_a = sqrt(side_c**2 - side_b**2)

    elif angle_c and side_a:
        side_b = side_a * trig.cot(Degrees(angle_c).to_radians())
        side_c = sqrt(side_a**2 + side_b**2)
    elif angle_c and side_b:
        side_a = side_b * trig.tan(Degrees(angle_c).to_radians())
        side_c = sqrt(side_a**2 + side_b**2)
    elif angle_c and side_c:
        side_b = side_c * trig.cos(Degrees(angle_c).to_radians())
        side_a = sqrt(side_c**2 - side_b**2)

    if not angle_a:
        angle_a = getAngle('a', side_a, side_b, side_c)
    elif not angle_c:
        angle_c = getAngle('c', side_a, side_b, side_c)

    return {"Side A": side_a,
            "Side B": side_b,
            "Side C": side_c,
            "Angle A": angle_a,
            "Angle B": 90,
            "Angle C": angle_c}
        

if __name__ == "__main__": 
    result = RightTriangle(side_a=4, side_c=8)
    for k,v in result.items():
        print(f'{k} - {v}')