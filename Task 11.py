def find_characters_common_in_2_strings(string1, string2):
    string1_in_lowercase = []
    string1_in_lowercase.extend(string1.lower())
    string_2_in_lowercase = []
    string_2_in_lowercase.extend(string2.lower())
    similar_char_list = []
    for i in string1_in_lowercase:
        for j in string_2_in_lowercase:
            if((i == j) and (i != similar_char_list)):
                similar_char_list.append(j)
    return(similar_char_list)

string1 = "Sicelo"
string2 = "Siaeno"
print("The 2 Strings %s and %s, Have the following common characters " %(string1, string2), (find_characters_common_in_2_strings(string1, string2)))