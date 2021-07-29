from storage import Memory,Register,Stack
from datatype import Int
from instruction import ARGUMENTS, Instruction, JUMP_OPS, Opcode


class Machine:
    def __init__(self):
        self.registers = [Register(f'r{i}',Int(0)) for i in range(8)]
        self.stack = Stack()
        self.memory = Memory(2**15)

    def load_program(self,filename:str):
        address = Int(0)
        with open(filename,'rb') as program:
            while program.peek():
                self.memory.set(address,int.from_bytes(program.read(2), 'little'))
                address += 1

    def get(self,source:Int):
        if 32768 <= source <= 32775:
            return self.registers[source-32768].get()
        return source
    
    def set(self,dest:Int,source:Int):
        if 32768 <= dest <= 32775:
            self.registers[dest-32768].set(self.get(source))
        else:
            raise ValueError('Cannot set a constant')

    def execute(self,address:Int):
        pc = address
        while True:
            instr = Opcode(self.memory.get(pc))
            step = ARGUMENTS[instr]
            args = self.memory.get_range(pc+1,pc+step+1)
            if instr == Opcode.HALT:
                break

            elif instr == Opcode.OUT:
                char = chr(self.get(args[0]))
                print(char,end='')
            elif instr == Opcode.IN:
                pass

            elif instr == Opcode.NOOP:
                pass
            elif instr == Opcode.JMP:
                pc = self.get(args[0])
            elif instr == Opcode.JT:
                condition = self.get(args[0])
                if condition != 0:
                    pc = self.get(args[1])
                else:
                    pc += step + 1
            elif instr == Opcode.JF:
                condition = self.get(args[0])
                if condition == 0:
                    pc = self.get(args[1])
                else:
                    pc += step + 1

            elif instr == Opcode.SET:
                self.set(args[0],self.get(args[1]))

            elif instr == Opcode.ADD:
                dest = args[0]
                term_1 = self.get(args[1])
                term_2 = self.get(args[2])
                self.set(dest,(term_1+term_2)%2**15)
            elif instr == Opcode.MULT:
                dest = args[0]
                term_1 = self.get(args[1])
                term_2 = self.get(args[2])
                self.set(dest,(term_1*term_2)%2**15)
            elif instr == Opcode.MOD:
                dest = args[0]
                term_1 = self.get(args[1])
                term_2 = self.get(args[2])
                self.set(dest,term_1%term_2)

            elif instr == Opcode.EQ:
                dest = args[0]
                term_1 = self.get(args[1])
                term_2 = self.get(args[2])
                val = 1 if term_1 == term_2 else 0
                self.set(dest,val)

            elif instr == Opcode.PUSH:
                value = self.get(args[0])
                self.stack.push(value)
            elif instr == Opcode.POP:
                value = self.stack.pop()
                self.set(args[0],value)

            elif instr == Opcode.GT:
                dest = args[0]
                term_1 = self.get(args[1])
                term_2 = self.get(args[2])
                val = 1 if term_1 > term_2 else 0
                self.set(dest,val)

            elif instr == Opcode.AND:
                dest = args[0]
                term_1 = self.get(args[1])
                term_2 = self.get(args[2])
                self.set(dest,term_1 & term_2)
            elif instr == Opcode.OR:
                dest = args[0]
                term_1 = self.get(args[1])
                term_2 = self.get(args[2])
                self.set(dest,term_1 | term_2)
            elif instr == Opcode.NOT:
                dest = args[0]
                term_1 = self.get(args[1])

                self.set(dest,2**15-1-term_1)

            elif instr == Opcode.CALL:
                self.stack.push(pc+step+1)
                pc = self.get(args[0])
            elif instr == Opcode.RET:
                if len(self.stack) == 0:
                    break
                pc = self.stack.pop()

            elif instr == Opcode.RMEM:
                val = self.memory.get(self.get(args[1]))
                self.set(args[0],val)
            elif instr == Opcode.WMEM:
                self.memory.set(self.get(args[0]),self.get(args[1]))
            else:
                print(instr)


            if instr not in JUMP_OPS:
                pc += step + 1
            
