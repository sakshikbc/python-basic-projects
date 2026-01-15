import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 to 100"))
        if guess == number_to_guess:
            print("Yay You got it")
            break
        elif guess < number_to_guess:
            print("Try a Bigger number")

        elif guess > number_to_guess:
            print("Try a lower Number")

        else:
            print("Invalid Number")

    except ValueError:
        print("PLease Enter a valid number")
    