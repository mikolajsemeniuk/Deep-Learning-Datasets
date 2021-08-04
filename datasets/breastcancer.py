import numpy as np
from datasets.base import Base
from sklearn.datasets import load_breast_cancer
from typing import Dict

class BreastCancer(Base):
    def __init__(self):
        breast_cancer: Dict[str, np.ndarray] = load_breast_cancer()
        self.x, self.y = breast_cancer['data'], breast_cancer['target']
        self.y = np.expand_dims(self.y, 1)
