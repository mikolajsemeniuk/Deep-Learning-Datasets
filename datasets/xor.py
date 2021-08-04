import numpy as np
from datasets.base import Base
from typing import List

class XOR(Base):
    def __init__(self, samples: int = 150) -> None:
        self.x = np.array( [self.get_x(i) for i in range(samples)] )
        self.y = np.array( [self.get_y(i) for i in range(samples)] )

    def get_x(self, number: int) -> List[int]:
        xor = [[0, 0], [0, 1], [1, 0], [1, 1]]
        return xor[number % len(xor)]

    def get_y(self, number: int) -> List[int]:
        xor = [[0], [1], [1], [0]]
        return xor[number % len(xor)]
