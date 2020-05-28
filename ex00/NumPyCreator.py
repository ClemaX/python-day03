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
        return np.array(itr)

    @staticmethod
    def from_shape(shape, value):
        return np.full(shape, value)

    @staticmethod
    def random(shape):
        return np.random.random_sample(shape)

    @staticmethod
    def identity(n):
        return np.identity(n)
