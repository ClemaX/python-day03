from matplotlib import pyplot as plt


class ImageProcessor:
    @staticmethod
    def load(path):
        """Load a PNG image into a numpy array"""
        return plt.imread(path)

    @staticmethod
    def display(array):
        """Display an image from a numpy array"""
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    img = ImageProcessor.load('./test.png')
    ImageProcessor.display(img)
    while True:
        pass
