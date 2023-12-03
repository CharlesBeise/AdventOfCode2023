def part1():
    total = 0
    with open("day2_input.txt") as infile:
        for line in infile.read().splitlines():
            front, end = line.split(':')
            cur = int(front.split(' ')[1])
            cubes = {
                "red": 0,
                "blue": 0,
                "green": 0
                }
            groups = end.split(';')
            for group in groups:
                pairs = group.split(',')
                for pair in pairs:
                    pair = pair.split(" ")
                    cubes[pair[2]] = max(cubes[pair[2]], int(pair[1]))

            if cubes["red"] <= 12 and cubes["blue"] <= 14 and \
                    cubes["green"] <= 13:
                total += cur

    return total


def part2():
    total = 0
    with open("day2_input.txt") as infile:
        for line in infile.read().splitlines():
            front, end = line.split(':')
            cur = int(front.split(' ')[1])
            cubes = {
                "red": 1,
                "blue": 1,
                "green": 1
                }
            groups = end.split(';')
            for group in groups:
                pairs = group.split(',')
                for pair in pairs:
                    pair = pair.split(" ")
                    cubes[pair[2]] = max(cubes[pair[2]], int(pair[1]))

            total += (cubes["red"] * cubes["blue"] * cubes["green"])

    return total


if __name__ == '__main__':
    print(part2())
