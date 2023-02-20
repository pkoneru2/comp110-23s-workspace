"""EX03 - Wordle"""

__author__ = "730570597"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def main() -> None: 
    turn = 1
    secret = "codes"
    while(turn <= 6): # while loop exits after 6 turns are complete
        print(f"=== Turn {turn}/6 ===")
        user_input = input_guess(len(secret))
        print(emojified (user_input, secret))
        if(user_input == secret):
            print(f"You won in {turn}/6 turns!")
            turn = 7
        turn = turn + 1
    if(turn > 6 and user_input != secret):
        print ("X/6 - Sorry, try again tomorrow")


def contains_char(word: str, letter: str) -> bool:
    """Searches string for character"""
    assert len(letter) == 1
    idx = 0
    while (idx < len(word)):
        if(letter != word[idx]):
            alt_idx = 0
            while(alt_idx < len(word)): # Checks if letter is in another index of word
                if(word[alt_idx] == letter):
                    return True
                else:
                    alt_idx = alt_idx + 1
        idx = idx + 1
    return False

def emojified(guess: str, secret: str) -> str:
    "Checks letters and returns appropriate colored box"
    assert len(guess) == len(secret)
    word_idx = 0
    emoji_guess = ""
    while (word_idx < len(secret)):
        if(guess[word_idx] == secret[word_idx]): #If letters match, concatenates green box"
            emoji_guess = emoji_guess + GREEN_BOX
        else:
            yellow = contains_char(secret, guess[word_idx]) #Uses contains_char function to check all indices for letter before concatenating yellow box
            if(yellow == True):
                emoji_guess = emoji_guess + YELLOW_BOX
            else:
                emoji_guess = emoji_guess + WHITE_BOX #Concatenates white box if letter is not in word
        word_idx = word_idx + 1
    return emoji_guess

def input_guess(length: int) -> str:
    """Takes user input and checks if input matches length of secret word"""
    user_guess: str = input(f"Enter a { length} character word: ")
    while (len(user_guess) != length):
        user_guess = input(f"That wasn't { length } chars! Try again: ")
    return user_guess

if __name__ == "__main__":
    main()