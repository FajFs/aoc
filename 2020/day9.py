
def part1(d:list, pre:int) -> int:
    lookbackList = d[:pre]
    for i in range(pre, len(d)):
        needs = {j + k for j in lookbackList for k in lookbackList if j != k}
        if d[i] not in needs:
            return d[i]
        lookbackList = d[i + 1 - pre: i + 1]


def part2(d:list, invNum:int) -> int:
    for i in range(len(d)):
        res = [d[i]]
        j = i + 1
        while sum(res) < invNum:
            res.append(d[j])
            j += 1
            if i + j >= 2 and sum(res) == invNum:
                return min(res) + max(res)  
            

def main():
    inp = [int(x) for x in open("aoc/2020/inputfiles/day9.in", 'r').readlines()]
    invalidNumber = part1(inp, 25)
    print("part 1: ", invalidNumber)
    print("part 2: ",part2(inp, invalidNumber))
if __name__ == "__main__":
    main()