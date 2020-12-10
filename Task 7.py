def convert_celsius_to_faranheit(temperature_in_celcius):
    temperature_in_faranheit = (((9 / 5) * temperature_in_celcius) + 32)
    return (temperature_in_faranheit)

def convert_faranheit_to_celsius(temperature_in_faranheit):
    temperature_in_celcius = ((temperature_in_faranheit - 32) * (5 / 9))
    return (temperature_in_celcius)

