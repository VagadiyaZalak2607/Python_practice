import random

# Step 1: Predefined word list
words = ["apple", "banana", "grapes", "orange", "mango"]

# Step 2: Choose a random word
word = random.choice(words)

# Step 3: Game variables
guessed_letters = []
attempts = 5

print("Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")

# Step 4: Game loop
while attempts > 0:
    display_word = ""

    # Show guessed letters or underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())

    # Check if player won
    if "_" not in display_word:
        print(" Congratulations! You guessed the word correctly.")
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess not in word:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}\n")
    else:
        print("Good guess!\n")

# Step 5: Game over
if attempts == 0:
    print(" ame Over! The word was:", word)
