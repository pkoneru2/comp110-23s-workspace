"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730570597"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
word_length: int = len(secret_word)
word_idx: int = 0
emoji_guess: str = ""
user_guess: str = input(f"What is your { word_length}-letter guess? ")
while (len(user_guess) != word_length):
    user_guess = input(f"That was not { word_length } letters! Try again: ")
while (word_idx < word_length):
    if (user_guess[word_idx] == secret_word[word_idx]):
        emoji_guess = emoji_guess + GREEN_BOX
    if (user_guess[word_idx] != secret_word[word_idx]):
        yellow: bool = False
        alt_idx: int = 0
        while (yellow != True and alt_idx < word_length):
            if(secret_word[alt_idx] == user_guess[word_idx]):
                yellow = True
            else:
                alt_idx = alt_idx + 1
        if (yellow == True):
            emoji_guess = emoji_guess + YELLOW_BOX
        else:
            emoji_guess = emoji_guess + WHITE_BOX
    word_idx = word_idx+1
print(emoji_guess)
if (user_guess != secret_word):
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")

