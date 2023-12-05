def part1():
    grid = []
    symbols = set()

    with open("day3_input.txt") as infile:
        for line in infile.readlines():
            for char in line:
                if not char.isnumeric():
                    symbols.add(char)
            grid.append(list(line.strip('\n')))

    symbols -= {'\n', '.'}

    x = 1

    total = 0
    for row in range(len(grid)):
        if row - 2 > 0:
            print(grid[row-2])
        for char in range(len(grid[row])):
            if grid[row][char] in symbols:
                x += 1
                # Check the adjacent squares to see if they contain a number
                if char > 0:
                    if row > 0:
                        # Up and Left
                        if grid[row-1][char-1].isnumeric():
                            num = grid[row-1][char-1]
                            grid[row-1][char-1] = '.'
                            left, right = 2, 0
                            while char-left >= 0 and grid[row-1][char-left].isnumeric():
                                num = grid[row-1][char-left] + num
                                grid[row-1][char-left] = '.'
                                left += 1
                            while char+right < len(grid[row]) and grid[row-1][char+right].isnumeric():
                                num += grid[row-1][char+right]
                                grid[row-1][char+right] = '.'
                                right += 1
                            total += int(num)
                    if row < len(grid):
                        # Down and Left
                        if grid[row+1][char-1].isnumeric():
                            num = grid[row+1][char-1]
                            grid[row+1][char-1] = '.'
                            left, right = 2, 0
                            while char-left >= 0 and grid[row+1][char-left].isnumeric():
                                num = grid[row+1][char-left] + num
                                grid[row+1][char-left] = '.'
                                left += 1
                            while char+right < len(grid[row]) and grid[row+1][char+right].isnumeric():
                                num += grid[row+1][char+right]
                                grid[row+1][char+right] = '.'
                                right += 1
                            total += int(num)
                    # Left
                    if grid[row][char-1].isnumeric():
                        num = grid[row][char-1]
                        grid[row][char - 1] = '.'
                        left = 2
                        while char-left >= 0 and grid[row][char-left].isnumeric():
                            num = grid[row][char-left] + num
                            grid[row][char-left] = '.'
                            left += 1
                        total += int(num)

                if row > 0:
                    # Up
                    if grid[row - 1][char].isnumeric():
                        num = grid[row - 1][char]
                        grid[row - 1][char] = '.'
                        left, right = 1, 1
                        while char - left >= 0 and grid[row - 1][
                            char - left].isnumeric():
                            num = grid[row - 1][char - left] + num
                            grid[row - 1][char - left] = '.'
                            left += 1
                        while char + right < len(grid[row]) and grid[row - 1][
                            char + right].isnumeric():
                            num += grid[row - 1][char + right]
                            grid[row - 1][char + right] = '.'
                            right += 1
                        total += int(num)
                if char < len(grid[row])-1:
                    if row > 0:
                        # Up and Right
                        if grid[row - 1][char+1].isnumeric():
                            num = grid[row - 1][char+1]
                            grid[row - 1][char+1] = '.'
                            left, right = 0, 2
                            while char - left >= 0 and grid[row - 1][
                                char - left].isnumeric():
                                num = grid[row - 1][char - left] + num
                                grid[row - 1][char - left] = '.'
                                left += 1
                            while char + right < len(grid[row]) and grid[row - 1][
                                char + right].isnumeric():
                                num += grid[row - 1][char + right]
                                grid[row - 1][char + right] = '.'
                                right += 1
                            total += int(num)
                    if row < len(grid):
                        # Down and Right
                        if grid[row + 1][char+1].isnumeric():
                            num = grid[row + 1][char+1]
                            grid[row + 1][char+1] = '.'
                            left, right = 0, 2
                            while char - left >= 0 and grid[row + 1][
                                char - left].isnumeric():
                                num = grid[row + 1][char - left] + num
                                grid[row + 1][char - left] = '.'
                                left += 1
                            while char + right < len(grid[row]) and grid[row + 1][
                                char + right].isnumeric():
                                num += grid[row + 1][char + right]
                                grid[row + 1][char + right] = '.'
                                right += 1
                            total += int(num)
                    # Right
                    if grid[row][char+1].isnumeric():
                        num = grid[row][char+1]
                        grid[row][char+1] = '.'
                        right = 2
                        while char+right < len(grid[row]) and grid[row][char+right].isnumeric():
                            num = num + grid[row][char+right]
                            grid[row][char+right] = '.'
                            right += 1
                        total += int(num)
                if row < len(grid) - 1:
                    # Down
                    if grid[row+1][char].isnumeric():
                        num = grid[row+1][char]
                        grid[row+1][char] = '.'
                        left, right = 1, 1
                        while char - left >= 0 and grid[row+1][
                            char - left].isnumeric():
                            num = grid[row+1][char - left] + num
                            grid[row+1][char - left] = '.'
                            left += 1
                        while char + right < len(grid[row]) and grid[row+1][
                            char + right].isnumeric():
                            num += grid[row+1][char + right]
                            grid[row+1][char + right] = '.'
                            right += 1
                        total += int(num)

    print(total)


