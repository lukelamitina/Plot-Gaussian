import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plotGaussian(mu, sigma):
    x = np.linspace(-3 * sigma + mu, 3 * sigma + mu, 100)
    plt.plot(x, norm.pdf(x, mu, sigma))
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.show()




