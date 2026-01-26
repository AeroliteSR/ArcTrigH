from ArcTrigH import trig, Degrees, Radians, Coords

if __name__ == "__main__":
    """Example Usage:"""
    radians = Degrees(50).to_radians()
    cos = trig.cos(radians)
    arcsin = trig.arcsin(cos).to_degrees()
    print("cosine: ", cos) # 0.6427876096865394
    print("arcsin: ", arcsin) # 40.00000000000001