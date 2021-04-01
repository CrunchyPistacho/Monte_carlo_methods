import numpy as np
import matplotlib.pyplot as plt


class Pi_estimator:
    def __init__(self, throws, replications):
        self.throws = throws
        self.replications = replications

    def buffon_needle_pi(self):
        x = np.random.rand(self.throws)
        theta = np.random.rand(self.throws)
        theta = 0.5*np.pi*theta
        hits = x <= 0.5*np.sin(theta)
        hits = 1*hits
        pi = self.throws/sum(hits)
        return pi

    def hit_or_miss(self):
        x = np.random.rand(self.throws)
        y = np.random.rand(self.throws)
        hits = (x**2 + y**2) < 1
        pi = sum(4*hits) / self.throws
        return pi

    def multiple_buffon_needle_pi(self, model):
        pi = np.empty(self.replications)
        for i in range(0, self.replications):
            if model == 'buffon_needle':
                pi[i] = self.buffon_needle_pi()
            elif model == 'hit_or_miss':
                pi[i] = self.hit_or_miss()
        return pi


def plot_histogram(x):
    n, bins, patches = plt.hist(x=x, bins='auto',
                                alpha=0.7)
    plt.xlabel('Pi Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq %
             10 else maxfreq + 10)
    plt.show()


if __name__ == "__main__":
    pi_estimation = Pi_estimator(10000, 1000)
    multiple_pi = pi_estimation.multiple_buffon_needle_pi(model = 'hit_or_miss')
    print(multiple_pi)
    plot_histogram(multiple_pi)
