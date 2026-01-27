from ArcTrigH import trig, Degrees

if __name__ == "__main__":
    """Example Usage:"""
    radians = Degrees(50).radians()
    cos = trig.cos(radians) # 0.6427876096865394
    arcsin = trig.arcsin(cos).degrees() # 40.00000000000001

    result = trig.SolveRightTriangle(side_a=22, side_b=68)

    for k,v in result.items():
        print(f"{k} - {v:.3f}")