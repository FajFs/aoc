
def dataValidator(k,v):
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

def part12(d , part):
    passports = []
    p = newP.copy()
    for line in d:
        if not line:
            passports.append(p)
            p = newP.copy()
        else:
            for info in line:
                k,v = info.split(":")
                p[k] = v if part == "p1" else dataValidator(k,v)
    passports.append(p) #append last entry
    
    ans = 0
    for p in passports:
        if all(x != None for x in p.values()):
            ans += 1   
    print(part, ans)








def main():
    f = open("aoc/2020/inputfiles/day4.in", 'r')
    inp = [x.split() for x in f.readlines()]
    part12(inp, "p1")
    part12(inp, "p2")


if __name__ == "__main__":
    main()