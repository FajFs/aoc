
def part1(inp:list, pre:int) -> int:
    lookbackList = inp[:pre]
    for i in range(pre, len(inp)):
        needs = {j + k for j in lookbackList for k in lookbackList if j != k}
        if inp[i] not in needs:
            return inp[i]
        lookbackList = inp[i + 1 - pre: i + 1]

def part2(inp:list, invNum:int) -> int:
    for i in range(len(inp)):
        res = [inp[i]]
        j = i + 1
        while sum(res) < invNum:
            res.append(inp[j])
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