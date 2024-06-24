from sys import argv
from math import floor


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        input = [
            line.replace(":", "|").split("|")[1:]
            for line in f.readlines()
        ]

    cards = [
        [ 
            [ int(y) for y in x.strip().split(" ") if y!="" ]
            for x in line
        ]
        for line in input
    ]
    num_cards = len(cards)
    card_dict = { i: 0 for i in range(1, num_cards+1) }

    num_wins = [
        sum([ 1 for x in card[1] if x in card[0] ])
        for card in cards
    ]

    for i, card in enumerate(num_wins, 1):
        card_dict[i] += 1
        for j in range(i+1, i+1+num_wins[i-1]):
            card_dict[j] += card_dict[i]

    print(card_dict)
    print(f"Total number of cards: {sum([val for val in card_dict.values()])}")
    print("-----------------------")
