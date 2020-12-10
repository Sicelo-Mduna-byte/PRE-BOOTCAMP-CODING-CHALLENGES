def vowel_finder(string_entered_by_user):
    vowels = "AaEeIiOoUu"
    final_answer = [each for each in string_entered_by_user if each in vowels]
    return final_answer

print(vowel_finder("Hello Egg"))