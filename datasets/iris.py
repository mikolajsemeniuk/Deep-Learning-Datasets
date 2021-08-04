import numpy as np
from datasets.base import Base
from sklearn.datasets import load_iris
from typing import Dict

class Iris(Base):
    def __init__(self):
        iris: Dict[str, np.ndarray] = load_iris()
        self.x, self.y = iris['data'], iris['target']
        self.y = np.expand_dims(self.y, 1)
