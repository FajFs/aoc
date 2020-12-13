import sys
import copy

directions = [(0,-1),(1,0),(-1,0),(0,1),\
            (1,1),(-1,1),(-1,-1),(1,-1)]

def part1(inp: list, tolerance: int) -> int:
    while True:
        modified = dict()
        for j in range(len(inp)):
            for i in range(len(inp[0])):
                e = inp[j][i]
                if e == ".":
                    continue
                counter = 0
                for jj, ii in directions:
                    if 0 <= i + ii < len(inp[0]) and 0 <= j + jj < len(inp):
                        if inp[j + jj][i + ii] == "#":
                            counter += 1
                            if e == "#" and counter >= tolerance:
                                modified[(j,i)] = "L" 
                                break
                if e == "L" and counter == 0:
                    modified[(j,i)] = "#" 
        
        for k, v in modified.items():
            inp[k[0]][k[1]] = v
        
        if not modified:
            return sum([x.count("#") for x in inp])
    

def part2(inp: list, tolerance: int) -> int:
    while True:
        modified = dict()
        for j in range(len(inp)):
            for i in range(len(inp[0])):
                e = inp[j][i]
                if e == ".":
                    continue
                counter = 0
                for jj, ii in directions:
                    for kk in range(1,len(inp)):
                        if 0 <= i + ii * kk < len(inp[0]) and 0 <= j + jj * kk < len(inp):
                            seat = inp[j + jj * kk][i + ii * kk]
                            if seat == "#":
                                counter += 1
                                break
                            if seat == "L":
                                break
                    if e == "#" and counter >= tolerance:
                        modified[(j,i)] = "L" 
                        break                     
                if e == "L" and counter == 0:
                    modified[(j,i)] = "#" 
        
        for k, v in modified.items():
            inp[k[0]][k[1]] = v
        if not modified:
            return sum([x.count("#") for x in inp])

def main():
    inp = [list(x.strip()) for x in open(sys.argv[1], "r").readlines()]
    inp2 = copy.deepcopy(inp)
    print("part 1: ", part1(inp, 4))
    print("part 2: ", part2(inp2, 5))
if __name__ == "__main__":
    main()