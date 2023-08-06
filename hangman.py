import random

HANGMAN_ASCII = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""",
]

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'pineapple', 'watermelon', 'mango', 'kiwi', 'papaya']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def is_game_over(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord: " + display_word(word_to_guess, guessed_letters))
        print(HANGMAN_ASCII[6 - attempts])
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            if is_game_over(word_to_guess, guessed_letters):
                print("Congratulations! You guessed the word:", word_to_guess)
                break
        else:
            attempts -= 1
            print(f"Wrong letter! You have {attempts} attempts remaining.")

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
