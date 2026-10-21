import random

secret_nunber = random.randint(1, 100)

max_attempts = 7
attempts = 0


while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1 
      
    if guess <  secret_nunber:
        print("Too low try higher")
    elif guess > secret_nunber:
        print("Too high try lower")
    else:
        print("congratulations! you guessed the correct number!")
        break
if attempts == max_attempts and guess != secret_nunber:
    print("Game over! You have used all your attempts.")
    print("The secret number was:", secret_nunber)
