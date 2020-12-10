def determine_the_status_of_the_input(first_number,second_number):               
    sum_of_the_two_numbers = str(first_number+second_number)
    if((first_number or second_number == 3) and ("3" in (sum_of_the_two_numbers))):
        return True
    else:
        return False

print(determine_the_status_of_the_input(3,15))