def vowel_finder(string_entered_by_user):
    vowels = "AaEeIiOoUu"
    final_answer = [each for each in string_entered_by_user if each in vowels]
    return final_answer

string_entered_by_user = "Hello World"
print("The string:", string_entered_by_user)
print("Contains the following vowels:", vowel_finder(string_entered_by_user))