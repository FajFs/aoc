def part1(inp: list) -> int:
    entries, e = [], ""
    for line in inp:
        if not line:
            entries.append(e)
            e = ""
        else:
            e += line
    entries.append(e)

    res = 0
    for line in entries:
        res += len(set(line))
    return res

def part2(inp: list) -> int:
    entries, e = [], []
    for line in inp:
        if not line:
            entries.append(e)
            e = list()
        else:
            e.append(set([c for c in line]))
    entries.append(e)
    
    res = []
    for e in entries:
        res.append(len((e[0].intersection(*e))))
    return sum(res)

def main():
    inp = [x.strip() for x in open("aoc/2020/inputfiles/day6.in", 'r').readlines()]
    print("part 1: ", part1(inp))
    print("part 2: ", part2(inp))

if __name__ == "__main__":
    main()