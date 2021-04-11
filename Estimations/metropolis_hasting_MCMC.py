import numpy as np
import matplotlib.pyplot as plt
import math


class MCMC_metropolis:
    def __init__(self, N, mu=0, sigma=1):
        self.mu = mu
        self.sigma = sigma
        self.N = N

    def distribution(self, x):
        return ((1/(math.sqrt(2*math.pi*self.sigma**2)))*(math.e**(-((x-self.mu)**2)/(2*self.sigma**2))))

    def metropolis(self):
        r = np.zeros(1)
        p = self.distribution(r[0])
        pts = []

        for i in range(self.N):
            rn = r + np.random.uniform(-1, 1)
            pn = self.distribution(rn[0])
            if pn >= p:
                p = pn
                r = rn
            else:
                u = np.random.rand()
                if u < pn/p:
                    p = pn
                    r = rn
            pts.append(r)

        pts = np.array(pts)
        return pts

def plot_simulation(array, bins):
    fig, axs = plt.subplots(1,2, gridspec_kw={'width_ratios': [1, 5], 'wspace': 0.1})
    axs[0].hist(array, bins=bins, orientation='horizontal')
    axs[1].plot(array)
    plt.show()

if __name__ == "__main__":
    metro = MCMC_metropolis(N=100000)
    simulation = metro.metropolis()
    plot_simulation(simulation, bins = 100)
