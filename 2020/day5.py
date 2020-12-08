import math


def part12(data):
    ids = []
    for line in data:
        rowHigh = 127
        rowLow = 0
        for row in range(0, 7):
            if line[row] == "F":
                rowHigh = (rowHigh + rowLow) // 2
            if line[row] == "B":
                rowLow = math.ceil((rowHigh + rowLow) / 2)
        
        colLow = 8
        colHigh = 0 
        for col in range(7,10):
            if line[col] == "R":
                colHigh = (colHigh + colLow) // 2
            if line[col] == "L":
                colLow = math.ceil((colHigh + colLow) / 2)
        
        ids.append(rowHigh * 8 + colHigh)
    print("p1: ", max(ids))

    res = []
    comp = range(0, max(ids))
    for i in comp:
        if i not in ids:
            res.append(i)
    print("p2: ", max(res))


def main():
    inp = open("aoc/2020/inputfiles/day5.in", 'r').readlines()
    part12(inp)
    



if __name__ == "__main__":
    main()  