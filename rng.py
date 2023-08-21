import random
play = 'y'

while play == 'y':
    maximum = int(input("How big of a range do you want? (ex: 100) "))
    target = random.randint(1, maximum)
    
    guess_limit = 10
    guess = int(input("Guess a number between 1 and " + str(maximum) + ": "))
    guess_limit -= 1

    while guess != target and guess_limit > 0:
        if guess > target:
            print("Lower")
        else:
            print("Higher")
        if 1 < guess_limit < 4:
            print(guess_limit, "guesses left!")
        elif guess_limit == 1:
            print("Last guess!")
        guess = int(input("Guess a number: "))
        guess_limit -= 1

    if guess == target:
        print("Correct!")
    else:
        print("You ran out of guesses. Better luck next time!")
        print("The correct number was", target)

    play = input("Would you like to play again? (y/n) ")

print("Thanks for playing!")