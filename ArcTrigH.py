from __future__ import annotations
import cmath
from math import pi, sqrt
import numpy as np
from functools import wraps
from numbers import Real
from dataclasses import dataclass

class Constants():
    IMAG_TOLERANCE = 1e-12
    d2r = pi/180
    r2d = 180/pi

def parseComplex(function):
    """Converts real-valued results to Radians.
        If the underlying function returns a complex value with a non-negligible
        imaginary part, the complex value is returned unchanged."""
    @wraps(function)
    def wrapper(x) -> Radians | complex:
        y = function(x)
        if isinstance(y, complex) and abs(y.imag) < Constants.IMAG_TOLERANCE:
            return Radians(y.real)
        if isinstance(y, Real):
            return Radians(y)
        return y
    return wrapper

def listFuncs(cls: type):
    for attr_name in dir(cls):
        if attr_name.startswith("_"):
            continue
        attr = getattr(cls, attr_name)
        if callable(attr):
            print(attr_name)

class Radians(float):
    __slots__ = ()
    def __new__(cls, value: float):
        return super().__new__(cls, value)
    
    def degrees(self) -> Degrees:
        return Degrees(self * Constants.r2d)

class Degrees(float):
    __slots__ = ()
    def __new__(cls, value: float):
        return super().__new__(cls, value)

    def radians(self) -> Radians:
        return Radians(self * Constants.d2r)

@dataclass
class Coords:
    x: float
    y: float

class Basic():
    """Basic Functions:"""
    @staticmethod
    @parseComplex
    def sin(x: Radians) -> float | complex:
        return cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def cos(x: Radians) -> float | complex:
        return cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def tan(x: Radians) -> float | complex:
        return cmath.tan(x)
    
    @staticmethod
    @parseComplex
    def csc(x: Radians) -> float | complex:
        return 1 / cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def sec(x: Radians) -> float | complex:
        return 1 / cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def cot(x: Radians) -> float | complex:
        return 1 / cmath.tan(x)

class Inverse():
    """Inverse Functions:"""
    @staticmethod
    @parseComplex
    def arcsin(x: float) -> Radians | complex:
        return cmath.asin(x)
    
    @staticmethod
    @parseComplex
    def arccos(x: float) -> Radians | complex:
        return cmath.acos(x)
    
    @staticmethod
    @parseComplex
    def arctan(x: float) -> Radians | complex:
        return cmath.atan(x)
    
    @staticmethod
    @parseComplex
    def arccos(x: float) -> Radians | complex:
        return cmath.asin(1 / x)
    
    @staticmethod
    @parseComplex
    def arcsec(x: float) -> Radians | complex:
        y = cmath.acos(1 / x)
        if y.real < 0:
            return y + cmath.tau
        return y
    
    @staticmethod
    @parseComplex
    def arccot(x: float | complex) -> Radians | complex:
        return pi / 2 - cmath.atan(x)

class Hyperbolic():
    """Hyperbolic Functions:"""
    @staticmethod
    @parseComplex
    def sinH(x: Radians) -> float | complex:
        return cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def cosH(x: Radians) -> float | complex:
        return cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def tanH(x: Radians) -> float | complex:
        return cmath.tanh(x)
    
    @staticmethod
    @parseComplex
    def cscH(x: Radians) -> float | complex:
        return 1 / cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def secH(x: Radians) -> float | complex:
        return 1 / cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def cotH(x: Radians) -> float | complex:
        return 1 / cmath.tanh(x)

class InverseHyperbolic():
    """Inverse Hyperbolic Functions:"""
    @staticmethod
    @parseComplex
    def arcsinH(x: float) -> float | complex:
        return cmath.asinh(x)
    
    @staticmethod
    @parseComplex
    def arccosH(x: float) -> float | complex:
        return cmath.acosh(x)
    
    @staticmethod
    @parseComplex
    def arctanH(x: float) -> float | complex:
        return cmath.atanh(x)
    
    @staticmethod
    @parseComplex
    def arccscH(x: float) -> float | complex:
        return cmath.asinh(1 / x)
    
    @staticmethod
    @parseComplex
    def arcsecH(x: float) -> float | complex:
        return cmath.acosh(1 / x)
    
    @staticmethod
    @parseComplex
    def arccotH(x: float) -> float | complex:
        return cmath.atanh(1 / x)

