import copy

class Inst:
    def __init__(self, op:str, arg:int, offset:int):
        self.op = op
        self.arg = arg
        self.offset = offset


def execute(ins) -> (int, str):
    acc = 0
    ptr = 0
    executedInstructions = set()

    while True:
        #Check if program exited properly
        if ptr >= len(ins):
            return (acc, "ok")

        #Terminate the program if the instruction has been executed before
        if ins[ptr].offset in executedInstructions:
            return (acc, "err")
        else:
            executedInstructions.add(ins[ptr].offset)
        
        #Execute intruction
        if ins[ptr].op == "nop":
            ptr += 1
            continue
        if ins[ptr].op == "acc":
            acc += ins[ptr].arg
            ptr += 1
            continue
        if ins[ptr].op == "jmp":
            ptr += ins[ptr].arg
            continue



def part2(instructions:list):
    i = instructions[:]
    for idx in range(len(i)):
        i = copy.deepcopy(instructions)
        acc = 0
        err = ""
        if i[idx].op == "jmp":
            i[idx].op = "nop"
            acc, err = execute(i)

        elif i[idx].op == "nop":
            i[idx].op = "jmp"
            acc, err = execute(i)
        
       # print(acc, err)
        if err == "ok":
            print(acc, err)
            return

def main():
    inp = [x.strip() for x in open("aoc/2020/inputfiles/day8.in", 'r').readlines()]
    # tree structure 
    #filter strings.
    instructions = []
    for i, ins in enumerate(inp):
        op, arg = ins.split()
        instructions.append(Inst(op, int(arg), i))
    print(execute(instructions))
    part2(instructions)


    

if __name__ == "__main__":
    main()