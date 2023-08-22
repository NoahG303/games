import random
import time

def roll_dice():
    return random.randint(1,6)

def play_turn():
    score = 0
    again = 'y'
    while again == 'y':
        roll = roll_dice()
        print("Roll:", roll)
        if roll == 1:
            print("Unlucky!")
            time.sleep(0.5)
            score = 0
            break
        score += roll
        print("Current score:", score)
        again = input("Roll again? (y/n) ")
    print("Round score:", score)
    return score

def game():
    scores = [0, 0]
    turn = 0
    while max(scores) < 100:
        print("\nPlayer " + str(turn+1) + "\'s turn")
        score = play_turn()
        scores[turn] += score
        print("Total score:", scores[turn])
        turn = not turn
        time.sleep(0.5)
    print("Congratulations Player " + str(scores.index(max(scores))+1))

def main():
    again = 'y'
    while again == 'y':
        game()
        again = input("Would you like to play again? (y/n) ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()