class Advanced():
    """Advanced Functions:"""
    @staticmethod
    @parseComplex
    def versine(x: Radians) -> float | complex:
        return 1 - cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def coversine(x: Radians) -> float | complex:
        return 1 - cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def vercosine(x: Radians) -> float | complex:
        return 1 + cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def covercosine(x: Radians) -> float | complex:
        return 1 + cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def haversine(x: Radians) -> float | complex:
        return (1 - cmath.cos(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacoversine(x: Radians) -> float | complex:
        return (1 - cmath.sin(x)) / 2
    
    @staticmethod
    @parseComplex
    def havercosine(x: Radians) -> float | complex:
        return (1 + cmath.cos(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacovercosine(x: Radians) -> float | complex:
        return (1 + cmath.sin(x)) / 2
    
    @staticmethod
    @parseComplex
    def exsecant(x: Radians) -> float | complex:
        return 1 / cmath.cos(x) - 1
    
    @staticmethod
    @parseComplex
    def excosecant(x: Radians) -> float | complex:
        return 1 / cmath.sin(x) - 1
    
    @staticmethod
    @parseComplex
    def chord(x: Radians) -> float | complex:
        return 2 * cmath.sin(x / 2)

class InverseAdvanced():
    """Inverse Advanced Functions:"""
    @staticmethod
    @parseComplex
    def arcversine(x: Radians) -> Radians | complex:
        return cmath.acos(1 - x)
    
    @staticmethod
    @parseComplex
    def arccoversine(x: Radians) -> Radians | complex:
        return cmath.asin(1 - x)
    
    @staticmethod
    @parseComplex
    def arcvercosine(x: Radians) -> Radians | complex:
        return cmath.acos(x - 1)
    
    @staticmethod
    @parseComplex
    def arccovercosine(x: Radians) -> Radians | complex:
        return cmath.asin(x - 1)
    
    @staticmethod
    @parseComplex
    def archaversine(x: Radians) -> Radians | complex:
        return cmath.acos(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archacoversine(x: Radians) -> Radians | complex:
        return cmath.asin(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archavercosine(x: Radians) -> Radians | complex:
        return cmath.acos(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def archacovercosine(x: Radians) -> Radians | complex:
        return cmath.asin(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def arcexsecant(x: Radians) -> Radians | complex:
        return cmath.acos(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcexcosecant(x: Radians) -> Radians | complex:
        return cmath.asin(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcchord(x: Radians) -> Radians | complex:
        return cmath.asin(x / 2) * 2

class HyperbolicAdvanced():
    """Hyperbolic Advanced Functions:"""
    @staticmethod
    @parseComplex
    def versineH(x: Radians) -> float | complex:
        return 1 - cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def coversineH(x: Radians) -> float | complex:
        return 1 - cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def vercosineH(x: Radians) -> float | complex:
        return 1 + cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def covercosineH(x: Radians) -> float | complex:
        return 1 + cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def haversineH(x: Radians) -> float | complex:
        return (1 - cmath.cosh(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacoversineH(x: Radians) -> float | complex:
        return (1 - cmath.sinh(x)) / 2
    
    @staticmethod
    @parseComplex
    def havercosineH(x: Radians) -> float | complex:
        return (1 + cmath.cosh(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacovercosineH(x: Radians) -> float | complex:
        return (1 + cmath.sinh(x)) / 2
    
    @staticmethod
    @parseComplex
    def exsecantH(x: Radians) -> float | complex:
        return 1 / cmath.cosh(x) - 1
    
    @staticmethod
    @parseComplex
    def excosecantH(x: Radians) -> float | complex:
        return 1 / cmath.sinh(x) - 1
    
    @staticmethod
    @parseComplex
    def chordH(x: Radians) -> float | complex:
        return 2 * cmath.sinh(x/2)

class InverseHyperbolicAdvanced():
    """Inverse Hyperbolic Advanced Functions:"""
    @staticmethod
    @parseComplex
    def arcversineH(x: Radians) -> Radians | complex:
        return cmath.acosh(1 - x)
    
    @staticmethod
    @parseComplex
    def arccoversineH(x: Radians) -> Radians | complex:
        return cmath.asinh(1 - x)
    
    @staticmethod
    @parseComplex
    def arcvercosineH(x: Radians) -> Radians | complex:
        return cmath.acosh(x - 1)
    
    @staticmethod
    @parseComplex
    def arccovercosineH(x: Radians) -> Radians | complex:
        return cmath.asinh(x - 1)
    
    @staticmethod
    @parseComplex
    def archaversineH(x: Radians) -> Radians | complex:
        return cmath.acosh(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archacoversineH(x: Radians) -> Radians | complex:
        return cmath.asinh(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archavercosineH(x: Radians) -> Radians | complex:
        return cmath.acosh(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def archacovercosineH(x: Radians) -> Radians | complex:
        return cmath.asinh(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def arcexsecantH(x: Radians) -> Radians | complex:
        return cmath.acosh(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcexcosecantH(x: Radians) -> Radians | complex:
        return cmath.asinh(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcchordH(x: Radians) -> Radians | complex:
        m = cmath.sqrt(2 * x**2 + 1)

        v = cmath.log((1 + m + cmath.sqrt(2 * (x**2 + m - 1))) / 2)
        if x.real < 0 or x.real == 0 and x.imag < 0:
            return -v
        return v

class trig(Basic,
           Inverse,
           Hyperbolic,
           InverseHyperbolic,
           Advanced,
           InverseAdvanced,
           HyperbolicAdvanced,
           InverseHyperbolicAdvanced):
    
    
    @classmethod
    def inject(cls):
        """Inject all static methods into the caller's global namespace. Messes with autocomplete tho"""
        import inspect
        caller_globals = inspect.stack()[1].frame.f_globals
        for name in dir(cls):
            attr = getattr(cls, name)
            if callable(attr) and not name.startswith("__"):
                caller_globals[name] = attr
    
    """Special Functions:"""
    @staticmethod
    def arctan2(coords: Coords) -> Radians:
        """Two-argument arctangent. Returns angle in radians in the range (-π, π]."""
        return Radians(np.atan2(coords.y, coords.x))
    
    @staticmethod
    def SolveRightTriangle(side_a=None, side_b=None, side_c=None, angle_a=None, angle_c=None):
        """Solve all missing values for a right triangle based on input.
        Angle A is adjacent to Sides A and C(hypotenuse), and opposite B
        Angle B is 90
        Angle C is adjacent to Sides B and C, and opposite A
        I simply prefer this convention."""
        if sum(x is not None for x in [side_a, side_b, side_c, angle_a, angle_c]) < 2:
            raise ValueError("At least two values are needed to solve the triangle")
    
        # fetch angles based on sides if none are given
        if angle_a is None and angle_c is None:
                if side_a is not None and side_b is not None :
                    angle_a = trig.arctan(side_b/side_a).degrees()
                elif side_a is not None and side_c is not None :
                    angle_a = trig.arcsin(side_a/side_c).degrees()
                elif side_b is not None and side_c is not None :
                    angle_a = trig.arcsin(side_b/side_c).degrees()
                else:
                    raise ValueError("Not enough sides to determine angles")
                
                angle_c = 90 - angle_a
        
        # get missing angle if one already exists
        if angle_a is None:
            angle_a = 90 - angle_c
        if angle_c is None:
            angle_c = 90 - angle_a

        # get missing sides with pythagoras if 2 are given
        if side_a is not None and side_b is not None and side_c is None:
            side_c = sqrt(side_a**2 + side_b**2)
        elif side_a is not None and side_c is not None and side_b is None:
            side_b = sqrt(side_c**2 - side_a**2)
        elif side_b is not None and side_c is not None and side_a is None:
            side_a = sqrt(side_c**2 - side_b**2)

        # get missing sides with trig if only 1 is given
        if side_a is not None and side_b is None and side_c is None:
            side_b = side_a * trig.tan(Degrees(angle_a).radians())
            side_c = sqrt(side_a**2 + side_b**2)
        elif side_b is not None and side_a is None and side_c is None:
            side_a = side_b * trig.cot(Degrees(angle_a).radians())
            side_c = sqrt(side_a**2 + side_b**2)
        elif side_c is not None and side_a is None and side_b is None:
            side_a = side_c * trig.sin(Degrees(angle_a).radians())
            side_b = side_c * trig.cos(Degrees(angle_a).radians())

        perimeter = side_a+side_b+side_c

        return {"Side A": side_a,
                "Side B": side_b,
                "Side C": side_c,
                "Angle A": angle_a,
                "Angle B": 90,
                "Angle C": angle_c,
                "Perimeter": perimeter,
                "Area": side_a*side_b/2,
                "Inradius": (side_a*side_b)/perimeter,
                "Circumradius": side_c/2,
                "Height": side_a*side_b/side_c}