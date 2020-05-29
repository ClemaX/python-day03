import random
import numpy
import matplotlib.pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
        for i in range(ncentroid):
            self.centroids.append(None)

    def nearest_centroid(self, X):
        min_dist = float("inf")
        for i, c in enumerate(self.centroids):
            dist = numpy.linalg.norm(X - c)
            if dist < min_dist:
                min_dist = dist
                nearest = i
        return nearest

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids,
        random pick ncentroids from the dataset.
        Args:
          X: has to be a numpy.ndarray, a matrice of dimension m * n.
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """
        for iteration in range(self.max_iter):
            old_centroids = self.centroids.copy()

            clusters = []

            for i in range(self.ncentroid):
                clusters.append([])
                rand = random.randint(0, len(X) - 1)
                self.centroids[i] = X[rand]
                # ax.scatter(*X[rand], marker='^', color='red')

            for x in X:
                min_dist = float('inf')
                nearest = self.nearest_centroid(x)
                clusters[nearest].append(x)
                # ax.scatter(*x, color=color)

            for i in range(self.ncentroid):
                self.centroids[i] = numpy.mean(numpy.array(clusters[i]),
                                               axis=0)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('Height')
        ax.set_ylabel('Weight')
        ax.set_zlabel('Bone Density')
        colors = ('b', 'g', 'r', 'c', 'm')
        for i, c in enumerate(clusters):
            for x in c:
                ax.scatter(*x, color=colors[i])
            ax.scatter(*self.centroids[i], color='k')
        plt.show()

    def predict(self, X):
        """
        Predict from which cluster each datapoint belongs to.
        Args:
          X: has to be an numpy.ndarray, a matrice of dimension
        Returns:
          None.
        Raises:
          This function should not raise any Exception.
        """
        nearest = self.nearest_centroid(X)
        print('Nearest centroid: ', self.centroids[nearest])


if __name__ == "__main__":
    k = KmeansClustering()

    X = numpy.genfromtxt('solar_system_census.csv', delimiter=",",
                         skip_header=1, usecols=range(1, 4))
    k.fit(X)
    k.predict(X[0])
