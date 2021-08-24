# Russian rules for 36 cards' deck
import random
from art import logo


def clear():
    print("\n"*20)


def deal_the_cards(side):
    card = random.randint(0, len(from_deck))
    print(card)
    side += from_deck.get(deck[card])
    return side


def shuffle(side):
    for i in range(0, 2):
        deal_the_cards(side)
    return side


deck = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
from_deck = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "Q": 3, "K": 4, "A": 11}
is_game = True
players_cards = []
comp_cards = []

while is_game:
    print(logo)
    players_cards = shuffle(players_cards)
    comp_cards = shuffle(comp_cards)
    print(f"Your cards: {players_cards}")
    print(f"Computer first card: {comp_cards[0]}")
    if input("do you want to play again?: ").lower() == "y":
        print("cont")
    else:
        is_game = False

print("final result")