def part2():
    grid = []

    with open("day3_input.txt") as infile:
        for line in infile.readlines():
            grid.append(list(line.strip('\n')))

    x = 1

    total = 0
    for row in range(len(grid)):
        if row - 2 > 0:
            print(grid[row - 2])
        for char in range(len(grid[row])):
            if grid[row][char] == '*':
                gear = []
                x += 1
                # Check the adjacent squares to see if they contain a number
                if char > 0:
                    if row > 0:
                        # Up and Left
                        if grid[row - 1][char - 1].isnumeric():
                            num = grid[row - 1][char - 1]
                            grid[row - 1][char - 1] = '.'
                            left, right = 2, 0
                            while char - left >= 0 and grid[row - 1][
                                char - left].isnumeric():
                                num = grid[row - 1][char - left] + num
                                grid[row - 1][char - left] = '.'
                                left += 1
                            while char + right < len(grid[row]) and \
                                    grid[row - 1][char + right].isnumeric():
                                num += grid[row - 1][char + right]
                                grid[row - 1][char + right] = '.'
                                right += 1
                            gear.append(num)
                    if row < len(grid):
                        # Down and Left
                        if grid[row + 1][char - 1].isnumeric():
                            num = grid[row + 1][char - 1]
                            grid[row + 1][char - 1] = '.'
                            left, right = 2, 0
                            while char - left >= 0 and grid[row + 1][
                                char - left].isnumeric():
                                num = grid[row + 1][char - left] + num
                                grid[row + 1][char - left] = '.'
                                left += 1
                            while char + right < len(grid[row]) and \
                                    grid[row + 1][char + right].isnumeric():
                                num += grid[row + 1][char + right]
                                grid[row + 1][char + right] = '.'
                                right += 1
                            gear.append(num)
                    # Left
                    if grid[row][char - 1].isnumeric():
                        num = grid[row][char - 1]
                        grid[row][char - 1] = '.'
                        left = 2
                        while char - left >= 0 and grid[row][
                            char - left].isnumeric():
                            num = grid[row][char - left] + num
                            grid[row][char - left] = '.'
                            left += 1
                        gear.append(num)

                if row > 0:
                    # Up
                    if grid[row - 1][char].isnumeric():
                        num = grid[row - 1][char]
                        grid[row - 1][char] = '.'
                        left, right = 1, 1
                        while char - left >= 0 and grid[row - 1][
                            char - left].isnumeric():
                            num = grid[row - 1][char - left] + num
                            grid[row - 1][char - left] = '.'
                            left += 1
                        while char + right < len(grid[row]) and grid[row - 1][
                            char + right].isnumeric():
                            num += grid[row - 1][char + right]
                            grid[row - 1][char + right] = '.'
                            right += 1
                        gear.append(num)
                if char < len(grid[row]) - 1:
                    if row > 0:
                        # Up and Right
                        if grid[row - 1][char + 1].isnumeric():
                            num = grid[row - 1][char + 1]
                            grid[row - 1][char + 1] = '.'
                            left, right = 0, 2
                            while char - left >= 0 and grid[row - 1][
                                char - left].isnumeric():
                                num = grid[row - 1][char - left] + num
                                grid[row - 1][char - left] = '.'
                                left += 1
                            while char + right < len(grid[row]) and \
                                    grid[row - 1][
                                        char + right].isnumeric():
                                num += grid[row - 1][char + right]
                                grid[row - 1][char + right] = '.'
                                right += 1
                            gear.append(num)
                    if row < len(grid):
                        # Down and Right
                        if grid[row + 1][char + 1].isnumeric():
                            num = grid[row + 1][char + 1]
                            grid[row + 1][char + 1] = '.'
                            left, right = 0, 2
                            while char - left >= 0 and grid[row + 1][
                                char - left].isnumeric():
                                num = grid[row + 1][char - left] + num
                                grid[row + 1][char - left] = '.'
                                left += 1
                            while char + right < len(grid[row]) and \
                                    grid[row + 1][
                                        char + right].isnumeric():
                                num += grid[row + 1][char + right]
                                grid[row + 1][char + right] = '.'
                                right += 1
                            gear.append(num)
                    # Right
                    if grid[row][char + 1].isnumeric():
                        num = grid[row][char + 1]
                        grid[row][char + 1] = '.'
                        right = 2
                        while char + right < len(grid[row]) and grid[row][
                            char + right].isnumeric():
                            num = num + grid[row][char + right]
                            grid[row][char + right] = '.'
                            right += 1
                        gear.append(num)
                if row < len(grid) - 1:
                    # Down
                    if grid[row + 1][char].isnumeric():
                        num = grid[row + 1][char]
                        grid[row + 1][char] = '.'
                        left, right = 1, 1
                        while char - left >= 0 and grid[row + 1][
                            char - left].isnumeric():
                            num = grid[row + 1][char - left] + num
                            grid[row + 1][char - left] = '.'
                            left += 1
                        while char + right < len(grid[row]) and grid[row + 1][
                            char + right].isnumeric():
                            num += grid[row + 1][char + right]
                            grid[row + 1][char + right] = '.'
                            right += 1
                        gear.append(num)
                if len(gear) == 2:
                    total += (int(gear[0]) * int(gear[1]))
    print(total)

# 86879020

if __name__ == '__main__':
    part2()
