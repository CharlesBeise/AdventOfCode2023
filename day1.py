# Part 1
def part1():
    nums = []
    with open("day1_input.txt") as infile:
        for line in infile.readlines():
            tempLine = []
            for char in line:
                if char.isnumeric():
                    tempLine.append(char)
            nums.append(tempLine)

    total = 0

    for num in nums:
        total += int(num[0] + num[-1])

    print(total)


# Part 2
def part2():
    num_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    rawLines = []
    with open("day1_input.txt") as infile:
        for line in infile:
            rawLines.append(line.strip('\n'))

    numbers = []
    for test in rawLines:
        for key in num_dict.keys():
            while key in test:
                spot = test.index(key)
                test = list(test)
                test[spot + 1] = num_dict[key]
                test = ''.join(test)
        numbers.append(test)

    nums = []
    for cur in numbers:
        tempNum = []
        for char in cur:
            if char.isnumeric():
                tempNum.append(char)
        nums.append(tempNum)

    total = 0
    i = 0
    for num in nums:
        total += int(num[0] + num[-1])
        i += 1

    return total


if __name__ == '__main__':
    print(part2())
