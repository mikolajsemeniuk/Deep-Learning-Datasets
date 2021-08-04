from typing import Tuple
import numpy as np

class Base:
    x: np.ndarray
    y: np.ndarray
    
    def __call__(self) -> Tuple[np.ndarray, np.ndarray]:
        return self.x, self.y

    def __repr__(self) -> str:
        return f"x shape: {self.x.shape}, y shape: {self.y.shape}"
