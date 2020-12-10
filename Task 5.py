def area_of_triangle(side1,side2,side3):                                    
    semiperimeter = (side1 + side2 + side3) / 2
    area = (((semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)) * semiperimeter)
    final_answer = area ** 0.5
    return (final_answer)

print(area_of_triangle(3,4,5))