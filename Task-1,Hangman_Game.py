print("**********")
import random

# List of predefined words
words = ['apple', 'banana', 'cherry', 'mango', 'grapes']

# Randomly select a word from the list
secret_word = random.choice(words)

# Initialize variables
guessed_letters = []
attempts_left = 6
current_progress = ['_'] * len(secret_word)

print("Welcome to Hangman!")
print("Try to guess the word by entering one letter at a time.")
print("You have 6 chances to make incorrect guesses.")

while True:
    print("\nCurrent word:", ' '.join(current_progress))
    print("Remaining attempts:", attempts_left)
    
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You have already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")

        # Reveal all positions where the letter matches
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                current_progress[index] = guess
    else:
        print("Incorrect guess.")
        attempts_left -= 1

    # Check if the player has guessed the full word
    if '_' not in current_progress:
        print("\nCongratulations! You've guessed the word:", secret_word)
        break

    # Check if the player has run out of attempts
    if attempts_left == 0:
        print("\nGame Over. You've used all your attempts.")
        print("The word was:", secret_word)
        break
