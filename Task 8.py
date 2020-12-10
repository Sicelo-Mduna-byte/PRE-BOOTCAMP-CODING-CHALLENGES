def converter(number_that_has_to_be_converted):
     hour = int(number_that_has_to_be_converted / 60) 
     minute = int(number_that_has_to_be_converted % 60)           
     if(hour <= 1 and minute <= 1):
         return (" %d hour %d minute" % (hour, minute))
     if(hour <= 1 and minute > 1):
         return (" %d hour %d minutes" % (hour, minute))
     if(hour > 1 and minute <= 1):
         return (" %d hours %d minute" % (hour, minute))
     if(hour > 1 and minute > 1):
         return (" %d hours %d minutes" % (hour, minute))
     return()

print(converter(133))