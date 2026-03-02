from __future__ import annotations
import cmath
from math import pi, sqrt
import numpy as np
from functools import wraps
from typing import Callable, TypeVar, ParamSpec
from dataclasses import dataclass

class Constants:
    IMAG_TOLERANCE = 1e-12
    d2r = pi/180
    r2d = 180/pi

    autoRadians = True # assumes inputs are degrees and converts them to radians automatically. Bypass by wrapping with Radians()
    autoDegrees = True # automatically converts outputted Radians to Degrees for relevant inverse functions

    @classmethod
    def snapshot(cls) -> dict:
        return {
            k: v
            for k, v in cls.__dict__.items()
            if not k.startswith("__") and not callable(v)
        }

    @classmethod
    def restore(cls, obj: dict):
        for key, value in obj.items():
            setattr(cls, key, value)

P = ParamSpec("P")
R = TypeVar("R")
def parseComplex(func: Callable[P, R] | None = None, *, convert: bool = False,) -> Callable[[Callable[P, R]], Callable[P, Degrees | Radians | complex]] | Callable[P, Degrees | Radians | complex]:

    def decorator(function: Callable[P, R]):
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Degrees | Radians | complex:
            y = function(*args, **kwargs)

            if isinstance(y, complex) and abs(y.imag) < Constants.IMAG_TOLERANCE:
                y = y.real

            # Wrap floats into Radians if original return was Radians
            if isinstance(y, float) and function.__annotations__.get("return") in (Radians, Radians | complex):
                y = Radians(y)

            if convert and Constants.autoDegrees:
                print("Output auto-converted from Radians to Degrees")
                y = toDegrees(y)

            return y

        return wrapper

    # If used as @parseComplex
    if func is not None:
        return decorator(func)

    # If used as @parseComplex(convert=True)
    return decorator

def listFuncs(cls: type):
    for attr_name in dir(cls):
        if attr_name.startswith("_"):
            continue
        attr = getattr(cls, attr_name)
        if callable(attr):
            print(attr_name)

def toRadians(obj: Degrees) -> Radians:
    if isinstance(obj, complex):
        print("Degrees are complex, discarding non-real elements.")
        obj = obj.real
    return Radians(obj * Constants.d2r)

def toDegrees(obj: Radians) -> Degrees:
    if isinstance(obj, complex):
        print("Radians are complex, discarding non-real elements.")
        obj = obj.real
    return Degrees(obj * Constants.r2d)

