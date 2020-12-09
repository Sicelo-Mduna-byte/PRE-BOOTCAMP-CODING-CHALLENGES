def find_characters_common_in_2_strings(string1, string2):
    list_that_contains_string1_in_lowercase = []
    list_that_contains_string1_in_lowercase.extend(string1.lower())
    list_that_contains_string2_in_lowercase = []
    list_that_contains_string2_in_lowercase.extend(string2.lower())
    list_that_contains_the_similar_characters = []
    for i in list_that_contains_string1_in_lowercase:
        for j in list_that_contains_string2_in_lowercase:
            if((i == j) and (i != list_that_contains_the_similar_characters)):
                list_that_contains_the_similar_characters.append(j)
    
    
    return(list_that_contains_the_similar_characters)

string1 = "Sicelo"
string2 = "Siaeno"
print("The 2 Strings %s and %s, Have the following common characters " %(string1, string2), (find_characters_common_in_2_strings(string1, string2)))