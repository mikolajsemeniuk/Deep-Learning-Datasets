from typing import List, Tuple
import numpy as np
from nnfs.datasets import spiral_data, vertical_data
import nnfs
import random
from sklearn.datasets import make_moons, \
                             make_circles, \
                             load_breast_cancer, \
                             load_iris, \
                             load_boston, \
                             load_diabetes
                            
nnfs.init()
breast_cancer = load_breast_cancer()
iris = load_iris()
boston = load_boston()
diabetes = load_diabetes()

# x1

def generate_xor_dataset(samples: int = 150) -> Tuple[np.ndarray, np.ndarray]:
    x_choice: List[List[int]] = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y_choice: List[int] = [0, 1, 1, 0]
    x, y = [], []
    for _ in range(samples):
        choice: int = random.randint(0, 3)
        x.append(x_choice[choice])
        y.append(y_choice[choice])
    return np.array(x), np.array(y)

def generate_fizz_buzz_dataset(samples: int = 150) -> Tuple[np.ndarray, np.ndarray]:
    fizz_buzz_encode = lambda _: [0, 0, 0, 1] if _ % 15 == 0 \
                       else ([0, 0, 1, 0] if _ % 5 == 0
                       else ([0, 1, 0, 0] if _ % 3 == 0
                       else [1, 0, 0, 0]))
    binary_encode = lambda _: [_ >> i & 1 for i in range(16)]
    return np.array([binary_encode(_)[::-1] for _ in range(100, samples + 100)]), \
            np.array([fizz_buzz_encode(_) for _ in range(100, samples + 100)])

x0, y0 = spiral_data(samples=150, classes=3)
x1, y1 = vertical_data(samples=150, classes=3)
x2, y2 = make_moons(150, noise=0.035, random_state=20)
x3, y3 = make_circles(150, noise=0.02, random_state=20)
x4, y4 = generate_xor_dataset()
x5, y5 = generate_fizz_buzz_dataset()
x6, y6 = iris['data'], iris['target']
x7, y7 = diabetes['data'], diabetes['target']
x8, y8 = breast_cancer['data'], breast_cancer['target']
x9, y9 = boston['data'], boston['target']

print(f'x0.shape: {x0.shape}, y0.shape: {y0.shape}\n')
print(f'x0: {x0[:10]}\n')
print(f'y0: {y0[:10]}\n')

print(f'x1.shape: {x1.shape}, y1.shape: {y1.shape}\n')
print(f'x1: {x1[:10]}\n')
print(f'y1: {y1[:10]}\n')

print(f'x2.shape: {x2.shape}, y2.shape: {y2.shape}\n')
print(f'x2: {x2[:10]}\n')
print(f'y2: {y2[:10]}\n')

print(f'x3.shape: {x3.shape}, y3.shape: {y3.shape}\n')
print(f'x3: {x3[:10]}\n')
print(f'y3: {y3[:10]}\n')

print(f'x4.shape: {x4.shape}, y4.shape: {y4.shape}\n')
print(f'x4: {x4[:10]}\n')
print(f'y4: {y4[:10]}\n')

print(f'x5.shape: {x5.shape}, y5.shape: {y5.shape}\n')
print(f'x5: {x5[:10]}\n')
print(f'y5: {y5[:10]}\n')
print(f'y5 classes: {len(set(y5.reshape(-1).tolist()))}')

print(f'x6.shape: {x6.shape}, y6.shape: {y6.shape}\n')
print(f'x6: {x6[:10]}\n')
print(f'y6: {y6[:10]}\n')
print(f'y6 classes: {len(set(y6.reshape(-1).tolist()))}')

print(f'x7.shape: {x7.shape}, y7.shape: {y7.shape}\n')
print(f'x7: {x7[:10]}\n')
print(f'y7: {y7[:10]}\n')

print(f'x8.shape: {x8.shape}, y8.shape: {y8.shape}\n')
print(f'x8: {x8[:10]}\n')
print(f'y8: {y8[:10]}\n')

print(f'x9.shape: {x9.shape}, y9.shape: {y9.shape}\n')
print(f'x9: {x9[:10]}\n')
print(f'y9: {y9[:10]}\n')

