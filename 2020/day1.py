test = [1721,979,366,299,675,1456]


def part1(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                print(i*j)
                return


def part2(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(i*j*k)
                    return

def main():
    inp = open("aoc/2020/inputfiles/day1.in", 'r').readlines()
    data = list(map(int, inp))
    part1(data)
    part2(data)



if __name__ == "__main__":
    main()