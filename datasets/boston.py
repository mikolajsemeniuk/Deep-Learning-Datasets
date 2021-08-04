import numpy as np
from datasets.base import Base
from sklearn.datasets import load_boston
from typing import Dict

class Boston(Base):
    def __init__(self):
        boston: Dict[str, np.ndarray] = load_boston()
        self.x, self.y = boston['data'], boston['target']
        self.y = np.expand_dims(self.y, 1)
