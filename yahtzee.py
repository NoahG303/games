import random

translations = {
    1: "ONES",
    2: "TWOS",
    3: "THREES",
    4: "FOURS",
    5: "FIVES",
    6: "SIXES",
    7: "THREE_OF_A_KIND",
    8: "FOUR_OF_A_KIND",
    9: "FULL_HOUSE",
    10: "SMALL_STRAIGHT",
    11: "LARGE_STRAIGHT",
    12: "YAHTZEE",
    13: "CHANCE",
    "ONES": 1,
    "TWOS": 2,
    "THREES": 3,
    "FOURS": 4,
    "FIVES": 5,
    "SIXES": 6,
    "THREE_OF_A_KIND": 7,
    "FOUR_OF_A_KIND": 8,
    "FULL_HOUSE": 9,
    "SMALL_STRAIGHT": 10,
    "LARGE_STRAIGHT": 11,
    "YAHTZEE": 12,
    "CHANCE": 13
}

def roll_dice(keeps, dice):
    dice_vals = []
    for i in range(5):
        if i+1 not in keeps:
            dice_vals.append(random.randint(1,6))
        else:
            dice_vals.append(dice[i])
    return dice_vals

def roll_section():
    keeps = []
    dice = [-1] * 5
    for _ in range(2):
        dice = roll_dice(keeps, dice)
        print("Your values are: " + str(dice))
        keepers = input("Which dice do you want to keep (1 2 3 4 5): ")
        if keepers == "1 2 3 4 5":
            return dice
        elif keepers:
            keeps = [int(item) for item in keepers.split(" ")]
    dice = roll_dice(keeps, dice)
    print("Your values are: " + str(dice))
    return dice

def map_occurrences(dice):
    mapping = {}
    for die in dice:
        if die in mapping.keys():
            mapping[die] += 1
        else:
            mapping[die] = 1
    return mapping

def calculate_score(type, dice):
    dice_vals = map_occurrences(dice)
    occurrences = [val for val in dice_vals.values()]
    if 1 <= type <= 6:
        return dice.count(type)*type
    elif type == translations["THREE_OF_A_KIND"]:
        if 3 in occurrences or 4 in occurrences or 5 in occurrences:
            return sum(dice)
    elif type == translations["FOUR_OF_A_KIND"]:
        if 4 in occurrences or 5 in occurrences:
            return sum(dice)
    elif type == translations["FULL_HOUSE"]:
        if 3 in occurrences and 2 in occurrences:
            return 25
    elif type == translations["SMALL_STRAIGHT"]:
        if 3 in dice and 4 in dice and ((1 in dice and 2 in dice) or (2 in dice and 5 in dice) or (5 in dice and 6 in dice)):
            return 30
    elif type == translations["LARGE_STRAIGHT"]:
        if 2 in dice and 3 in dice and 4 in dice and 5 in dice and (1 in dice or 6 in dice):
            return 40
    elif type == translations["YAHTZEE"]:
        if dice[0] == dice[1] and dice[0] == dice[2] and dice[0] == dice[3] and dice[0] == dice[4]:
            return 50
    elif type == translations["CHANCE"]:
        return sum(dice)
    return 0

def play_turn(scores, dice):
    options = {}
    for index, score in enumerate(scores):
        if score == None:
            options[translations[index+1]] = calculate_score(index+1, dice)
    print("\nScoring options left: " + str(options) + "\n")
    selection = input("Select an option to score: ")
    scores[translations[selection]-1] = options[selection]

def display_scores(scores):
    used = {}
    unused = []
    for index, score in enumerate(scores):
        if score == None:
            unused.append(translations[index+1])
        else:
            used[translations[index+1]] = scores[index]
    if used:
        print("\nOptions used:", used)
    if unused:
        print("\nOptions remaining:", unused, "\n")

def game():
    scores = [None] * 13
    total_score = 0

    for _ in range(13):
        display_scores(scores)
        dice = roll_section()
        play_turn(scores, dice)

    print("\nFinal Scores: " + str(scores))

    if sum(scores[:6]) >= 63:
        total_score += 35
    total_score += sum(scores)
    print("Total score: " + str(total_score))

def main():
    again = 'y'
    while again == 'y':
        game()
        again = input("\nWould you like to play again? (y/n) ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()