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

def toRadians(obj):
    if isinstance(obj, complex):
        print("Degrees are complex, discarding non-real elements.")
        obj = obj.real
    return obj * Constants.d2r

def toDegrees(obj):
    if isinstance(obj, complex):
        print("Radians are complex, discarding non-real elements.")
        obj = obj.real
    return obj * Constants.r2d

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
        """sinθ = opposite / hypotenuse"""
        return cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def cos(x: Radians) -> float | complex:
        """cosθ = adjacent / hypotenuse"""
        return cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def tan(x: Radians) -> float | complex:
        """tanθ = opposite / adjacent"""
        return cmath.tan(x)
    
    @staticmethod
    @parseComplex
    def csc(x: Radians) -> float | complex:
        """cscθ = 1 / sinθ"""
        return 1 / cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def sec(x: Radians) -> float | complex:
        """secθ = 1 / cosθ"""
        return 1 / cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def cot(x: Radians) -> float | complex:
        """cotθ = 1 / tanθ"""
        return 1 / cmath.tan(x)

class Inverse():
    """Inverse Functions:"""

    @staticmethod
    @parseComplex
    def arcsin(x: float) -> Radians | complex:
        """arcsin(x) = θ such that sinθ = x"""
        return cmath.asin(x)
    
    @staticmethod
    @parseComplex
    def arccos(x: float) -> Radians | complex:
        """arccos(x) = θ such that cosθ = x"""
        return cmath.acos(x)
    
    @staticmethod
    @parseComplex
    def arctan(x: float) -> Radians | complex:
        """arctan(x) = θ such that tanθ = x"""
        return cmath.atan(x)
    
    @staticmethod
    @parseComplex
    def arccsc(x: float) -> Radians | complex:
        """arccsc(x) = arcsin(1 / x)"""
        return cmath.asin(1 / x)
    
    @staticmethod
    @parseComplex
    def arcsec(x: float) -> Radians | complex:
        """arcsec(x) = arccos(1 / x)"""
        y = cmath.acos(1 / x)
        if y.real < 0:
            return y + cmath.tau
        return y
    
    @staticmethod
    @parseComplex
    def arccot(x: float | complex) -> Radians | complex:
        """arccot(x) = π/2 − arctan(x)"""
        return pi / 2 - cmath.atan(x)

class Hyperbolic():
    """Hyperbolic Functions:"""

    @staticmethod
    @parseComplex
    def sinH(x: Radians) -> float | complex:
        """sinh(x) = (eˣ − e⁻ˣ) / 2"""
        return cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def cosH(x: Radians) -> float | complex:
        """cosh(x) = (eˣ + e⁻ˣ) / 2"""
        return cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def tanH(x: Radians) -> float | complex:
        """tanh(x) = sinh(x) / cosh(x)"""
        return cmath.tanh(x)
    
    @staticmethod
    @parseComplex
    def cscH(x: Radians) -> float | complex:
        """csch(x) = 1 / sinh(x)"""
        return 1 / cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def secH(x: Radians) -> float | complex:
        """sech(x) = 1 / cosh(x)"""
        return 1 / cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def cotH(x: Radians) -> float | complex:
        """coth(x) = 1 / tanh(x)"""
        return 1 / cmath.tanh(x)

class InverseHyperbolic():
    """Inverse Hyperbolic Functions:"""

    @staticmethod
    @parseComplex
    def arcsinH(x: float) -> float | complex:
        """arsinh(x) = ln(x + √(x² + 1))"""
        return cmath.asinh(x)
    
    @staticmethod
    @parseComplex
    def arccosH(x: float) -> float | complex:
        """arcosh(x) = ln(x + √(x − 1)√(x + 1))"""
        return cmath.acosh(x)
    
    @staticmethod
    @parseComplex
    def arctanH(x: float) -> float | complex:
        """artanh(x) = ½ ln((1 + x)/(1 − x))"""
        return cmath.atanh(x)
    
    @staticmethod
    @parseComplex
    def arccscH(x: float) -> float | complex:
        """arcsch(x) = arsinh(1 / x)"""
        return cmath.asinh(1 / x)
    
    @staticmethod
    @parseComplex
    def arcsecH(x: float) -> float | complex:
        """arsech(x) = arcosh(1 / x)"""
        return cmath.acosh(1 / x)
    
    @staticmethod
    @parseComplex
    def arccotH(x: float) -> float | complex:
        """arcoth(x) = artanh(1 / x)"""
        return cmath.atanh(1 / x)

