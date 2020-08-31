import random

print("---------------------------")
print("\t\tGuess That Number")
print("---------------------------")
print()

the_number = random.randint(0, 100)

guess = "a"

while guess != the_number:

    guess_text = input('Guess a number between 0 and 100: ')

    guess = int(guess_text)
    if guess < the_number:
        print(f"Your {guess} is too low")
    elif guess > the_number:
        print(f"Your {guess} is too high")
    else:
        print("You win wtf")
