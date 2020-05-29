import numpy as np


class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position):
        """
        Crops the 2D-array with the given dimensions,
        whose top left corner is given by position
        """
        if dimensions[0] >= array.shape[0]\
           or dimensions[1] >= array.shape[0]\
           or position[0] >= array.shape[0]\
           or position[1] >= array.shape[1]:
            return None

        end = (position[0] + dimensions[0], position[1] + dimensions[1])
        return array[position[0]:end[0], position[1]:end[1]]

    @staticmethod
    def thin(array, n, axis):
        """
        Deletes every n-th pixel row of the 2D-array
        along the specified axis

        Axis: 0 -> vertical, 1-> horizontal
        """
        if n == 0:
            return array

        return np.delete(array, slice(n - 1, None, n),
                         axis=0 if axis == 1 else 1)

    @staticmethod
    def juxtapose(array, n, axis):
        """
        Juxtaposes n copies of the 2D-array along the specified axis

        Axis: 0 -> vertical, 1-> horizontal
        """
        return np.concatenate([array] * n, axis=axis)

    @staticmethod
    def mosaic(array, dimensions):
        """
        Makes a grid with multiple copies of the 2D-array

        The dimensions argument specifies the dimensions of the grid
        """
        return np.tile(array, dimensions)


if __name__ == "__main__":
    a = np.array([list("ABCDEFGHIJQL") for i in range(10)])
    print(a)
    b = ScrapBooker.crop(a, (2, 3), (0, 1))
    print(b)
    c = ScrapBooker.thin(a, 3, 0)
    print(c)
    d = ScrapBooker.juxtapose(b, 2, 1)
    print(d)
    e = ScrapBooker.mosaic(b, (2, 3))
    print(e)
