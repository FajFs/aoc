import re

test = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

def part1(data):
    res = 0
    for line in data:
        d = re.split('[-: ]+', line)
        if int(d[0]) <= d[3].count(d[2]) <= int(d[1]):
            res = res + 1
    print(res)


def part2(data):
    res = 0
    for line in data:
        d = re.split('[-: ]+', line)
        n = d[3][int(d[0])-1]
        m = d[3][int(d[1])-1]
        if (n == d[2] and not m == d[2]) or (not n == d[2] and m == d[2]): 
            res = res + 1
    print(res)

def main():
    inp = open("aoc/2020/inputfiles/day2.in", 'r').readlines()
    part1(inp)
    part2(inp)



if __name__ == "__main__":
    main()