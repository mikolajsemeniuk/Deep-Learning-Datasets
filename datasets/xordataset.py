from typing import Final, List
import numpy as np
from datasets.basedataset import BaseDataset
import random

class XORDataset(BaseDataset):
    x: np.ndarray
    y: np.ndarray
    def __init__(self, samples: int = 150) -> None:
        x_choice: Final[List[List[int]]] = [[0, 0], [0, 1], [1, 0], [1, 1]]
        y_choice: Final[List[int]] = [0, 1, 1, 0]
        x, y = [], []
        for _ in range(samples):
            choice: int = random.randint(0, 3)
            x.append(x_choice[choice])
            y.append(y_choice[choice])
        self.x, self.y = np.array(x), np.array(y)
