from enum import Enum

class Opcode(Enum):
    HALT = 0
    SET = 1
    PUSH = 2
    POP = 3
    EQ = 4
    GT = 5
    JMP = 6
    JT = 7
    JF = 8
    ADD = 9
    MULT = 10
    MOD = 11
    AND = 12
    OR = 13
    NOT = 14
    RMEM = 15
    WMEM = 16
    CALL = 17
    RET = 18
    OUT = 19
    IN = 20
    NOOP = 21

ARGUMENTS = {
    Opcode.HALT: 0,
    Opcode.SET: 2,
    Opcode.PUSH: 1,
    Opcode.POP: 1,
    Opcode.EQ: 3,
    Opcode.GT: 3,
    Opcode.JMP: 1,
    Opcode.JT: 2,
    Opcode.JF: 2,
    Opcode.ADD: 3,
    Opcode.MULT: 3,
    Opcode.MOD: 3,
    Opcode.AND: 3,
    Opcode.OR: 3,
    Opcode.NOT: 2,
    Opcode.RMEM: 2,
    Opcode.WMEM: 2,
    Opcode.CALL: 1,
    Opcode.RET: 0,
    Opcode.OUT: 1,
    Opcode.IN: 1,
    Opcode.NOOP: 0
}

JUMP_OPS = {
    Opcode.JMP,
    Opcode.JT,
    Opcode.JF,
    Opcode.CALL,
    Opcode.RET
}


class Instruction:
    def __init__(self,opcode:Opcode,arguments:list):
        self.opcode = opcode