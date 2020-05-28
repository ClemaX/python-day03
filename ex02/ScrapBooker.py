class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position):
        """
        Crops the array with the given dimensions,
        whose top left corner is given by position
        """

        if dimensions[0] >= array.shape[0]\
           or dimensions[1] >= array.shape[0]\
           or position[0] >= array.shape[0]\
           or position[1] >= array.shape[1]:
            return None
        end = position + dimensions
        return array[position[0]:end[0], position[1]:end[1]]

    @staticmethod
    def thin(array, n, axis):
        """
        Deletes every n-th pixel row along the specified axis

        Axis: 0 -> vertical, 1-> horizontal
        """
        return np.delete(array, [::n], axis)

    @staticmethod
    def juxtapose(array, n, axis):
        """
        Juxtaposes n copies of the array along the specified axis

        Axis: 0 -> vertical, 1-> horizontal
        """
        return np.repeat(a, n, axis)

    @staticmethod
    def mosaic(array, dimensions):
        """
        Makes a grid with multiple copies of the array

        The dimensions argument specifies the dimensions of the grid
        """
        return np.tile(array, dimensions)
