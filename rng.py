import random
import math

def game():
    maximum = int(input("How big of a range do you want? (ex: 100) "))
    target = random.randint(1, maximum)

    guess_limit = math.ceil(10 + math.log2(maximum / 100)) # 10 guesses for 100, extra guess for 200 to cut in half, 1 less for 50, etc
    print("You have", guess_limit, "guesses.")
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

def main():
    again = 'y'
    while again == 'y':
        game()
        again = input("Would you like to play again? (y/n) ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()