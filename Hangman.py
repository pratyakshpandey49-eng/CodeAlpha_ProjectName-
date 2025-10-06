import random

# List of predefined words
words = ["python", "computer", "program", "science", "hangman"]

# Randomly choose a word
word = random.choice(words)

# Initialize variables
guessed_letters = []
attempts = 6

# Create a string with underscores for unguessed letters
display_word = ["_"] * len(word)

print("🎯 Welcome to the Hangman Game!")
print("Guess the word, one letter at a time.")
print("You have", attempts, "incorrect guesses allowed.\n")

# Game loop
while attempts > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try another.\n")
        continue

    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print("✅ Good guess!\n")
        # Reveal the letter in the display_word
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts, "\n")

# Game result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game over! The word was:", word)
