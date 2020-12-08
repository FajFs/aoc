test = ["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.", "..#.##.....", ".#.#.#....#", ".#........#", "#.##...#...", "#...##....#", ".#..#...#.#"]

def part1(d):
    c = 0
    r = 0
    ans = 0
    while r < len(d)-1:
        r += 1
        c += 3
        if d[r][c%len(d[r])] == "#":
            ans += 1
    print(ans)

    

move = [(1,1), (1,3), (1,5), (1,7), (2,1)]

def part2(d):
    ans = 1
    for row, col in move:
        c = 0
        r = 0
        val = 0
        while r < len(d)-1:
            r += row
            c += col
            if d[r][c%len(d[r])] == "#":
                val += 1
        ans *= val
    print(ans)
        


def main():
    inp = open("aoc/2020/inputfiles/day3.in", 'r').readlines()
    graph = []
    for line in inp:
        graph.append(line.strip())
        
    part1(graph)
    part2(graph)



if __name__ == "__main__":
    main()