def checkFormat(x):
    if Constants.autoRadians and isinstance(x, (Degrees, int, float)):
        print("Function takes Radians, but a non-Radians object was given. Output will be converted. Wrap your value with Radians() if that was intended.")
        return toRadians(x)
    return x

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
        return cmath.sin(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def cos(x: Radians) -> float | complex:
        """cosθ = adjacent / hypotenuse"""
        return cmath.cos(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def tan(x: Radians) -> float | complex:
        """tanθ = opposite / adjacent"""
        return cmath.tan(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def csc(x: Radians) -> float | complex:
        """cscθ = 1 / sinθ"""
        return 1 / cmath.sin(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def sec(x: Radians) -> float | complex:
        """secθ = 1 / cosθ"""
        return 1 / cmath.cos(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def cot(x: Radians) -> float | complex:
        """cotθ = 1 / tanθ"""
        return 1 / cmath.tan(checkFormat(x))

class Inverse():
    """Inverse Functions:"""

    @staticmethod
    @parseComplex(convert=True)
    def arcsin(x: float) -> Radians | complex:
        """arcsin(x) = θ such that sinθ = x"""
        return cmath.asin(x)
    
    @staticmethod
    @parseComplex(convert=True)
    def arccos(x: float) -> Radians | complex:
        """arccos(x) = θ such that cosθ = x"""
        return cmath.acos(x)
    
    @staticmethod
    @parseComplex(convert=True)
    def arctan(x: float) -> Radians | complex:
        """arctan(x) = θ such that tanθ = x"""
        return cmath.atan(x)
    
    @staticmethod
    @parseComplex(convert=True)
    def arccsc(x: float) -> Radians | complex:
        """arccsc(x) = arcsin(1 / x)"""
        return cmath.asin(1 / x)
    
    @staticmethod
    @parseComplex(convert=True)
    def arcsec(x: float) -> Radians | complex:
        """arcsec(x) = arccos(1 / x)"""
        return cmath.acos(1 / x)
    
    @staticmethod
    @parseComplex(convert=True)
    def arccot(x: float | complex) -> Radians | complex:
        """arccot(x) = π/2 - arctan(x)"""
        return pi / 2 - cmath.atan(x)

class Hyperbolic():
    """Hyperbolic Functions:"""

    @staticmethod
    @parseComplex
    def sinH(x: Radians) -> float | complex:
        """sinh(x) = (eˣ - e⁻ˣ) / 2"""
        return cmath.sinh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def cosH(x: Radians) -> float | complex:
        """cosh(x) = (eˣ + e⁻ˣ) / 2"""
        return cmath.cosh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def tanH(x: Radians) -> float | complex:
        """tanh(x) = sinh(x) / cosh(x)"""
        return cmath.tanh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def cscH(x: Radians) -> float | complex:
        """csch(x) = 1 / sinh(x)"""
        return 1 / cmath.sinh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def secH(x: Radians) -> float | complex:
        """sech(x) = 1 / cosh(x)"""
        return 1 / cmath.cosh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def cotH(x: Radians) -> float | complex:
        """coth(x) = 1 / tanh(x)"""
        return 1 / cmath.tanh(checkFormat(x))

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
        """arcosh(x) = ln(x + √(x - 1)√(x + 1))"""
        return cmath.acosh(x)
    
    @staticmethod
    @parseComplex
    def arctanH(x: float) -> float | complex:
        """artanh(x) = ½ ln((1 + x)/(1 - x))"""
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
        """versinθ = 1 - cosθ"""
        return 1 - cmath.cos(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def coversine(x: Radians) -> float | complex:
        """coversinθ = 1 - sinθ"""
        return 1 - cmath.sin(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def vercosine(x: Radians) -> float | complex:
        """vercosθ = 1 + cosθ"""
        return 1 + cmath.cos(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def covercosine(x: Radians) -> float | complex:
        """covercosθ = 1 + sinθ"""
        return 1 + cmath.sin(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def haversine(x: Radians) -> float | complex:
        """haversinθ = (1 - cosθ) / 2"""
        return (1 - cmath.cos(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def hacoversine(x: Radians) -> float | complex:
        """hacoversinθ = (1 - sinθ) / 2"""
        return (1 - cmath.sin(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def havercosine(x: Radians) -> float | complex:
        """havercosθ = (1 + cosθ) / 2"""
        return (1 + cmath.cos(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def hacovercosine(x: Radians) -> float | complex:
        """hacovercosθ = (1 + sinθ) / 2"""
        return (1 + cmath.sin(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def exsecant(x: Radians) -> float | complex:
        """exsecθ = secθ - 1"""
        return 1 / cmath.cos(checkFormat(x)) - 1
    
    @staticmethod
    @parseComplex
    def excosecant(x: Radians) -> float | complex:
        """excscθ = cscθ - 1"""
        return 1 / cmath.sin(checkFormat(x)) - 1
    
    @staticmethod
    @parseComplex
    def chord(x: Radians) -> float | complex:
        """chordθ = 2 sin(θ / 2)"""
        return 2 * cmath.sin(checkFormat(x) / 2)

class InverseAdvanced():
    """Inverse Advanced Functions:"""

    @staticmethod
    @parseComplex(convert=True)
    def arcversine(x: Radians) -> Radians | complex:
        """arcversin(x) = arccos(1 - x)"""
        return cmath.acos(1 - checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def arccoversine(x: Radians) -> Radians | complex:
        """arccoversin(x) = arcsin(1 - x)"""
        return cmath.asin(1 - checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def arcvercosine(x: Radians) -> Radians | complex:
        """arcvercos(x) = arccos(x - 1)"""
        return cmath.acos(checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def arccovercosine(x: Radians) -> Radians | complex:
        """arccovercos(x) = arcsin(x - 1)"""
        return cmath.asin(checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def archaversine(x: Radians) -> Radians | complex:
        """archaversin(x) = arccos(1 - 2x)"""
        return cmath.acos(1 - 2 * checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def archacoversine(x: Radians) -> Radians | complex:
        """archacoversin(x) = arcsin(1 - 2x)"""
        return cmath.asin(1 - 2 * checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def archavercosine(x: Radians) -> Radians | complex:
        """archavercos(x) = arccos(2x - 1)"""
        return cmath.acos(2 * checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def archacovercosine(x: Radians) -> Radians | complex:
        """archacovercos(x) = arcsin(2x - 1)"""
        return cmath.asin(2 * checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def arcexsecant(x: Radians) -> Radians | complex:
        """arcexsec(x) = arccos(1 / (x + 1))"""
        return cmath.acos(1 / (checkFormat(x) + 1))
    
    @staticmethod
    @parseComplex(convert=True)
    def arcexcosecant(x: Radians) -> Radians | complex:
        """arcexcsc(x) = arcsin(1 / (x + 1))"""
        return cmath.asin(1 / (checkFormat(x) + 1))
    
    @staticmethod
    @parseComplex(convert=True)
    def arcchord(x: Radians) -> Radians | complex:
        """arcchord(x) = 2 arcsin(x / 2)"""
        return cmath.asin(checkFormat(x) / 2) * 2

class HyperbolicAdvanced():
    """Hyperbolic Advanced Functions:"""

    @staticmethod
    @parseComplex
    def versineH(x: Radians) -> float | complex:
        """versinh(x) = 1 - cosh(x)"""
        return 1 - cmath.cosh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def coversineH(x: Radians) -> float | complex:
        """coversinh(x) = 1 - sinh(x)"""
        return 1 - cmath.sinh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def vercosineH(x: Radians) -> float | complex:
        """vercosh(x) = 1 + cosh(x)"""
        return 1 + cmath.cosh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def covercosineH(x: Radians) -> float | complex:
        """covercosh(x) = 1 + sinh(x)"""
        return 1 + cmath.sinh(checkFormat(x))
    
    @staticmethod
    @parseComplex
    def haversineH(x: Radians) -> float | complex:
        """haversinh(x) = (1 - cosh(x)) / 2"""
        return (1 - cmath.cosh(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def hacoversineH(x: Radians) -> float | complex:
        """hacoversinh(x) = (1 - sinh(x)) / 2"""
        return (1 - cmath.sinh(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def havercosineH(x: Radians) -> float | complex:
        """havercosh(x) = (1 + cosh(x)) / 2"""
        return (1 + cmath.cosh(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def hacovercosineH(x: Radians) -> float | complex:
        """hacovercosh(x) = (1 + sinh(x)) / 2"""
        return (1 + cmath.sinh(checkFormat(x))) / 2
    
    @staticmethod
    @parseComplex
    def exsecantH(x: Radians) -> float | complex:
        """exsech(x) = sech(x) - 1"""
        return 1 / cmath.cosh(checkFormat(x)) - 1
    
    @staticmethod
    @parseComplex
    def excosecantH(x: Radians) -> float | complex:
        """excsch(x) = csch(x) - 1"""
        return 1 / cmath.sinh(checkFormat(x)) - 1
    
    @staticmethod
    @parseComplex
    def chordH(x: Radians) -> float | complex:
        """chordh(x) = 2 sinh(x / 2)"""
        return 2 * cmath.sinh(checkFormat(x) / 2)

class InverseHyperbolicAdvanced():
    """Inverse Hyperbolic Advanced Functions:"""

    @staticmethod
    @parseComplex(convert=True)
    def arcversineH(x: Radians) -> Radians | complex:
        """arcversinh(x) = arccosh(1 - x)"""
        return cmath.acosh(1 - checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def arccoversineH(x: Radians) -> Radians | complex:
        """arccoversinh(x) = arcsinh(1 - x)"""
        return cmath.asinh(1 - checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def arcvercosineH(x: Radians) -> Radians | complex:
        """arcvercosh(x) = arccosh(x - 1)"""
        return cmath.acosh(checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def arccovercosineH(x: Radians) -> Radians | complex:
        """arccovercosh(x) = arcsinh(x - 1)"""
        return cmath.asinh(checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def archaversineH(x: Radians) -> Radians | complex:
        """archaversinh(x) = arccosh(1 - 2x)"""
        return cmath.acosh(1 - 2 * checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def archacoversineH(x: Radians) -> Radians | complex:
        """archacoversinh(x) = arcsinh(1 - 2x)"""
        return cmath.asinh(1 - 2 * checkFormat(x))
    
    @staticmethod
    @parseComplex(convert=True)
    def archavercosineH(x: Radians) -> Radians | complex:
        """archavercosh(x) = arccosh(2x - 1)"""
        return cmath.acosh(2 * checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def archacovercosineH(x: Radians) -> Radians | complex:
        """archacovercosh(x) = arcsinh(2x - 1)"""
        return cmath.asinh(2 * checkFormat(x) - 1)
    
    @staticmethod
    @parseComplex(convert=True)
    def arcexsecantH(x: Radians) -> Radians | complex:
        """arcexsech(x) = arccosh(1 / (x + 1))"""
        return cmath.acosh(1 / (checkFormat(x) + 1))
    
    @staticmethod
    @parseComplex(convert=True)
    def arcexcosecantH(x: Radians) -> Radians | complex:
        """arcexcsch(x) = arcsinh(1 / (x + 1))"""
        return cmath.asinh(1 / (checkFormat(x) + 1))
    
    @staticmethod
    @parseComplex(convert=True)
    def arcchordH(x: Radians) -> Radians | complex:
        """arcchordh(x) = 2 arcsinh(x / 2)"""
        return 2 * cmath.asinh(checkFormat(x)/2)

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
    def SolveTriangle(side_a=None, side_b=None, side_c=None,
                    angle_a=None, angle_b=None, angle_c=None):
        """
        Solve a triangle given any valid combination of 3 known values.
        Angles are assumed to be in degrees.
        """

        # Count inputs
        sides = {"a": side_a, "b": side_b, "c": side_c}
        angles = {"A": angle_a, "B": angle_b, "C": angle_c}
        backup = Constants.snapshot()
        Constants.autoDegrees, Constants.autoRadians = True, True
        
        # Fetch missing angle if 2 are given
        if angle_a is None and angle_b is not None and angle_c is not None:
            angle_a = 180 - angle_b - angle_c
        if angle_b is None and angle_a is not None and angle_c is not None:
            angle_b = 180 - angle_a - angle_c
        if angle_c is None and angle_a is not None and angle_b is not None:
            angle_c = 180 - angle_b - angle_a

        known_count = sum(v is not None for v in sides.values()) + \
                    sum(v is not None for v in angles.values())

        if known_count < 3:
            raise ValueError("At least three values are required.")

        # Validate sides
        for s in sides.values():
            if s is not None and s <= 0:
                raise ValueError("Sides must be positive.")

        # Validate angles
        for a in angles.values():
            if a is not None and not (0 < a < 180):
                raise ValueError("Angles must be between 0 and 180 degrees.")
        
        # Fix for AAA
        if all(s is None for s in sides.values()):
            print("No sides given. Result will be in a ratio to a hypotenuse (c) of 1.")
            side_c = 1

        # Helper aliases
        a, b, c = side_a, side_b, side_c
        A, B, C = angle_a, angle_b, angle_c

        # -------------------------
        # CASE 1: SSS
        # -------------------------
        if a and b and c:
            A = trig.arccos((b*b + c*c - a*a) / (2*b*c))
            B = trig.arccos((a*a + c*c - b*b) / (2*a*c))
            C = 180 - A - B

        # -------------------------
        # CASE 2: SAS
        # -------------------------
        elif a and b and C:
            c = sqrt(a*a + b*b - 2*a*b*trig.cos(Degrees(C)))
            A = trig.arcsin(a * trig.sin(Degrees(C)) / c)
            B = 180 - A - C

        elif a and c and B:
            b = sqrt(a*a + c*c - 2*a*c*trig.cos(Degrees(B)))
            A = trig.arcsin(a * trig.sin(Degrees(B)) / b)
            C = 180 - A - B

        elif b and c and A:
            a = sqrt(b*b + c*c - 2*b*c*trig.cos(Degrees(A)))
            B = trig.arcsin(b * trig.sin(Degrees(A)) / a)
            C = 180 - A - B

        # -------------------------
        # CASE 3: ASA or AAS
        # -------------------------
        else:
            # Get missing angle first
            if A is None:
                A = 180 - B - C
            elif B is None:
                B = 180 - A - C
            elif C is None:
                C = 180 - A - B

            # Now use Law of Sines
            if a:
                b = a * trig.sin(Degrees(B)) / trig.sin(Degrees(A))
                c = a * trig.sin(Degrees(C)) / trig.sin(Degrees(A))
            elif b:
                a = b * trig.sin(Degrees(A)) / trig.sin(Degrees(B))
                c = b * trig.sin(Degrees(C)) / trig.sin(Degrees(B))
            elif c:
                a = c * trig.sin(Degrees(A)) / trig.sin(Degrees(C))
                b = c * trig.sin(Degrees(B)) / trig.sin(Degrees(C))

        # -------------------------
        # Final Validation
        # -------------------------
        if abs(A + B + C - 180) > 1e-6:
            raise ValueError("Invalid triangle geometry.")

        # Derived values
        perimeter = a + b + c
        s = perimeter / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))

        # Restore Constants
        Constants.restore(backup)

        return {
            "Side A": a,
            "Side B": b,
            "Side C": c,
            "Angle A": A,
            "Angle B": B,
            "Angle C": C,
            "Perimeter": perimeter,
            "Area": area,
            "Inradius": area / s,
            "Circumradius": a / (2 * trig.sin(Degrees(A)))
        }

if __name__ == "__main__":
    print(trig.SolveTriangle(angle_b=30, angle_c=90, angle_a=60))
    
