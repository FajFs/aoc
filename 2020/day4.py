def ruleSet(k,v):
    switch = {
        "byr": lambda v: int(v) if 1920 <= int(v) <= 2002 else None,
        "iyr": lambda v: int(v) if 2010 <= int(v) <= 2020 else None,
        "eyr": lambda v: int(v) if 2020 <= int(v) <= 2030 else None,
        "hgt": lambda v: int(v[:-2]) if v[:-2].isnumeric() \
            and ((v.endswith("cm") and ( 150 <= int(v[:-2]) <= 193)) \
            or (v.endswith("in") and ( 59 <= int(v[:-2]) <= 76))) else None,

        "hcl": lambda v: v if v[0] == "#" and len(v[1:]) == 6 and v[1:].isalnum() else None,
        "ecl": lambda v: v if v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else None,
        "pid": lambda v: v if len(v) == 9 and v.isnumeric() else None,
        "cid": lambda v: v                  
    }
    return switch[k](v)

newP = {"byr":None, "iyr":None, "eyr":None, "hgt":None, "hcl":None, "ecl":None, "pid":None } #"cid":None

def part12(inp: list, part: str) -> int:
    passports = []
    p = newP.copy()
    for line in inp:
        if not line:
            if all(x != None for x in p.values()):
                passports.append(p)
            p = newP.copy()
        else:
            for info in line:
                k,v = info.split(":")
                p[k] = v if part == "p1" else ruleSet(k,v)
    #append last entry
    if all(x != None for x in p.values()):
        passports.append(p) 
    return len(passports)

def main():
    inp = [x.split() for x in open("aoc/2020/inputfiles/day4.in", 'r')]
    print("part 1: ", part12(inp, "p1"))
    print("part 2: ", part12(inp, "p2"))

if __name__ == "__main__":
    main()