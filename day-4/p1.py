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

    win_nums = [
        floor(2**(len([ num for num in card[1] if num in card[0] ])-1))
        for card in cards
    ]

    print("-----------------------")
    print(f"Total winning worth: {sum(win_nums)}")
