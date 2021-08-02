import numpy as np

class BaseDataset:
    x: np.ndarray
    y: np.ndarray
    def __init__(self, samples: int = 150) -> None:
        raise NotImplemented()
    def __repr__(self): 
        return f"x shape: {self.x.shape}, y shape: {self.y.shape}"
