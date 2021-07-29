import numpy as np

class Int(np.uint16):
    MAX = 2**16-1
    def __add__(self, other):
        return Int(int(self) + int(other))

    def __sub__(self, other):
        return Int(int(self) - int(other))