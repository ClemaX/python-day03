from matplotlib import pyplot as plt


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
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    img = ImageProcessor.load('./test.png')
    ImageProcessor.display(img)
