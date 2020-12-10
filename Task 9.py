def sum_of_multiples_of_3_and_10_below_1000():
    list_contaning_multiples_of_three = []
    list_contaning_multiples_of_five = [] 
    for i in range(3, 1000, 3):                                                                                                   
        list_contaning_multiples_of_three.append(i)
    sum_of_multiples_of_list_contaning_multiples_of_three = (sum(list_contaning_multiples_of_three))
    
    for i in range(5, 1000, 5):                                                                                                    
       list_contaning_multiples_of_five.append(i)
    sum_of_multiples_of_list_contaning_multiples_of_five = (sum(list_contaning_multiples_of_five))
    



    sum_of_multiples_of_3_and_10_below_1000 = sum_of_multiples_of_list_contaning_multiples_of_three + sum_of_multiples_of_list_contaning_multiples_of_five
    return sum_of_multiples_of_3_and_10_below_1000

print("The sum of all the multiples of 3 and 5 below 1000 is: %d " % (sum_of_multiples_of_3_and_10_below_1000()))