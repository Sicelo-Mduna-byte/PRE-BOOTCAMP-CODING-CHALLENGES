def vowel_finder(string_entered_by_user):
    string = []
    string.extend(string_entered_by_user)
    vowels = "aAeEiIoOuU"
    vowel_list = []
    for i in string:
            if(i in vowels):
                vowel_list.append(i)
    vowels = (", " .join(vowel_list))
    print("The following vowels are contained in the string: %s" % (vowels))

vowel_finder("Hello Egg")
