from art import logo
import random


def deal_card():
    """Function will deal card from the deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


def calculate_score(cards):
    """"Function will sum the values of the cards"""
    return sum(cards)


def compare(score_1, score_2):
    """Function will check the scores and return the result"""
    if score_1 > 21 and score_2 > 21:
        print("You went over. You lose 😤")

    if score_1 == score_2:
        return "Draw 🙃"
    elif score_2 == 0:
        return "Lose, opponent has Blackjack 😱"
    elif score_1 == 0:
        return "Win with a Blackjack 😎"
    elif score_1 > 21:
        return "You went over. You lose 😭"
    elif score_2 > 21:
        return "Opponent went over. You win 😁"
    elif score_1 > score_2:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal the cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer final's hand: {computer_cards}, "
          f"final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? "
            "Type 'y' or 'n': ") == "y":
    play_game()
