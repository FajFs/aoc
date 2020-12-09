import re

#Bottom up
def part1(inp: list) -> int:
    parents = set()
    res = set()
    #prepare first case
    for (k,v) in inp.items():
        if "shinygold" in [x.color for x in v]:
            parents.add(k)
            res.add(k)

    while parents:
        p = parents.pop()
        for (k,v) in inp.items():
            if p in [x.color for x in v]:
                parents.add(k)
                res.add(k)
    return len(res)

#Top down - recursive preorder node count times node value
def rec_count(children: list, fullList: list) -> int:
    res = 1
    for c in children:
        res += c.value * rec_count(fullList[c.color], fullList)
    return res

def part2(inp: list) -> int:
    return rec_count(inp["shinygold"], inp) - 1

class Bag:
    def __init__(self, v, c):
        self.value = v
        self.color = c

def main():
    inp = [x.strip() for x in open("aoc/2020/inputfiles/day7.in", 'r').readlines()]
    filteredInput = {}
    for line in inp:
        line = line.replace("bags","").replace("contain","").replace("bag","").replace(".","").replace(" ","").replace(",","").replace("noother","")
        tmp = re.split("([0-9]+)", line)
        bags = []
        for i in range(1, len(tmp), 2):
            bags.append(Bag(int(tmp[i]), tmp[i+1]))
        filteredInput[tmp[0]] = bags
    print("part 1: ", part1(filteredInput))
    print("part 2: ", part2(filteredInput))

if __name__ == "__main__":
    main()