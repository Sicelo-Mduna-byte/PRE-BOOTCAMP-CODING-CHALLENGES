NumList = []

def maximum(NumList):
    """
    This function will find the Maximum/Largest value in an array and display it

    """

    temp = NumList[0]
    for i in range(n):
        if(NumList[i] > temp):
            temp = NumList[i]
    return (temp)



n = int(input("How many numbers will you enter? : "))
print("Please Enter %d Numbers: " % (n))
for i in range(n):
    numbers = int(input("Enter number %d: " % (i+1)))
    NumList.append(numbers)

print("The following numbers were entered: ", NumList)

print(maximum(NumList))