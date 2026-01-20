import random
numberToGuess = random.randint(1, 10)
while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < numberToGuess:
            print("Too Low!")
        elif guess > numberToGuess:
            print("Too High!")
        else:
            print("Congrats! You guessed right")
            break
    except ValueError:
        print("Oops! That's not a number!")
