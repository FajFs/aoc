import re

class Bag:
    mult = 1
    def __init__(self, v, c):
        self.value = v
        self.color = c

#Bottom up
def part1(d):
    parents = set()
    res = set()
    #prepare first case
    for (k,v) in d.items():
        if "shinygold" in [x.color for x in v]:
            parents.add(k)
            res.add(k)

    while parents:
        p = parents.pop()
        for (k,v) in d.items():
            if p in [x.color for x in v]:
                parents.add(k)
                res.add(k)
    print("part 1: ", len(res))


#Top down - recursive preorder node count times node value
def rec_count(children, fullList):
    res = 1
    for c in children:
        res += c.value * rec_count(fullList[c.color], fullList)
    return res


def part2(d):
    print("part 2: ", rec_count(d["shinygold"], d) - 1)



def main():
    inp = [x.strip() for x in open("aoc/2020/inputfiles/day7.in", 'r').readlines()]
    # tree structure 
    #filter strings.
    filteredInput = {}
    for line in inp:
        line = line.replace("bags","").replace("contain","").replace("bag","").replace(".","").replace(" ","").replace(",","").replace("noother","")
        tmp = re.split("([0-9]+)", line)
        bags = []
        for i in range(1, len(tmp), 2):
            bags.append(Bag(int(tmp[i]), tmp[i+1]))
        filteredInput[tmp[0]] = bags



    part1(filteredInput)
    part2(filteredInput)




if __name__ == "__main__":
    main()