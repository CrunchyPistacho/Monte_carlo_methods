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

    def multiple_buffon_needle_pi(self):
        pi = np.empty(self.replications)
        for i in range(0, self.replications):
            pi[i] = self.buffon_needle_pi()
        return pi

def plot_histogram(x):
    n, bins, patches = plt.hist(x=x, bins='auto',
                                alpha=0.7, rwidth=0.85)
    plt.xlabel('Pi Value')
    plt.ylabel('Frequency')
    plt.title('Buffon Needle Histogram')
    plt.text(23, 45, r'$\mu=15, b=3$')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq %
                10 else maxfreq + 10)
    plt.show()


if __name__ == "__main__":
    pi_estimation = Pi_estimator(10000, 1000)
    pi = pi_estimation.buffon_needle_pi()
    multiple_pi = pi_estimation.multiple_buffon_needle_pi()
    plot_histogram(multiple_pi)
