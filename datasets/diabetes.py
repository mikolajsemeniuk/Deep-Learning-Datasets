import numpy as np
from datasets.base import Base
from sklearn.datasets import load_diabetes
from typing import Dict

class Diabetes(Base):
    def __init__(self):
        diabetes: Dict[str, np.ndarray] = load_diabetes()
        self.x, self.y = diabetes['data'], diabetes['target']
        self.y = np.expand_dims(self.y, 1)
