from ArcTrigH import trig
from math import sqrt

def RightTriangle(side_a=None, side_b=None, side_c=None, angle_a=None, angle_c=None):
    if angle_a is None and angle_c is None:
            if side_a is not None and side_c is not None :
                angle_a = trig.arccosecant(side_c/side_a).degrees()
            elif side_b is not None and side_c is not None :
                angle_a = trig.arcsecant(side_c/side_b).degrees()
            elif side_a is not None and side_b is not None :
                angle_a = trig.arccot(side_b/side_a).degrees()
            else:
                raise ValueError("Not enough sides to determine angles")
            
            angle_c = 90 - angle_a
    
    if angle_a is None:
        angle_a = 90 - angle_c
    if angle_c is None:
        angle_c = 90 - angle_a

    if side_a is not None and side_b is not None:
        side_c = sqrt(side_a**2 + side_b**2)
    elif side_a is not None and side_c is not None:
        side_b = sqrt(side_c**2 - side_a**2)
    elif side_b is not None and side_c is not None:
        side_a = sqrt(side_c**2 - side_b**2)

    return {"Side A": side_a,
            "Side B": side_b,
            "Side C": side_c,
            "Angle A": angle_a,
            "Angle B": 90,
            "Angle C": angle_c}
        
if __name__ == "__main__": 
    result = RightTriangle(side_a=4, side_c=30)
    for k,v in result.items():
        print(f'{k} - {v}')