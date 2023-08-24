import random
import time

val_trans = {
    1: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

suit_trans = {
    1: "Hearts",
    2: "Diamonds",
    3: "Clubs",
    4: "Spades",
    "Hearts": 1,
    "Diamonds": 2,
    "Clubs": 3,
    "Spades": 4
}

def draw_card():
    return (random.randint(1,13),random.randint(1,4))

def display_player_cards(player_hand):
    print("Your cards: " + str([(val_trans[card[0]], suit_trans[card[1]]) for card in player_hand]))

def display_dealer_card(dealer_hand):
    print("Dealer's card: " + str([(val_trans[dealer_hand[0][0]], suit_trans[dealer_hand[0][1]])]))

def display_dealer_cards(dealer_hand):
    print("Dealer's cards: " + str([(val_trans[card[0]], suit_trans[card[1]]) for card in dealer_hand]))

def calc_score(cards):
    score = 0
    for card in cards:
        if card[0] == 1:
            score += 11
        elif card[0] >= 10:
            score += 10
        else:
            score += card[0]
    for card in cards:
        if score > 21 and card[0] == 1:
            score -= 10
    return score

def game():
    player_hand = [draw_card() for _ in range(2)]
    dealer_hand = [draw_card() for _ in range(2)]
    display_player_cards(player_hand)
    display_dealer_card(dealer_hand)
    player_score = calc_score(player_hand)
    dealer_score = calc_score(dealer_hand)
    print("Your score: " + str(player_score))
    if player_score == 21:
        print("Blackjack!")
        if dealer_score == 21:
            print("Dealer has blackjack too. Tie!")
        else:
            print("You win!")
        return
    next = input("Hit or Stay? (h/s): ")
    while next != 's':
        if next == 'h':
            player_hand.append(draw_card())
            display_player_cards(player_hand)
            player_score = calc_score(player_hand)
            print("Your score: " + str(player_score))
            if player_score > 21:
                break
        else:
            print("Invalid input!")
        next = input("Hit or Stay? (h/s): ")
    if player_score > 21:
        print("Bust!")
        print("You lose!")
        return
    print("Your final score: " + str(player_score))
    time.sleep(2)
    display_dealer_cards(dealer_hand)
    dealer_score = calc_score(dealer_hand)
    print("Dealer score: " + str(dealer_score))
    while dealer_score < 17:
        print("Dealer hits...")
        time.sleep(2)
        dealer_hand.append(draw_card())
        display_dealer_cards(dealer_hand)
        dealer_score = calc_score(dealer_hand)
        print("Dealer score: " + str(dealer_score))
        if dealer_score > 21:
            break
    if dealer_score > 21:
        print("Dealer bust!")
        print("You win!")
        return
    print("Dealer's final score: " + str(dealer_score))
    if player_score > dealer_score:
        print("You win!")
    elif dealer_score > player_score:
        print("You lose!")
    else:
        print("Tie!")

def main():
    again = 'y'
    while again == 'y':
        game()
        again = input("Would you like to play again? (y/n) ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()