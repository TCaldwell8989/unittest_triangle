import math

def area(base, height):
    '''
    Compute the area of a triangle with the given base and height.
    Raises a ValueError if base or height area negative.
    '''

    if base < 0 or height < 0:
        raise ValueError('Base and height must be positive. Was given base: {}, height {}'.format(base, height))

    area = base * height / 2
    return area

def is_right_angle(s1, s2, s3):
    ''' Use Pythagoras' Theorum to determine if right-angled'''

    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        raise ValueError('Sides must be postive. Was given s1: {} s2: {} s3: {}'.format(s1, s2, s3))

    sides = [s1, s2, s3]
    sides.sort()

    a, b, c = tuple(sides)

    if a**2 + b**2 == c**2:
        return True

    # Floating point math rounding, return True if the values are close
    return math.isclose(a**2 + b**2, c**2)