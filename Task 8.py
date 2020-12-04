def converter(number):
    '''
    The modulus operand will return the remainder after division which in this case is the minutes
    The Division sign will return the hours as it will be rounded off to a whole number using the %d operand
    '''
    hour = int(number / 60) 

    minute = int(number % 60)

    if(hour <= 1):
        return (str(hour) + "hour", str(minute) + "minutes")
    else:
        return (str(hour) + "hours", str(minute) + "minutes")

        
print(converter(133))