# Russian rules for 36 cards' deck
import random
from art import logo


def clear():
    print("\n"*20)


def deal_the_cards(hand):
    card = random.randint(0, len(from_deck))
    # print(card)
    hand.append(from_deck.get(deck[card]))
    return hand


def shuffle(hand):
    for i in range(0, 2):
        deal_the_cards(hand)
    return hand


deck = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
from_deck = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "Q": 3, "K": 4, "A": 11}
is_game = True
result = ""
players_hand, comp_hand = [], []
players_hand = shuffle(players_hand)
comp_hand = shuffle(comp_hand)

while is_game:
    print(logo)
    print(f"Your cards: {players_hand}")
    print(f"Computer first card: {comp_hand[0]}")
    if input("do you want to play again?: ").lower() == "y":
        players_hand, comp_hand = [], []
        print("cont")
    else:
        is_game = False

print(f"Your final hand: {players_hand}")
print(f"Computer's final hand: {comp_hand}")
print(f"{result}")
