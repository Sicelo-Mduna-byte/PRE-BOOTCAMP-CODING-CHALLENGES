def convert_celsius_to_faranheit(temperature_in_celcius):
    Temperature_in_faranheit = (((9 / 5) * temperature_in_celcius) + 32)
    return (Temperature_in_faranheit)

def convert_faranheit_to_celsius(temperature_in_faranheit):
    temperature_in_celcius = ((temperature_in_faranheit - 32) * (5 / 9))
    return (temperature_in_celcius)



the_entered_temperature = []  

user_answer_for_celcius_to_faranheit_conversion  = input("Do you wish to convert Celsius to Faranheit(y/n) ?: ")
if((user_answer_for_celcius_to_faranheit_conversion == 'y') or (user_answer_for_celcius_to_faranheit_conversion == 'Y')):
    temperature_in_celcius = int(input("Enter the Temperature in Celsius : "))
    the_entered_temperature.append(temperature_in_celcius)
    print(temperature_in_celcius, "degrees Celsius converted to degrees Faranheit is:", convert_celsius_to_faranheit(temperature_in_celcius))

else:
    user_answer_for_faranheit_to_celcius_conversion = input("Do you wish to convert Faranheit to Celsius(y/n) ?: ")
    if((user_answer_for_faranheit_to_celcius_conversion == 'y') or (user_answer_for_faranheit_to_celcius_conversion == 'Y')):
        temperature_in_faranheit = int(input("Enter the Temperature in Faranheit : "))
        the_entered_temperature.append(temperature_in_faranheit)
        print(temperature_in_faranheit, "degrees Faranheit converted to degrees Celsius is: %.2f" % (convert_faranheit_to_celsius(temperature_in_faranheit)))
                                                                                                  