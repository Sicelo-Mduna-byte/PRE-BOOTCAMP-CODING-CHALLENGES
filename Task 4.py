
def my_function(x,y):

    sum = str(x+y)
    """
    Function that takes 2 numbers as input, if either of the numbers is 3 AND the sum of the numbers 
    contains a 3 then return true. Otherwise return False

    """
    
    if((x or y == 3) and ("3" in (sum))):

        return True
    
    else:
        return False

print(my_function(3,15))