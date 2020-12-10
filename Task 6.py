
def maximum_value_finder(number_1, number_2, number_3):
    current_maximum_value = number_1 
    if(number_2 > number_1):
        current_maximum_value = number_2
    if(number_3 > number_2):
        current_maximum_value = number_3
    return current_maximum_value                     

print("The maximum number entered is:", maximum_value_finder(20, 30, 20))