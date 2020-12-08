def part1(data):
    entries = []
    e = ""
    for line in data:
        if not line:
            entries.append(e)
            e = ""
        else:
            e += line
    entries.append(e)

    res = 0
    for line in entries:
        res += len(set(line))
    print(res)


def part2(data):
    entries = list()
    e = list()
    for line in data:
        if not line:
            entries.append(e)
            e = list()
        else:
            e.append(set([c for c in line]))
    entries.append(e)
    
    res = []
    for e in entries:
        res.append(len((e[0].intersection(*e))))
    print(sum(res))

   

    

def main():
    inp = [x.strip() for x in open("aoc/2020/inputfiles/day6.in", 'r').readlines()]
    part1(inp)
    part2(inp)




if __name__ == "__main__":
    main()