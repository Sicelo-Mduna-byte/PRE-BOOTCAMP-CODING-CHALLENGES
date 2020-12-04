NumList = []

def Celsius_to_faranheit(C):
    '''
    This function converts Celsius into Faranheit abd appends my list with the new value
    '''
    F = (((9 / 5) * C) + 32)
    return (F)

def Faranheit_to_celsius(F):
    '''
    This function converts Faranheit into Celsius and appends my listw with the new value
    '''
    C = ((F - 32) * (5 / 9))
    return (C)

user_answer_1 = input("Do you wish to convert Celsius to Faranheit(y/n) ?: ")
if((user_answer_1 == 'y') or (user_answer_1 == 'Y')):
    C = int(input("Enter the Temperature in Celsius : "))
    NumList.append(C)
    print(Celsius_to_faranheit(C))

else:
    user_answer_2 = input("Do you wish to convert Faranheit to Celsius(y/n) ?: ")
    if((user_answer_2 == 'y') or (user_answer_2 == 'Y')):
        F = int(input("Enter the Temperature in Faranheit : "))
        NumList.append(F)
        print(Faranheit_to_celsius(F))