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
            clusters = []

            for i in range(self.ncentroid):
                clusters.append([])
                rand = random.randint(0, len(X) - 1)
                self.centroids[i] = X[rand]

            for x in X:
                nearest = self.nearest_centroid(x)
                clusters[nearest].append(x)

            for i in range(self.ncentroid):
                self.centroids[i] = numpy.mean(numpy.array(clusters[i]),
                                               axis=0)
        self.clusters = clusters

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
    ncentroid = 4
    k = KmeansClustering(ncentroid=ncentroid)

    X = numpy.genfromtxt('solar_system_census.csv', delimiter=",",
                         skip_header=1, usecols=range(1, 4))
    k.fit(X)
    # Low weight: Venus
    # Tall: Martian
    # Tallest, lowest bone density: Citizens of the Belt
    martian = [185, 60, 0.8]
    k.predict(martian)
    print(f"HEIGHT         WEIGHT        BONE DENSITY")
    print(*k.centroids, sep='\n')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Bone Density')
    colors = numpy.linspace(0, 1.1, ncentroid)
    for i, c in enumerate(k.clusters):
        color = plt.cm.RdYlBu(colors[i])
        for x in c:
            ax.scatter(*x, color=color)
        ax.scatter(*k.centroids[i], s=200, color=color)
    plt.show()
