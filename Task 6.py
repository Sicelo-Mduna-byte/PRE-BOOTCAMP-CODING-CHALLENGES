
def maximum(list_of_all_the_numbers_entered):

    current_maximum_value = list_of_all_the_numbers_entered[0]                        # making the first element in my list the current maximum value
    for i in range(numbers_that_will_be_entered):                                     # using a for loop to iterate through my list, looking for a element thats greater than my current_maximum_value
        if(list_of_all_the_numbers_entered[i] > current_maximum_value):               # if i find an element thats greater than my current_maximum value, than assign that value to be my new current_maximum_value
            current_maximum_value = list_of_all_the_numbers_entered[i]
    return (current_maximum_value)


list_of_all_the_numbers_entered = []                                                  #list to store all the numbers the user will enter.
numbers_that_will_be_entered = int(input("How many numbers will you enter? : "))
print("Please Enter %d Numbers: " % (numbers_that_will_be_entered))
for i in range(numbers_that_will_be_entered):
    the_entered_number_from_the_user = int(input("Enter number %d: " % (i+1)))
    list_of_all_the_numbers_entered.append(the_entered_number_from_the_user)          #takes the entered value and adds it to the list, but adds it after the last current value

print("The following numbers were entered: ", list_of_all_the_numbers_entered)

print("The maximum number entered is:", maximum(list_of_all_the_numbers_entered))