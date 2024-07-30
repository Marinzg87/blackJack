from art import logo
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hand_sum(hand):
    on_hand = 0
    for card in hand:
        on_hand += card
    return on_hand


def first_two_cards(hand):
    for card in range(2):
        hand.append(random.choice(deck))
    return hand


user_hand = []
computer_hand = []

first_two_cards(user_hand)
first_two_cards(computer_hand)

print(f"User hand: {user_hand}, Computer hand: {computer_hand}")

user_sum = hand_sum(user_hand)
computer_sum = hand_sum(computer_hand)
print(f"User score: {user_sum}, Computer score: {computer_sum}")