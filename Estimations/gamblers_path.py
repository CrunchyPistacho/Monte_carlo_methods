import numpy as np
import matplotlib.pyplot as plt


class Gambler_path:
    def __init__(self, gambler_starting_money, casino_starting_money, bet_amout, max_iterations, replications):
        self.gambler_starting_money = gambler_starting_money
        self.casino_starting_money = casino_starting_money
        self.bet_amout = bet_amout
        self.replications = replications
        self.max_iterations = max_iterations

    def play(self):
        R = np.zeros(self.max_iterations)
        R[:] = np.NaN
        i = 0
        R[i] = self.gambler_starting_money
        while(R[i] > 0 and R[i] < (self.gambler_starting_money + self.casino_starting_money) and i < self.max_iterations-1):
            i = i+1
            W = np.random.rand() < 0.5
            W = 2 * self.bet_amout * W - self.bet_amout
            R[i] = R[i-1]+W
            if R[i] == (self.gambler_starting_money + self.casino_starting_money):
                R[i:] = self.gambler_starting_money + \
                    self.casino_starting_money
        end = i
        return R, end

    def multiple_plays(self):
        R = np.empty((self.max_iterations, self.replications))
        end = np.empty(self.replications)
        for i in range(0, self.replications):
            R[:, i], end[i] = self.play()
        return R, end


def plot_games(x):
    plt.plot(x)
    plt.xlabel('number of plays')
    plt.ylabel('Player Money')
    plt.title('Players game evolution')
    plt.show()


def plot_histogram(x):
    n, bins, patches = plt.hist(x=x, bins='auto',
                                alpha=0.7)
    plt.xlabel('number of plays')
    plt.ylabel('Frequency')
    plt.title('Histogram for number of plays before bankrupt')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq %
             10 else maxfreq + 10)
    plt.show()


if __name__ == "__main__":
    casino = Gambler_path(50, 2000, 1, 100000, 100)
    results, end = casino.multiple_plays()
    plot_games(results)
    plot_histogram(end)
