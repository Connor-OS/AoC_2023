TEST = False
in_file = "./resources/day_7_test.txt" if TEST else "./resources/day_7_input.txt"

face_cards = {"A": "14", "K": "13", "Q": "12", "J": "11", "T": "10"}
face_cards_joker = {"A": "14", "K": "13", "Q": "12", "J": "1", "T": "10"}

BEST_HAND = 6
HAND_CONST = 1000000000

from itertools import groupby

def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split()
            yield line


def question(hand_power):
    """Answer to the first question of the day"""
    answer = 0
    hands = [(hand, int(bid)) for hand, bid in file_lines()]

    hands = sorted(hands, key=lambda x: hand_power(x[0]))

    for i, hand in enumerate(hands):
        # print(hand[0], i+1)
        answer += hand[1] * (i+1)

    return answer


def calc_hand_power(hand):
    power = 0
    # convert  face cards to numerical
    hand = list(hand)

    for f in face_cards:
        hand = [card.replace(f, face_cards[f]) for card in hand]
    # check type
    sorted_hand = sorted(hand)
    groups = []
    for k, g in groupby(sorted_hand):
        groups.append(list(g))

    for group in groups:
        if len(group) == 5:
            # 5 of a kind
            power += HAND_CONST * BEST_HAND
        if len(group) == 4:
            # 4 of a kind
            power += HAND_CONST * (BEST_HAND - 1)
        if len(group) == 3:
            # 3 of a kind
            power += HAND_CONST * (BEST_HAND - 3)
        if len(group) == 2:
            # pair
            power += HAND_CONST * (BEST_HAND - 5)

    # add individual power
    for i, card in enumerate(hand):
        power += (14**(6-i)) * int(card)

    return power


def calc_hand_power_jokers(hand):
    power = 0
    # convert  face cards to numerical
    hand = list(hand)

    for f in face_cards:
        hand = [card.replace(f, face_cards_joker[f]) for card in hand]
    # check type
    sorted_hand = sorted(hand)
    groups = []
    for k, g in groupby(sorted_hand):
        g = list(g)
        # remove joker group
        if "1" in g:
            continue
        groups.append(g)
    groups.append([])

    #add jokers to the biggest other group
    for card in hand:
        if card == "1":
            groups = sorted(groups, key=lambda x: 5-len(x))
            groups[0].append("J")

    for group in groups:
        if len(group) == 5:
            # 5 of a kind
            power += HAND_CONST * BEST_HAND
        if len(group) == 4:
            # 4 of a kind
            power += HAND_CONST * (BEST_HAND - 1)
        if len(group) == 3:
            # 3 of a kind
            power += HAND_CONST * (BEST_HAND - 3)
        if len(group) == 2:
            # pair
            power += HAND_CONST * (BEST_HAND - 5)

    # add individual power
    for i, card in enumerate(hand):
        power += (14**(6-i)) * int(card)


    return power


if __name__ == '__main__':
    answer_1 = question(calc_hand_power)
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question(calc_hand_power_jokers)
    print(f"Question 2 answer is: {answer_2}")
