def converter(number_that_has_to_be_converted):
     hour = int(number_that_has_to_be_converted / 60)                          # converts the entered number into hours
     
     minute = int(number_that_has_to_be_converted % 60)                        # converts the entered number into minutes
     
     if(hour <= 1):
         current_hour =  (str(hour) + " hour")
    
     elif(hour > 1):
         current_hour =  (str(hour) + " hours")
        
     if(minute <= 1):
         current_minute =  (str(minute) + " minute")
         return current_hour, current_minute
     elif(minute > 1):
         current_minute = (str(minute) + " minutes")
         return current_hour, current_minute


        
print(converter(125))