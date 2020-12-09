def part1(inp: list) -> int:
    deltaDict = {(2020 - i): i 
                for i in inp}
    for i in inp:
        if i in deltaDict:
            return i * deltaDict[i]

def part2(inp: list) -> int:
    deltaDict = {(2020 - i - j): (i,j)
                    for i in inp 
                    for j in inp 
                    if i != j}
    for i in inp:
        if i in deltaDict:
            return i * deltaDict[i][0] * deltaDict[i][1]

def main():
    inp = [int(x) for x in open("aoc/2020/inputfiles/day1.in", 'r').readlines()]
    print("part 1: ", part1(inp))
    print("part 2: ", part2(inp))

if __name__ == "__main__":
    main()