import random
facts = ['For a right-sided triangle, the square of the longest side is equal',
         'Scalene, isosceles, equilateral, and right-angle are types',
         'Google Play, Delta Airlines, and CAT all have triangles',
         'The sierpinkski Triangle is a fractal form']

def random_fact(facts):

    fact = random.choice(facts)

    if fact == '':
        raise ValueError('Error, Empty String')

    return facts

