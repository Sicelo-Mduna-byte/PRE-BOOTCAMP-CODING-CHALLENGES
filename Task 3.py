def my_function(x,y):
    """
        function that takes 2 numbers as input. If either of the numbers is 65, OR if the sum of the numbers is
        65 then return true. Otherwise return false.

    """
    
    if((x == 65 or y == 65) or ((x + y) == 65)):

        return True
    
    else:
        return False

print(my_function(55,10))