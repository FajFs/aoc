import re

def part1(inp: list) -> int:
    res = 0
    for line in inp:
        minVal, maxVal, c, psw = re.split('[-: ]+', line)
        if int(minVal) <= psw.count(c) <= int(maxVal):
            res = res + 1
    return res

def part2(inp: list) -> int:
    res = 0
    for line in inp:
        posA, posB, c, psw = re.split('[-: ]+', line)
        ca, cb = psw[int(posA)-1], psw[int(posB)-1]
        if (ca == c and not cb == c) or (not ca == c and cb == c): 
            res = res + 1
    return res

def main():
    inp = open("aoc/2020/inputfiles/day2.in", 'r').readlines()
    print("part 1: ", part1(inp))
    print("part 2: ", part2(inp))

if __name__ == "__main__":
    main()