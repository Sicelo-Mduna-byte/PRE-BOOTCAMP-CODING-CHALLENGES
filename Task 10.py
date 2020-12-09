def vowel_finder(string_entered_by_user):

    list_containing_entire_string = []
    list_containing_vowels_found_in_users_string = []
    list_containing_entire_string.extend(string_entered_by_user)
    for i in list_containing_entire_string:
        if (("a" == i) or ("a" == i) or ("e" == i) or ("i" == i) or ("o" == i) or ("u" == i)):
            list_containing_vowels_found_in_users_string.append(i)
    return list_containing_vowels_found_in_users_string

string_entered_by_user = "Hello World"
print("The string:", string_entered_by_user)
print("Contains the following vowels:", vowel_finder(string_entered_by_user))