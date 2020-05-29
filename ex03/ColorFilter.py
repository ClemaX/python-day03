from matplotlib import pyplot as plt
import numpy as np


class ImageProcessor:
    @staticmethod
    def load(path):
        """Load a PNG image into a numpy array"""
        img = plt.imread(path)
        dimensions = f"{img.shape[0]} x {img.shape[1]}"
        print(f"Loaded image at {path} of dimensions {dimensions}")
        return img

    @staticmethod
    def display(array):
        """Display an image from a numpy array"""
        plt.figure()
        plt.imshow(array)
        plt.show()


class ColorFilter:
    @staticmethod
    def invert(array):
        """
        Takes a numpy array of an image and
        returns an array with inverted color
        """

        f = [1, 1, 1]

        result = np.array(array)

        for row in range(result.shape[0]):
            for pixel in range(result.shape[1]):
                result[row][pixel] = f - result[row][pixel]

        return result

    @staticmethod
    def to_blue(array):
        """
        Takes a numpy array of an image and
        returns an array with a blue filter
        """
        result = np.zeros(array.shape)

        for row in range(result.shape[0]):
            for pixel in range(result.shape[1]):
                result[row][pixel][2] = array[row][pixel][2]

        return result

    @staticmethod
    def to_green(array):
        """
        Takes a numpy array of an image and
        returns an array with a green filter
        """
        result = np.zeros(array.shape)

        for row in range(result.shape[0]):
            for pixel in range(result.shape[1]):
                result[row][pixel][1] = array[row][pixel][1]

        return result

    @staticmethod
    def to_red(array):
        """
        Takes a numpy array of an image and
        returns an array with a red filter
        """
        result = np.zeros(array.shape)

        for row in range(array.shape[0]):
            for pixel in range(array.shape[1]):
                result[row][pixel][0] = array[row][pixel][0]

        return result

    @staticmethod
    def celluloid(array):
        """
        Takes a numpy array of an image and
        returns an array with a blue filter
        """
        shades = np.linspace(1, 0, num=4)

        result = np.zeros(array.shape)

        for row in range(array.shape[0]):
            for pixel in range(array.shape[1]):
                for color in range(array.shape[2]):
                    for shade in shades:
                        if array[row][pixel][color] >= shade:
                            result[row][pixel][color] = shade
                            break

        return result

    @staticmethod
    def to_grayscale(array, filter):
        """
        Takes a numpy array of an image and
        returns an array with a grayscale filter

        filter can be 'mean'/'m' or 'weighted'/'w'
        returns None for invalid filter
        """
        if filter == 'mean' or filter == 'm':
            result = np.zeros(array.shape)
            for row in range(array.shape[0]):
                for pixel in range(array.shape[1]):
                    color = array[row][pixel]
                    mean = (color[0] + color[1] + color[2]) / 3
                    result[row][pixel] = mean
            return result
        elif filter == 'weighted' or filter == 'w':
            result = np.zeros(array.shape)
            weight = [0.299, 0.587, 0.114]
            for row in range(result.shape[0]):
                for pixel in range(array.shape[1]):
                    color = array[row][pixel] * weight
                    weighted = color[0] + color[1] + color[2]
                    result[row][pixel] = weighted
            return result
        else:
            return None


imp = ImageProcessor()
arr = imp.load('test.png')

grm = ColorFilter.to_grayscale(arr, 'm')
imp.display(grm)

grm = ColorFilter.to_grayscale(arr, 'w')
imp.display(grm)

inv = ColorFilter.invert(arr)
imp.display(inv)

blu = ColorFilter.to_blue(arr)
imp.display(blu)

gre = ColorFilter.to_green(arr)
imp.display(gre)

red = ColorFilter.to_red(arr)
imp.display(red)

cel = ColorFilter.celluloid(arr)
imp.display(cel)
