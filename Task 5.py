from math import sqrt


def area_of_triangle(side1,side2,side3):
    '''
    Calculate the area of a triangle given only 3 sides, a,b,c
    '''
    Semiperimeter = (side1 + side2 + side3) / 2
    Area = (((Semiperimeter - side1) * (Semiperimeter - side2) * (Semiperimeter - side3)) * Semiperimeter)
    Final_answer = sqrt(Area)


    return (Final_answer)




print(area_of_triangle(3,4,5))