"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730570597"

user_word: str = input("Enter a 5-character word: ")
if (len(user_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
else:
    user_character: str = input("Enter a single character: ")
    if (len(user_character) != 1):
        print("Error: Character must be a single character.")
        exit()
    else:
        matching_characters: int = 0    
        print("Searching for " + user_character + " in " + user_word)
        if (user_word[0] == user_character):
            print(user_character + " found at index 0")
            matching_characters = matching_characters + 1
        if (user_word[1] == user_character):
            print(user_character + " found at index 1")
            matching_characters = matching_characters + 1
        if (user_word[2] == user_character):
            print(user_character + " found at index 2")
            matching_characters = matching_characters + 1
        if (user_word[3] == user_character):
            print(user_character + " found at index 3")
            matching_characters = matching_characters + 1
        if (user_word[4] == user_character):
            print(user_character + " found at index 4")
            matching_characters = matching_characters + 1
        if (matching_characters == 1):
            print(str(matching_characters) + " instance of " + user_character + " found in " + user_word)
        if (matching_characters > 1):
            print(str(matching_characters) + " instances of " + user_character + " found in " + user_word)
        if (matching_characters == 0):
            print("No instances of " + user_character + " found in " + user_word)
