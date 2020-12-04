from math import sqrt


def area_of_triangle(a,b,c):
    '''
    Calculate the area of a triangle given only 3 sides, a,b,c
    '''
    S = (a + b + c) / 2
    A = (((S - a) * (S - b) * (S - c)) * S)
    C = sqrt(A)


    return (C)




print(area_of_triangle(3,4,5))