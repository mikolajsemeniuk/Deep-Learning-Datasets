import numpy as np
from datasets.base import Base
from typing import List

class Binary(Base):
    def __init__(self, samples: int = 150) -> None:
        self.x = np.array( [self.get_x(i) for i in range(samples)] )
        self.y = np.array( [self.get_y(i) for i in range(samples)] )

    def get_x(self, number: int) -> List[int]:
        binary_array = [number >> i & 1 for i in range(16)]
        return binary_array[::-1]

    def get_y(self, number: int) -> List[int]:
        return [number]
