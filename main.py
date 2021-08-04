from datasets.diabetes import Diabetes
from datasets.breastcancer import BreastCancer
from datasets.boston import Boston
from datasets.iris import Iris
from datasets.circles import Circles
from datasets.moons import Moons
from datasets.vertical import Vertical
from datasets.spiral import Spiral
from datasets.binaryfizzbuzz import BinaryFizzBuzz
from datasets.fizzbuzz import FizzBuzz
from datasets.binary import Binary
from datasets.xor import XOR

def main() -> None:
    xor = XOR()
    print(xor)

    binary = Binary()
    print(binary)

    fizzBuzz = FizzBuzz()
    print(fizzBuzz)

    binaryFizzBuzz = BinaryFizzBuzz()
    print(binaryFizzBuzz)

    spiral = Spiral()
    print(spiral)

    vertical = Vertical()
    print(vertical)

    moons = Moons()
    print(moons)

    circles = Circles()
    print(circles)

    iris = Iris()
    print(iris)

    boston = Boston()
    print(boston)

    breastCancer = BreastCancer()
    print(breastCancer)

    diabetes = Diabetes()
    print(diabetes)

if __name__ == "__main__":
    main()
