import numpy as np


class NumPyCreator:
    @staticmethod
    def from_list(lst):
        return np.array(lst)

    @staticmethod
    def from_tuple(tpl):
        return np.array(tpl)

    @staticmethod
    def from_iterable(itr):
        return np.fromiter(itr, dtype=None)

    @staticmethod
    def from_shape(shape, value):
        return np.full(shape, value)

    @staticmethod
    def random(shape):
        return np.random.random_sample(shape)

    @staticmethod
    def identity(n):
        return np.identity(n)


if __name__ == "__main__":
    c = NumPyCreator()
    print('list:     ', c.from_list([1, 2, 3]))
    print('tuple:    ', c.from_tuple((1, 2, 3)))
    print('iterable: ', c.from_iterable(iter([1, 2, 3])))
    print('shape:    ', c.from_shape((10, 2), 10))
    print('random:   ', c.random((4)))
    print('identity: ', c.identity(2))
