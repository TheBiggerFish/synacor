import numpy as np
from datatype import Int
from collections import deque

class Memory:
    def __init__(self,size):
        self.size = size
        self.array = list(np.zeros(size,Int))

    def set(self,address,value:Int):
        self.array[address] = value

    def get(self,address):
        return self.array[address]
    
    def get_range(self,add_low,add_high):
        return self.array[add_low:add_high]

    def dump(self,rows:Int=0):
        end = self.size if rows==0 else rows*16
        for row in range(0,end,16):
            for col in range(0,16):
                print(str(self.array[row+col]),end=' ')
            print()

class Stack(deque):
    def push(self,value:Int):
        super().append(Int(value))

class Register:
    def __init__(self,id:str,initial:Int):
        self.id = id
        self.val = initial

    def get(self):
        return Int(self.val)

    def set(self,val:Int):
        self.val = Int(val)