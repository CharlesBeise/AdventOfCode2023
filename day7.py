def part1():
    hands = []

    with open("day7_input.txt") as infile:
        for line in infile.readlines():
            hands.append(line.strip('\n').split(" "))

    hand_dict = {"five": [],
                 "four": [],
                 "full": [],
                 "three": [],
                 "two": [],
                 "one": [],
                 "high":[]}

    scores = {}
    for hand, score in hands:
        cards = {}
        scores[hand] = int(score)
        for card in hand:
            if card in cards.keys():
                cards[card] += 1
            else:
                cards[card] = 1
        nums = sorted(list(cards.values()), reverse=True)

        if nums[0] == 5:
            hand_dict["five"].append(hand)
        elif nums[0] == 4:
            hand_dict["four"].append(hand)
        elif nums[0] == 3:
            if nums[1] == 2:
                hand_dict["full"].append(hand)
            else:
                hand_dict["three"].append(hand)
        elif nums[0] == 2:
            if nums[1] == 2:
                hand_dict["two"].append(hand)
            else:
                hand_dict["one"].append(hand)
        else:
            hand_dict["high"].append(hand)

    alphabet = 'AKQJT98765432'

    allHands = []
    for rank in hand_dict.items():
        cur = rank[1]
        temp = sorted(cur, key=lambda word: [alphabet.index(c) for c in word])
        allHands += temp

    total = 0
    counter = len(allHands)
    for i in range(len(allHands)):
        temp = (scores[allHands[i]] * counter)
        total += temp
        counter -= 1
    print("Total:", total)


def part2():

    hands = []

    with open("day7_input.txt") as infile:
        for line in infile.readlines():
            hands.append(line.strip('\n').split(" "))

    hand_dict = {"five": [],
                 "four": [],
                 "full": [],
                 "three": [],
                 "two": [],
                 "one": [],
                 "high":[]}

    scores = {}
    for hand, score in hands:
        cards = {}
        scores[hand] = int(score)
        jokers = 0
        for card in hand:
            if card == 'J':
                jokers += 1
            elif card in cards.keys():
                cards[card] += 1
            else:
                cards[card] = 1
        nums = sorted(list(cards.values()), reverse=True)
        if len(nums) == 0:
            nums.append(5)
        else:
            nums[0] += jokers

        if nums[0] == 5:
            hand_dict["five"].append(hand)
        elif nums[0] == 4:
            hand_dict["four"].append(hand)
        elif nums[0] == 3:
            if nums[1] == 2:
                hand_dict["full"].append(hand)
            else:
                hand_dict["three"].append(hand)
        elif nums[0] == 2:
            if nums[1] == 2:
                hand_dict["two"].append(hand)
            else:
                hand_dict["one"].append(hand)
        else:
            hand_dict["high"].append(hand)

    alphabet = 'AKQT98765432J'

    allHands = []
    for rank in hand_dict.items():
        cur = rank[1]
        temp = sorted(cur, key=lambda word: [alphabet.index(c) for c in word])
        allHands += temp

    total = 0
    counter = len(allHands)
    for i in range(len(allHands)):
        temp = (scores[allHands[i]] * counter)
        total += temp
        counter -= 1
    print("Total:", total)


if __name__ == '__main__':
    part2()
