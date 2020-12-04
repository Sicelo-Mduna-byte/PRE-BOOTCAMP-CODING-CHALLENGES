NumList = []

def Celsius_to_faranheit(Temperature_in_celcius):
    '''
    This function converts Celsius into Faranheit abd appends my list with the new value
    '''
    Temperature_in_faranheit = (((9 / 5) * Temperature_in_celcius) + 32)
    return (Temperature_in_faranheit)

def Faranheit_to_celsius(Temperature_in_faranheit):
    '''
    This function converts Faranheit into Celsius and appends my listw with the new value
    '''
    Temperature_in_celcius = ((Temperature_in_faranheit - 32) * (5 / 9))
    return (Temperature_in_celcius)

user_answer_1 = input("Do you wish to convert Celsius to Faranheit(y/n) ?: ")
if((user_answer_1 == 'y') or (user_answer_1 == 'Y')):
    Temperature_in_celcius = int(input("Enter the Temperature in Celsius : "))
    NumList.append(Temperature_in_celcius)
    print(Celsius_to_faranheit(Temperature_in_celcius))

else:
    user_answer_2 = input("Do you wish to convert Faranheit to Celsius(y/n) ?: ")
    if((user_answer_2 == 'y') or (user_answer_2 == 'Y')):
        Temperature_in_faranheit = int(input("Enter the Temperature in Faranheit : "))
        NumList.append(Temperature_in_faranheit)
        print(Faranheit_to_celsius(Temperature_in_faranheit))