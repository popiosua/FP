"""
  Utility module to work with integer numbers
"""

def gcd(a, b):
    """
    Return the greatest common divisor of two positive integers.
    a,b integer numbers
    return an integer number, the  greatest common divisor of a and b
    """
    if a < 0 or b < 0:
        raise ValueError("a and b must be greater than 0")
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined")
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def test_gcd():
    """
      test function for gdc
    """
    assert gcd(0, 2) == 2
    assert gcd(2, 0) == 2
    assert gcd(2, 3) == 1
    assert gcd(2, 4) == 2
    assert gcd(6, 4) == 2
    assert gcd(24, 9) == 3
    try:
        gcd(-2, 0)
        gcd(0, -2)
        gcd(0, 0)
        assert False
    except ValueError:
        assert True
test_gcd()