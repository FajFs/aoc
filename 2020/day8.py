import copy
import sys

def execute(ins) -> (int, str):
    acc, ptr = 0, 0
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

def part2(instructions:list) -> (int, str):
    i = instructions[:]
    for idx in range(len(i)):
        i = copy.deepcopy(instructions)
        acc, err = 0, ""
        if i[idx].op == "jmp":
            i[idx].op = "nop"
            acc, err = execute(i)
        elif i[idx].op == "nop":
            i[idx].op = "jmp"
            acc, err = execute(i)
        
        if err == "ok":
            return acc, err

class Inst:
    def __init__(self, op:str, arg:int, offset:int):
        self.op = op
        self.arg = arg
        self.offset = offset

def main():
    inp = [x.strip() for x in open(sys.argv[1], 'r').readlines()]
    instructions = []
    for i, ins in enumerate(inp):
        op, arg = ins.split()
        instructions.append(Inst(op, int(arg), i))
    print("part 1: ", execute(instructions))
    print("part 2: ", part2(instructions))

if __name__ == "__main__":
    main()