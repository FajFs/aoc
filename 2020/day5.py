import math

def part12(inp: list) -> (int, int):
    id = []
    res = []

    floor = lambda a,b: (a + b) // 2
    ceil  = lambda a,b: math.ceil((a + b) / 2)
    
    for line in inp:
        rowH, rowL = 127, 0
        colH, colL = 8, 0

        for c in line:
            if c == "F": 
                rowH = floor(rowH, rowL)
            if c == "B":
                rowL = ceil(rowH, rowL)
            if c == "L":
                colH = floor(colH, colL)
            if c == "R":
                colL = ceil(colH, colL)      
        id.append(rowH * 8 + colL)
        
    for i in [x for x in range(0, max(id))]:
        if i not in id:
            res.append(i)
    return max(id), max(res)

def main():
    inp = [x.strip() for x in open("aoc/2020/inputfiles/day5.in", 'r').readlines()]
    a,b = part12(inp)
    print("part 1: ", a)
    print("part 2: ", b)

if __name__ == "__main__":
    main()  