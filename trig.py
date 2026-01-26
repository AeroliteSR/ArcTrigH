from __future__ import annotations
import cmath
import numpy as np
from functools import wraps
from numbers import Real

def complex2real(function):
    @wraps(function)
    def wrapper(x):
        y = function(x)
        if isinstance(x, Real):
            if abs(y.imag) < 1e-12:
                return y.real
        return y
    return wrapper

def listFuncs():
    for attr_name in dir(Functions):
        attr = getattr(Functions, attr_name)
        if callable(attr):
            print(attr_name)

class Constants():
    d2r = cmath.pi/180
    r2d = 180/cmath.pi

class Radians(float):
    def __new__(cls, value: float):
        return super().__new__(cls, value)
    
    def to_degrees(self) -> Degrees:
        return Degrees(self * Constants.r2d)

class Degrees(float):
    def __new__(cls, value: float):
        return super().__new__(cls, value)

    def to_radians(self) -> Radians:
        return Radians(self * Constants.d2r)
    
class Coords():
    def __init__(self, value: tuple[int|float, int|float]):
        self.x = value[0]
        self.y = value[1]

class Basic():
    """Basic Functions:"""
    @staticmethod
    @complex2real
    def sin(x: Radians) -> float:
        return cmath.sin(x)
    
    @staticmethod
    @complex2real
    def cos(x: Radians) -> float:
        return cmath.cos(x)
    
    @staticmethod
    @complex2real
    def tan(x: Radians) -> float:
        return cmath.tan(x)
    
    @staticmethod
    @complex2real
    def cosecant(x: Radians) -> float:
        return 1 / cmath.sin(x)
    
    @staticmethod
    @complex2real
    def secant(x: Radians) -> float:
        return 1 / cmath.cos(x)
    
    @staticmethod
    @complex2real
    def cotan(x: Radians) -> float:
        return 1 / cmath.tan(x)

class Inverse():
    """Inverse Functions:"""
    @staticmethod
    @complex2real
    def arcsin(x: float) -> Radians:
        return cmath.asin(x)
    
    @staticmethod
    @complex2real
    def arccos(x: float) -> Radians:
        return cmath.acos(x)
    
    @staticmethod
    @complex2real
    def arctan(x: float) -> Radians:
        return cmath.atan(x)
    
    @staticmethod
    @complex2real
    def arccosecant(x: float) -> Radians:
        return cmath.asin(1 / x)
    
    @staticmethod
    @complex2real
    def arcsecant(x: float) -> Radians:
        y = cmath.acos(1 / x)
        if y.real < 0:
            return y + cmath.tau
        return y
    
    @staticmethod
    @complex2real
    def arccotan(x: float) -> Radians:
        return cmath.pi / 2 - cmath.atan(x)

class Hyperbolic():
    """Hyperbolic Functions:"""
    @staticmethod
    @complex2real
    def sinH(x: Radians) -> float:
        return cmath.sinh(x)
    
    @staticmethod
    @complex2real
    def cosH(x: Radians) -> float:
        return cmath.cosh(x)
    
    @staticmethod
    @complex2real
    def tanH(x: Radians) -> float:
        return cmath.tanh(x)
    
    @staticmethod
    @complex2real
    def cosecantH(x: Radians) -> float:
        return 1 / cmath.sinh(x)
    
    @staticmethod
    @complex2real
    def secantH(x: Radians) -> float:
        return 1 / cmath.cosh(x)
    
    @staticmethod
    @complex2real
    def cotanH(x: Radians) -> float:
        return 1 / cmath.tanh(x)

class InverseHyperbolic():
    """Inverse Hyperbolic Functions:"""
    @staticmethod
    @complex2real
    def arcsinH(x: Radians) -> float:
        return cmath.asinh(x)
    
    @staticmethod
    @complex2real
    def arccosH(x: Radians) -> float:
        return cmath.acosh(x)
    
    @staticmethod
    @complex2real
    def arctanH(x: Radians) -> float:
        return cmath.atanh(x)
    
    @staticmethod
    @complex2real
    def arccosecantH(x: Radians) -> float:
        return cmath.asinh(1 / x)
    
    @staticmethod
    @complex2real
    def arcsecantH(x: Radians) -> float:
        return cmath.acosh(1 / x)
    
    @staticmethod
    @complex2real
    def arccotanH(x: Radians) -> float:
        return cmath.atanh(1 / x)

class Advanced():
    """Advanced Functions:"""
    @staticmethod
    @complex2real
    def versine(x: Radians) -> float:
        return 1 - cmath.cos(x)
    
    @staticmethod
    @complex2real
    def coversine(x: Radians) -> float:
        return 1 - cmath.sin(x)
    
    @staticmethod
    @complex2real
    def vercosine(x: Radians) -> float:
        return 1 + cmath.cos(x)
    
    @staticmethod
    @complex2real
    def covercosine(x: Radians) -> float:
        return 1 + cmath.sin(x)
    
    @staticmethod
    @complex2real
    def haversine(x: Radians) -> float:
        return (1 - cmath.cos(x)) / 2
    
    @staticmethod
    @complex2real
    def hacoversine(x: Radians) -> float:
        return (1 - cmath.sin(x)) / 2
    
    @staticmethod
    @complex2real
    def havercosine(x: Radians) -> float:
        return (1 + cmath.cos(x)) / 2
    
    @staticmethod
    @complex2real
    def hacovercosine(x: Radians) -> float:
        return (1 + cmath.sin(x)) / 2
    
    @staticmethod
    @complex2real
    def exsecant(x: Radians) -> float:
        return 1 / cmath.cos(x) - 1
    
    @staticmethod
    @complex2real
    def excosecant(x: Radians) -> float:
        return 1 / cmath.sin(x) - 1
    
    @staticmethod
    @complex2real
    def chord(x: Radians) -> float:
        return 2 * cmath.sin(x / 2)

