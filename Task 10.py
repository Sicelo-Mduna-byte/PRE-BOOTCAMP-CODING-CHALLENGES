def vowel_finder(string_entered_by_user):
    string_in_lowercase = []
    string_in_lowercase.extend(string_entered_by_user.lower())
    vowels = "aeiou"
    similar_vowel_list = []
    for i in string_in_lowercase:
            if((i in vowels) and (i not in similar_vowel_list)):
                    similar_vowel_list.append(i)
    vowels = (", " .join(similar_vowel_list))
    print("The following vowels are contained in the string: %s" % (vowels))

vowel_finder("Hello Egg")