class Advanced():
    """Advanced Functions:"""

    @staticmethod
    @parseComplex
    def versine(x: Radians) -> float | complex:
        """versinθ = 1 − cosθ"""
        return 1 - cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def coversine(x: Radians) -> float | complex:
        """coversinθ = 1 − sinθ"""
        return 1 - cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def vercosine(x: Radians) -> float | complex:
        """vercosθ = 1 + cosθ"""
        return 1 + cmath.cos(x)
    
    @staticmethod
    @parseComplex
    def covercosine(x: Radians) -> float | complex:
        """covercosθ = 1 + sinθ"""
        return 1 + cmath.sin(x)
    
    @staticmethod
    @parseComplex
    def haversine(x: Radians) -> float | complex:
        """haversinθ = (1 − cosθ) / 2"""
        return (1 - cmath.cos(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacoversine(x: Radians) -> float | complex:
        """hacoversinθ = (1 − sinθ) / 2"""
        return (1 - cmath.sin(x)) / 2
    
    @staticmethod
    @parseComplex
    def havercosine(x: Radians) -> float | complex:
        """havercosθ = (1 + cosθ) / 2"""
        return (1 + cmath.cos(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacovercosine(x: Radians) -> float | complex:
        """hacovercosθ = (1 + sinθ) / 2"""
        return (1 + cmath.sin(x)) / 2
    
    @staticmethod
    @parseComplex
    def exsecant(x: Radians) -> float | complex:
        """exsecθ = secθ − 1"""
        return 1 / cmath.cos(x) - 1
    
    @staticmethod
    @parseComplex
    def excosecant(x: Radians) -> float | complex:
        """excscθ = cscθ − 1"""
        return 1 / cmath.sin(x) - 1
    
    @staticmethod
    @parseComplex
    def chord(x: Radians) -> float | complex:
        """chordθ = 2 sin(θ / 2)"""
        return 2 * cmath.sin(x / 2)

class InverseAdvanced():
    """Inverse Advanced Functions:"""

    @staticmethod
    @parseComplex
    def arcversine(x: Radians) -> Radians | complex:
        """arcversin(x) = arccos(1 − x)"""
        return cmath.acos(1 - x)
    
    @staticmethod
    @parseComplex
    def arccoversine(x: Radians) -> Radians | complex:
        """arccoversin(x) = arcsin(1 − x)"""
        return cmath.asin(1 - x)
    
    @staticmethod
    @parseComplex
    def arcvercosine(x: Radians) -> Radians | complex:
        """arcvercos(x) = arccos(x − 1)"""
        return cmath.acos(x - 1)
    
    @staticmethod
    @parseComplex
    def arccovercosine(x: Radians) -> Radians | complex:
        """arccovercos(x) = arcsin(x − 1)"""
        return cmath.asin(x - 1)
    
    @staticmethod
    @parseComplex
    def archaversine(x: Radians) -> Radians | complex:
        """archaversin(x) = arccos(1 − 2x)"""
        return cmath.acos(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archacoversine(x: Radians) -> Radians | complex:
        """archacoversin(x) = arcsin(1 − 2x)"""
        return cmath.asin(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archavercosine(x: Radians) -> Radians | complex:
        """archavercos(x) = arccos(2x − 1)"""
        return cmath.acos(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def archacovercosine(x: Radians) -> Radians | complex:
        """archacovercos(x) = arcsin(2x − 1)"""
        return cmath.asin(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def arcexsecant(x: Radians) -> Radians | complex:
        """arcexsec(x) = arccos(1 / (x + 1))"""
        return cmath.acos(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcexcosecant(x: Radians) -> Radians | complex:
        """arcexcsc(x) = arcsin(1 / (x + 1))"""
        return cmath.asin(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcchord(x: Radians) -> Radians | complex:
        """arcchord(x) = 2 arcsin(x / 2)"""
        return cmath.asin(x / 2) * 2

class HyperbolicAdvanced():
    """Hyperbolic Advanced Functions:"""

    @staticmethod
    @parseComplex
    def versineH(x: Radians) -> float | complex:
        """versinh(x) = 1 − cosh(x)"""
        return 1 - cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def coversineH(x: Radians) -> float | complex:
        """coversinh(x) = 1 − sinh(x)"""
        return 1 - cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def vercosineH(x: Radians) -> float | complex:
        """vercosh(x) = 1 + cosh(x)"""
        return 1 + cmath.cosh(x)
    
    @staticmethod
    @parseComplex
    def covercosineH(x: Radians) -> float | complex:
        """covercosh(x) = 1 + sinh(x)"""
        return 1 + cmath.sinh(x)
    
    @staticmethod
    @parseComplex
    def haversineH(x: Radians) -> float | complex:
        """haversinh(x) = (1 − cosh(x)) / 2"""
        return (1 - cmath.cosh(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacoversineH(x: Radians) -> float | complex:
        """hacoversinh(x) = (1 − sinh(x)) / 2"""
        return (1 - cmath.sinh(x)) / 2
    
    @staticmethod
    @parseComplex
    def havercosineH(x: Radians) -> float | complex:
        """havercosh(x) = (1 + cosh(x)) / 2"""
        return (1 + cmath.cosh(x)) / 2
    
    @staticmethod
    @parseComplex
    def hacovercosineH(x: Radians) -> float | complex:
        """hacovercosh(x) = (1 + sinh(x)) / 2"""
        return (1 + cmath.sinh(x)) / 2
    
    @staticmethod
    @parseComplex
    def exsecantH(x: Radians) -> float | complex:
        """exsech(x) = sech(x) − 1"""
        return 1 / cmath.cosh(x) - 1
    
    @staticmethod
    @parseComplex
    def excosecantH(x: Radians) -> float | complex:
        """excsch(x) = csch(x) − 1"""
        return 1 / cmath.sinh(x) - 1
    
    @staticmethod
    @parseComplex
    def chordH(x: Radians) -> float | complex:
        """chordh(x) = 2 sinh(x / 2)"""
        return 2 * cmath.sinh(x / 2)

class InverseHyperbolicAdvanced():
    """Inverse Hyperbolic Advanced Functions:"""

    @staticmethod
    @parseComplex
    def arcversineH(x: Radians) -> Radians | complex:
        """arcversinh(x) = arcosh(1 − x)"""
        return cmath.acosh(1 - x)
    
    @staticmethod
    @parseComplex
    def arccoversineH(x: Radians) -> Radians | complex:
        """arccoversinh(x) = arsinh(1 − x)"""
        return cmath.asinh(1 - x)
    
    @staticmethod
    @parseComplex
    def arcvercosineH(x: Radians) -> Radians | complex:
        """arcvercosh(x) = arcosh(x − 1)"""
        return cmath.acosh(x - 1)
    
    @staticmethod
    @parseComplex
    def arccovercosineH(x: Radians) -> Radians | complex:
        """arccovercosh(x) = arsinh(x − 1)"""
        return cmath.asinh(x - 1)
    
    @staticmethod
    @parseComplex
    def archaversineH(x: Radians) -> Radians | complex:
        """archaversinh(x) = arcosh(1 − 2x)"""
        return cmath.acosh(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archacoversineH(x: Radians) -> Radians | complex:
        """archacoversinh(x) = arsinh(1 − 2x)"""
        return cmath.asinh(1 - 2 * x)
    
    @staticmethod
    @parseComplex
    def archavercosineH(x: Radians) -> Radians | complex:
        """archavercosh(x) = arcosh(2x − 1)"""
        return cmath.acosh(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def archacovercosineH(x: Radians) -> Radians | complex:
        """archacovercosh(x) = arsinh(2x − 1)"""
        return cmath.asinh(2 * x - 1)
    
    @staticmethod
    @parseComplex
    def arcexsecantH(x: Radians) -> Radians | complex:
        """arcexsech(x) = arcosh(1 / (x + 1))"""
        return cmath.acosh(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcexcosecantH(x: Radians) -> Radians | complex:
        """arcexcsch(x) = arsinh(1 / (x + 1))"""
        return cmath.asinh(1 / (x + 1))
    
    @staticmethod
    @parseComplex
    def arcchordH(x: Radians) -> Radians | complex:
        """arcchordh(x) = 2 arsinh(x / 2)"""
        m = cmath.sqrt(2 * x**2 + 1)
        v = cmath.log((1 + m + cmath.sqrt(2 * (x**2 + m - 1))) / 2)
        if x.real < 0 or (x.real == 0 and x.imag < 0):
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
    def SolveTriangle(side_a=None, side_b=None, side_c=None, angle_a=None, angle_b=None, angle_c=None):
        """Solve all missing values for a triangle based on input.
        Angle inputs are assumed to be in degrees."""

        sides = [side_a, side_b, side_c]
        angles = [angle_a, angle_b, angle_c]

        if sum(x is not None for x in sides + angles) < 3:
            raise ValueError("At least three values are required")

        if all(s is None for s in sides):
            raise ValueError("At least one side must be provided")

        for s in sides:
            if s is not None and s <= 0:
                raise ValueError("Side lengths must be positive")

        for a in angles:
            if a is not None and not (0 < a < 180):
                raise ValueError("Angles must be between 0 and 180 degrees")

        # fetch missing angle if 2 are known
        if angles.count(None) == 1:
            if angle_a is None:
                angle_a = 180 - angle_b - angle_c
            elif angle_b is None:
                angle_b = 180 - angle_a - angle_c
            elif angle_c is None:
                angle_c = 180 - angle_a - angle_b

        # sss/sas
        if side_a and side_b and side_c:
            angle_a = trig.arccos((side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)).degrees()
            angle_b = trig.arccos((side_a**2 + side_c**2 - side_b**2) / (2 * side_a * side_c)).degrees()
            angle_c = 180 - angle_a - angle_b

        elif side_a and side_b and angle_c:
            side_c = sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * trig.cos(Degrees(angle_c).radians()))
        elif side_a and side_c and angle_b:
            side_b = sqrt(side_a**2 + side_c**2 - 2 * side_a * side_c * trig.cos(Degrees(angle_b).radians()))
        elif side_b and side_c and angle_a:
            side_a = sqrt(side_b**2 + side_c**2 - 2 * side_b * side_c * trig.cos(Degrees(angle_a).radians()))

        # asa/aas
        if angle_a and angle_b and side_a and side_b is None:
            side_b = side_a * trig.sin(Degrees(angle_b).radians()) / trig.sin(Degrees(angle_a).radians())
        if angle_a and angle_c and side_a and side_c is None:
            side_c = side_a * trig.sin(Degrees(angle_c).radians()) / trig.sin(Degrees(angle_a).radians())
        if angle_b and angle_c and side_b and side_c is None:
            side_c = side_b * trig.sin(Degrees(angle_c).radians()) / trig.sin(Degrees(angle_b).radians())

        # get remaining angles
        if angle_a is None:
            angle_a = trig.arcsin(side_a * trig.sin(Degrees(angle_b).radians()) / side_b).degrees()
        if angle_b is None:
            angle_b = trig.arcsin(side_b * trig.sin(Degrees(angle_a).radians()) / side_a).degrees()
        if angle_c is None:
            angle_c = 180 - angle_a - angle_b

        # get remaining sides
        if side_a is None:
            side_a = side_b * trig.sin(Degrees(angle_a).radians()) / trig.sin(Degrees(angle_b).radians())
        if side_b is None:
            side_b = side_a * trig.sin(Degrees(angle_b).radians()) / trig.sin(Degrees(angle_a).radians())
        if side_c is None:
            side_c = side_a * trig.sin(Degrees(angle_c).radians()) / trig.sin(Degrees(angle_a).radians())

        # validation
        if angle_a + angle_b + angle_c > 180.000001:
            raise ValueError("Invalid triangle geometry")

        # derive extra values
        perimeter = side_a + side_b + side_c
        s = perimeter / 2
        area = sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

        return {
            "Side A": side_a,
            "Side B": side_b,
            "Side C": side_c,
            "Angle A": angle_a,
            "Angle B": angle_b,
            "Angle C": angle_c,
            "Perimeter": perimeter,
            "Area": area,
            "Inradius": area / s,
            "Circumradius": side_a / (2 * trig.sin(Degrees(angle_a).radians()))
        }

    
if __name__ == "__main__":
    print(trig.SolveTriangle(angle_a=24, angle_b=90, side_a=5))