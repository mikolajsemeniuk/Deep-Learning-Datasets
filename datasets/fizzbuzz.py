from datasets.base import Base
from typing import List
import numpy as np


class FizzBuzz(Base):
    def __init__(self, samples: int = 150):
        self.x = np.array( [self.get_x(i) for i in range(samples)] )
        self.y = np.array( [self.get_y(i) for i in range(samples)] )

    def get_x(self, number: int) -> List[int]:
        return [number]

    def get_y(self, number: int) -> List[int]:
        if number % 15 == 0:
            return [0, 0, 0, 1]
        elif number % 5 == 0:
            return [0, 0, 1, 0]
        elif number % 3 == 0:
            return [0, 1, 0, 0]
        else:
            return [1, 0, 0, 0]
