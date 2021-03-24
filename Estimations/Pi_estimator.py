import numpy as np

class Pi_estimator:
    def __init__(self, throws):
        self.throws = throws
        self.pi = None
    
    def Buffon_needle_pi(self):
        x = np.random.rand(self.throws)
        theta = np.random.rand(self.throws)
        theta = 0.5*np.pi*theta
        hits = x <= 0.5*np.sin(theta)
        hits = 1*hits
        self.pi = self.throws/sum(hits)

if __name__ == "__main__":
    pi_estimation = Pi_estimator(10000)
    pi_estimation.Buffon_needle_pi()
    print(pi_estimation.pi)