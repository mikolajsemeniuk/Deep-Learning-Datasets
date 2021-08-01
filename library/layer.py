from typing import Callable
import numpy as np
import numpy.ndarray as Tensor

class Layer:
    def __init__(self, in_dimension, out_dimension):
        self.weights = np.random.randn(in_dimension, out_dimension) * 0.01
        self.bias = np.zeros((1, out_dimension))
    def forward(self, tensor: Tensor):
        self.inputs = tensor
        return tensor @ self.weights + self.bias