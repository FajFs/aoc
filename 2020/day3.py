import sys

def part1(inp: list) -> int:
    col, row, ans = 0, 0, 0
    while row < len(inp) - 1:
        row, col = row + 1, col + 3
        if inp[row][col % len(inp[row])] == "#":
            ans += 1
    return ans

move = [(1,1), (1,3), (1,5), (1,7), (2,1)]
def part2(inp: list) -> int:
    ans = 1
    for down, right in move:
        col, row, val = 0, 0, 0
        while row < len(inp)-1:
            row, col = row + down, col + right
            if inp[row][col % len(inp[row])] == "#":
                val += 1
        ans *= val
    return ans
        
def main():
    inp = [x.strip() for x in open(sys.argv[1], 'r').readlines()]
    print("part 1: ", part1(inp))
    print("part 2: ", part2(inp))

if __name__ == "__main__":
    main()