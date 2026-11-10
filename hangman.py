import random

words = ["Apple", "Mango", "Python", "Orange"]
secret_word = random.choice(words).upper()

hidden_word = ["_"] * len(secret_word)
print("Word:", "".join(hidden_word))

Incorrect_guesses = 0
max_attempts = 6
guessed_letters = []

while Incorrect_guesses < max_attempts:

    Guess = input("Enter a letter: ").upper()

    if len(Guess) != 1 or not Guess.isalpha():
        print("Please enter one letter!")
        continue

    if Guess in guessed_letters:
        print("You have already guessed that letter!")
        continue

    guessed_letters.append(Guess)

    if Guess in secret_word:
        print("Correct guess! ✅")

        for index, letter in enumerate(secret_word):
            if letter == Guess:
                hidden_word[index] = letter

    else:
        print("Incorrect guess! ❌")
        Incorrect_guesses += 1

    print("Word:", "".join(hidden_word))
    print("Incorrect guesses:", Incorrect_guesses)

    if "".join(hidden_word) == secret_word:
        print("Congratulations! You won! 🎉")
        break

if Incorrect_guesses == max_attempts:
    print("Game Over! You lost.")
    print("The word was:", secret_word)
    