class InverseAdvanced():
    """Inverse Advanced Functions:"""
    @staticmethod
    @complex2real
    def arcversine(x: Radians) -> float:
        return cmath.acos(1 - x)
    
    @staticmethod
    @complex2real
    def arccoversine(x: Radians) -> float:
        return cmath.asin(1 - x)
    
    @staticmethod
    @complex2real
    def arcvercosine(x: Radians) -> float:
        return cmath.acos(x - 1)
    
    @staticmethod
    @complex2real
    def arccovercosine(x: Radians) -> float:
        return cmath.asin(x - 1)
    
    @staticmethod
    @complex2real
    def archaversine(x: Radians) -> float:
        return cmath.acos(1 - 2 * x)
    
    @staticmethod
    @complex2real
    def archacoversine(x: Radians) -> float:
        return cmath.asin(1 - 2 * x)
    
    @staticmethod
    @complex2real
    def archavercosine(x: Radians) -> float:
        return cmath.acos(2 * x - 1)
    
    @staticmethod
    @complex2real
    def archacovercosine(x: Radians) -> float:
        return cmath.asin(2 * x - 1)
    
    @staticmethod
    @complex2real
    def arcexsecant(x: Radians) -> float:
        return cmath.acos(1 / (x + 1))
    
    @staticmethod
    @complex2real
    def arcexcosecant(x: Radians) -> float:
        return cmath.asin(1 / (x + 1))
    
    @staticmethod
    @complex2real
    def arcchord(x: Radians) -> float:
        return cmath.asin(x / 2) * 2

class HyperbolicAdvanced():
    """Hyperbolic Advanced Functions:"""
    @staticmethod
    @complex2real
    def versineH(x: Radians) -> float:
        return 1 - cmath.cosh(x)
    
    @staticmethod
    @complex2real
    def coversineH(x: Radians) -> float:
        return 1 - cmath.sinh(x)
    
    @staticmethod
    @complex2real
    def vercosineH(x: Radians) -> float:
        return 1 + cmath.cosh(x)
    
    @staticmethod
    @complex2real
    def covercosineH(x: Radians) -> float:
        return 1 + cmath.sinh(x)
    
    @staticmethod
    @complex2real
    def haversineH(x: Radians) -> float:
        return (1 - cmath.cosh(x)) / 2
    
    @staticmethod
    @complex2real
    def hacoversineH(x: Radians) -> float:
        return (1 - cmath.sinh(x)) / 2
    
    @staticmethod
    @complex2real
    def havercosineH(x: Radians) -> float:
        return (1 + cmath.cosh(x)) / 2
    
    @staticmethod
    @complex2real
    def hacovercosineH(x: Radians) -> float:
        return (1 + cmath.sinh(x)) / 2
    
    @staticmethod
    @complex2real
    def exsecantH(x: Radians) -> float:
        return 1 / cmath.cosh(x) - 1
    
    @staticmethod
    @complex2real
    def excosecantH(x: Radians) -> float:
        return 1 / cmath.sinh(x) - 1
    
    @staticmethod
    @complex2real
    def chordH(x: Radians) -> float:
        return 2 * cmath.sinh(x/2)

class InverseHyperbolicAdvanced():
    """Inverse Hyperbolic Advanced Functions:"""
    @staticmethod
    @complex2real
    def arcversineH(x: Radians) -> float:
        return cmath.acosh(1 - x)
    
    @staticmethod
    @complex2real
    def arccoversineH(x: Radians) -> float:
        return cmath.asinh(1 - x)
    
    @staticmethod
    @complex2real
    def arcvercosineH(x: Radians) -> float:
        return cmath.acosh(x - 1)
    
    @staticmethod
    @complex2real
    def arccovercosineH(x: Radians) -> float:
        return cmath.asinh(x - 1)
    
    @staticmethod
    @complex2real
    def archaversineH(x: Radians) -> float:
        return cmath.acosh(1 - 2 * x)
    
    @staticmethod
    @complex2real
    def archacoversineH(x: Radians) -> float:
        return cmath.asinh(1 - 2 * x)
    
    @staticmethod
    @complex2real
    def archavercosineH(x: Radians) -> float:
        return cmath.acosh(2 * x - 1)
    
    @staticmethod
    @complex2real
    def archacovercosineH(x: Radians) -> float:
        return cmath.asinh(2 * x - 1)
    
    @staticmethod
    @complex2real
    def arcexsecantH(x: Radians) -> float:
        return cmath.acosh(1 / (x + 1))
    
    @staticmethod
    @complex2real
    def arcexcosecantH(x: Radians) -> float:
        return cmath.asinh(1 / (x + 1))
    
    @staticmethod
    @complex2real
    def arcchordH(x: Radians) -> float:
        m = cmath.sqrt(2 * x**2 + 1)

        v = cmath.log((1 + m + cmath.sqrt(2 * (x**2 + m - 1))) / 2)
        if x.real < 0 or x.real == 0 and x.imag < 0:
            return -v
        return v

class Functions(Basic,
                Inverse,
                Hyperbolic,
                InverseHyperbolic,
                Advanced,
                InverseAdvanced,
                HyperbolicAdvanced,
                InverseHyperbolicAdvanced):
    
    """Special Functions:"""
    @staticmethod
    def arctan2(coords: Coords) -> Radians:
        return np.atan2(coords.y, coords.x)

if __name__ == "__main__":
    """Example Usage:"""
    radians = Degrees(50).to_radians()
    print(Functions.cos(radians))