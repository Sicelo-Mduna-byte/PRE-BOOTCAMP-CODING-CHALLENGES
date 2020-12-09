from math import sqrt

def area_of_triangle(side1,side2,side3):                                    # returns the area of a triangle with 3 sides
    semiperimeter = (side1 + side2 + side3) / 2
    area = (((semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)) * semiperimeter)
    final_answer = sqrt(area)


    return (final_answer)

print(area_of_triangle(3,4,5))