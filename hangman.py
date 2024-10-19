# print("Hello World") --> First line of python
import requests

def getWord(length):
    url_length = str(length)
    url = f"https://random-word-api.herokuapp.com/word?length={url_length}"
    response = requests.get(url)

    return response.json()

def game(word):
    incorrect_guesses = 0

    game_word = list(word[0])  # Use the whole word
    game_word_length = len(game_word)

    # Initialize word_blank to show the current status of the guessed letters
    word_blank = list("_" * game_word_length)
    print(f"Your word is {game_word_length} letters long")

    while incorrect_guesses < 8:
        print("Current word status: " + " ".join(word_blank))
        print(f"You have {7 - incorrect_guesses} guesses left")
        guessedLetter = input("Make your guess of the letter: ")
        if guessedLetter in game_word:
            # Find all indices of the guessed letter
            indices = [index for index, letter in enumerate(game_word) if letter == guessedLetter]
            print(f"You got the letter right. It is at positions {indices}.")
            print("\n\n")
            # Update word_blank to reveal the letters
            for index in indices:
                word_blank[index] = guessedLetter
            
        else:
            print("\033[1mYou Got It Wrong!\033[0m")
            print("\n\n\n\n")
            incorrect_guesses += 1

        # Check if the player has guessed the whole word
        if "_" not in word_blank:
            print("\033[1mCongratulations! You've guessed the word:\033[0m", "".join(word_blank))
            break
    else:
        print("Game over! The correct word was:", "".join(game_word))

print("Welcome to \033[1mH A N G M A N\033[0m")



word_length_limit = 1
while int(word_length_limit)<5 or int(word_length_limit)>15:
    word_length_limit = input("Enter the maximum character count 5-15: ")



fetched_word = getWord(word_length_limit)
game(fetched_word)
