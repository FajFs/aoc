import sys

def part1(inp: list) -> int:
    diff = [inp[i + 1] - inp[i] for i in range(len(inp) - 1)]   
    return diff.count(1) * diff.count(3)


def part2(inp: list) -> int:
    print("TBD")

def main():
    inp = [int(x) for x in open("aoc/2020/input/day10.in", 'r').readlines()]
    inp.extend([0,max(inp) + 3])
    inp.sort()
    print("part 1: ", part1(inp))
    part2(inp)

if __name__ == "__main__":
    main()