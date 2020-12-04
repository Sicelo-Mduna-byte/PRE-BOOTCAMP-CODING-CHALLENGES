def comparison(String1, String2):
    '''
    I create a nested for loop, the inside loop runs to completion before the outer loop has a single iteration
    hence im always comparing my inner loop(j) to my outer loop(i) hence i append my list with the outer loop(j)
    '''
    List1 = []
    List1.extend(String1)
    List2 = []
    List2.extend(String2)
    List3 = []
    for i in List1:
        for j in List2:
            if((i == j) and (i != List3)):
                List3.append(j)
    
    
    return(List3)

String1 = "Sicelo"
String2 = "Siaeno"
print("The 2 Strings %s and %s, Have the following common characters " %(String1, String2), comparison(String1, String2))