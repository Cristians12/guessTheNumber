import random

top_of_range = input("Enter a number between 1 and 10: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Your number is too low.")
        quit()
else:
    print("Please type a number next time!")
    quit()

randomNum = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("You have to add an Integer, try again!")
        continue
    if user_guess == randomNum:
        print(f"You guessed it in {guesses} guesses!")
        break
    elif user_guess > randomNum:
        print("You were above the number!")
    else:
        print("You were below the number!")
