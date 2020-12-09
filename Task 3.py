def sum_of_arguments_is_65_decider(first_number,second_number):

    if((first_number == 65 or second_number == 65) or ((first_number + second_number) == 65)):

        return True
    
    else:
        return False

print(sum_of_arguments_is_65_decider(55,10))