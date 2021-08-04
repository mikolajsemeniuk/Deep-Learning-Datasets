import nnfs
import numpy as np
from datasets.base import Base
from nnfs.datasets import spiral_data

class Spiral(Base):
    def __init__(self, samples: int = 150, classes: int = 3) -> None:
        nnfs.init()
        self.x, self.y = spiral_data(samples=samples, classes=classes)
        self.y = np.expand_dims(self.y, 1)
