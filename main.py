from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_cards(hand, number):
    for card in range(number):
        hand.append(random.choice(deck))
    return hand


def hand_sum(hand):
    on_hand = 0
    for card in hand:
        on_hand += card
    return on_hand


# Empty lists of cards for user and computer
user_hand = []
computer_hand = []

# First two cards for each player
get_cards(user_hand, 2)
get_cards(computer_hand, 2)

computer_hand_view = []
computer_hand_view.append(computer_hand[0])
computer_hand_view.append("_")
print(f"User hand: {user_hand}\nComputer hand: {computer_hand_view}")

# Sum the deck values
user_sum = hand_sum(user_hand)
computer_sum = hand_sum(computer_hand)

# BlackJack game
is_blackjack = False
while not is_blackjack:
    if user_sum == 21:
        print("User win!")
        print(f"User score: {user_sum}, Computer score: {computer_sum}")
        is_blackjack = True
        break
    elif computer_sum == 21:
        print("Computer win!")
        print (f"User score: {user_sum}, Computer score: {computer_sum}")
        is_blackjack = True
        break
    elif user_sum > 21:
        if user_hand.count(11) == 1:
            user_sum -= 10
            if user_sum > 21:
                print("Computer win!")
                print(f"User score: {user_sum}, Computer score: {computer_sum}")
                is_blackjack = True
                break
            else:
                if input("Would you like another card? 'y' or 'n'\n") == "y":
                    get_cards(user_hand, 1)
                    user_sum = hand_sum(user_hand)
                    if user_sum > 21:
                        print("Computer win!")
                        print(f"User score: {user_sum}, Computer score: {
                        computer_sum}")
                        is_blackjack = True
                        break
    else:
        if input("Would you like another card? 'y' or 'n'\n") == "y":
            get_cards(user_hand, 1)
            user_sum = hand_sum(user_hand)
            if user_sum > 21:
                print("Computer win!")
                print(f"User score: {user_sum}, Computer score: {computer_sum}")
                is_blackjack = True
                break
    while computer_sum < 17:
        get_cards(computer_hand, 1)
        computer_sum = hand_sum(computer_hand)
        if computer_sum > 21:
            print("User win!")
            print(f"User score: {user_sum}, Computer score: {computer_sum}")
            is_blackjack = True
            break
    if user_sum > computer_sum:
        print("User win!")
        print(f"User score: {user_sum}, Computer score: {computer_sum}")
        is_blackjack = True
        break
    elif computer_sum > user_sum:
        print("Computer win!")
        print(f"User score: {user_sum}, Computer score: {computer_sum}")
        is_blackjack = True
        break
    else:
        print("Draw")
        print(f"User score: {user_sum}, Computer score: {computer_sum}")
        is_blackjack = True
