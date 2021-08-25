# Russian rules for 36 cards' deck
import random
from art import logo


def clear():
    """
    Supporting crunch to clear the terminal
    """
    print("\n"*30)


deck = ("6", "7", "8", "9", "10", "J", "Q", "K", "A")
from_deck = {"6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "Q": 3, "K": 4, "A": 11}


def draw_a_card(hand):
    """
    Append a card in a list
    :param hand:
    :return: hand
    """
    card = random.randint(0, len(from_deck))
    hand.append(from_deck.get(deck[card-1]))
    return hand


def deal_the_cards(hand):
    """
    Deal two cards for player or computer
    :param hand:
    :return: hand
    """
    for i in range(0, 2):
        draw_a_card(hand)
    return hand


def check_winner(p_hand, c_hand):
    print(f"Your final hand: {p_hand}, and your score is {sum(p_hand)}")
    print(f"Computer's final hand: {c_hand}, and it score is {sum(c_hand)}")
    if (sum(p_hand) > sum(c_hand)) and sum(p_hand) <= 21 or (sum(c_hand) > 21):
        print("You win!!")
    elif sum(p_hand) == sum(c_hand) == 21:
        print("Tied, Split the bank!")
    else:
        print("You lose")


def main():
    is_game = True
    players_hand, comp_hand = [], []
    players_hand = deal_the_cards(players_hand)
    comp_hand = deal_the_cards(comp_hand)

    while is_game:
        print(logo)
        print(f"Your cards: {players_hand}")
        print(f"Computer first card: {comp_hand[0]}")
        if input("Type 'y' to get another card or 'n' to continue: ").lower() == 'y':
            draw_a_card(players_hand)
            print(f"You get {players_hand[2]}")

        check_winner(players_hand, comp_hand)
        if input("do you want to play again?: ").lower() == "y":
            players_hand, comp_hand = [], []
            players_hand = deal_the_cards(players_hand)
            comp_hand = deal_the_cards(comp_hand)
            clear()
        else:
            is_game = False


if __name__ == '__main__':
    main()
