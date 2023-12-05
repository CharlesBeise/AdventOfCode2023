def part1():
    total = 0
    with open("day4_input.txt") as infile:
        for line in infile.readlines():
            left, right = line.strip('\n').split(":")[1].split("|")
            leftNums = left.split(" ")
            while "" in leftNums:
                leftNums.remove("")
            rightNums = right.split(" ")
            while "" in rightNums:
                rightNums.remove("")
            rightSet = set(rightNums)
            leftSet = set(leftNums)
            result = leftSet.intersection(rightSet)

            if len(result) > 0:
                total += (2**(len(result)-1))

    print(total)


def part2():
    # Bottom up approach
    cards = {}
    curCard = 1
    with open("day4_input.txt") as infile:
        for line in infile.readlines():
            left, right = line.strip('\n').split(":")[1].split("|")
            leftNums = left.split(" ")
            while "" in leftNums:
                leftNums.remove("")
            rightNums = right.split(" ")
            while "" in rightNums:
                rightNums.remove("")
            rightSet = set(rightNums)
            leftSet = set(leftNums)
            result = leftSet.intersection(rightSet)

            cards[curCard] = len(result)
            curCard += 1

    curCard -= 1
    print(cards)
    maxCards = curCard

    while curCard > 0:
        for i in range(1, cards[curCard]+1):
            if curCard + i <= maxCards:
                cards[curCard] += cards[curCard+i]
        curCard -= 1

    total = maxCards

    for i in range(1, maxCards-1):
        total += cards[i]

    print(total)


if __name__ == '__main__':
    part2()
