import numpy as np
from datasets.base import Base
from sklearn.datasets import make_moons

class Moons(Base):
    def __init__(self, samples: int = 150, noise = 0.035, random_state = 10) -> None:
        self.x, self.y = make_moons(n_samples = samples, noise = noise, random_state = random_state)
        self.y = np.expand_dims(self.y, 1)