def part1():
    with open("day5_input.txt") as infile:
        start = infile.read()

    numbers = ""
    for char in start:
        if char.isnumeric() or char.isspace() or char == ':':
            numbers += char

    values = numbers.split(":")

    final = []
    values.pop(0)

    for val in values:
        final.append(val.replace('\n', ' '))

    data = []
    for fin in final:
        temp = fin.split(" ")
        while "" in temp:
            temp.remove("")
        data.append(temp)

    info = []
    for row in data:
        temp = []
        for val in row:
            temp.append(int(val))
        info.append(temp)

    seeds = info.pop(0)

    almanac = {}
    for i in range(len(info)):
        temp = []
        cur = []
        for j in range(len(info[i])):
            cur.append(info[i][j])
            if len(cur) == 3:
                temp.append(cur)
                cur = []

        almanac[i] = temp

    lowest = float('inf')

    answers = {}

    for a in range(0, len(seeds), 2):
        for seed in range(seeds[a], seeds[a] + seeds[a+1]):
            if seed not in answers.keys():
                for i in range(len(info)):
                    for location in almanac[i]:
                        d, s, r = location
                        if s <= seed <= (s+r):
                            seed = (d + (seed - s))
                            break
            answers[seeds[a]] = seed
            lowest = min(lowest, seed)

    print(lowest)


if __name__ == '__main__':
    part1()
