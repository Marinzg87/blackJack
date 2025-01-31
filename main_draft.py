from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(hand, number):
    for card in range(number):
        hand.append(random.choice(deck))
    return hand


def calculate_score(hand):
    on_hand = 0
    for card in hand:
        on_hand += card
    if len(hand) == 2:
        if on_hand == 21:
            return 0
        else:
            return on_hand
    else:
        return on_hand


def compare(user_score, computer_score):
    if user_score == computer_score:
        result = "Draw"
    elif computer_score == 21:
        result = "Computer win!"
    elif user_score == 21:
        result = "User win!"
    elif user_score > computer_score:
        result = "User win!"
    else:
        result = "Computer win!"
    return result


# BlackJack
should_play = True
while should_play:
    # Empty lists of cards for user and computer
    user_hand = []
    computer_hand = []

    # First two cards for each player
    deal_card(user_hand, 2)
    deal_card(computer_hand, 2)

    # Cover second card from computer deck, show logo and decks
    computer_hand_view = [computer_hand[0], "_"]
    print(logo)
    print(f"Computer hand: {computer_hand_view}\nUser hand: {user_hand}")

    # Sum the deck values
    user_sum = calculate_score(user_hand)
    computer_sum = calculate_score(computer_hand)

    if user_sum == 0:
        print("User win!")
        print(f"User score: {user_sum}, Computer score: 21")
    elif user_sum > 21:
        print("Computer win!")
        print(f"User score: {user_sum}, Computer score: {computer_sum}")
    elif computer_sum == 0:
        print("Computer win!")
        print(f"User score: {user_sum}, Computer score: 21")
    else:
        game_on = True
        while game_on:
            if input("Draw card? 'y'\n") == "y":
                deal_card(user_hand, 1)
                user_sum = calculate_score(user_hand)
                if user_sum > 21:
                    print("Computer win!")
                    print(f"User score: {user_sum}, Computer score: {computer_sum}")
                    game_on = False
                    break
            if computer_sum < 17:
                while computer_sum < 17:
                    deal_card(computer_hand, 1)
                    computer_sum = calculate_score(computer_hand)
                if computer_sum > 21:
                    print("User win!")
                    print(f"User score: {user_sum}, Computer score: {computer_sum}")
                    game_on = False
                    break
            print(compare(user_sum, computer_sum))
            print(f"User score: {user_sum}, Computer score: {computer_sum}")
            game_on = False
        play_again = input("Another game? 'yes'\n")
        if play_again != "yes":
            should_play = False