

def vowel_finder(List):
    '''
    I create a for loop to iterate through my list, and check each elements of the list individually
    I use an if() conditional statemnt in the loop iteration to compare each element with the vowels(a,e,i,o,u)
    If theres a match i append my list with that vowel and print it
    '''
    List = []
    List2 = []
    List.extend(String)
    for i in List:
        if (("a" == i) or ("a" == i) or ("e" == i) or ("i" == i) or ("o" == i) or ("u" == i)):
            List2.append(i)
    return List2

String = "Hello World"
print(vowel_finder(String))