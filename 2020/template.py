def part1(data):
    print("part1")


def part2(data):
    print("part2")

def main():
    inp = open("aoc/2020/inputfiles/dayx.in", 'r').readlines()
    data = list(map(int, inp))
    part1(data)
    part2(data)



if __name__ == "__main__":
    main()