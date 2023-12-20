def part1():
    with open("test_input.txt") as infile:
        inTime = infile.readline().split(" ")
        inDist = infile.readline().split(" ")

    time = []
    dist = []
    for spot in inTime:
        if spot and spot[0].isnumeric():
            time.append(int(spot.strip('\n')))

    for spot in inDist:
        if spot and spot[0].isnumeric():
            dist.append(int(spot.strip('\n')))

    results = []
    for i in range(len(time)):
        curTime = time[i]
        curDist = dist[i]
        mid = curTime // 2
        offset = 1
        total = 0

        if (curTime % 2 == 0) and (mid * (curTime - mid)) > curDist:
            total += 1

        for j in range(curTime):
            if (mid + offset) * (curTime - mid - offset) > curDist:
                total += 2
            else:
                break

            offset += 1

        results.append(total)

    print(results)

    answer = 1

    for i in results:
        answer *= i

    print("Answer:", answer)


def part2():
    with open("day6_input.txt") as infile:
        inTime = [char for char in infile.readline() if char.isnumeric()]
        inDist = [char for char in infile.readline() if char.isnumeric()]

    curTime = int(''.join(inTime))
    curDist = int(''.join(inDist))

    while True:
        mid = curTime // 2
        offset = 1
        total = 0

        if (curTime % 2 == 0) and (mid * (curTime - mid)) > curDist:
            total += 1

        for j in range(curTime):
            if (mid + offset) * (curTime - mid - offset) > curDist:
                total += 2
            else:
                break

            offset += 1

        print(total)
        break




if __name__ == '__main__':
    part2()
