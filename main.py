import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.integrate import cumtrapz
from scipy.interpolate import interpnd_info, interp1d

from importer import import_dream_data
from simulations.barter import simulate_barter

# Constants
ender_pearl_drop_chance = 0.05
num_runs = 1000
ingots = 262

# Data
dream_barter_data = import_dream_data("./data/dream_pearls.csv")
barter_simulation = simulate_barter(num_runs, ingots, ender_pearl_drop_chance)

# Plots
def plot_runs():
    for run in barter_simulation:
        plt.plot(run, 'b', lw=0.5)
    plt.plot(dream_barter_data, 'r', lw=0.7)
    plt.xlabel('Cumulative Ingots Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()


def plot_best_run():
    best_run = barter_simulation[0]

    for run in barter_simulation:
        if run[-1] > best_run[-1]:
            best_run = run

    plt.plot(best_run, 'b', lw=0.5)
    plt.plot(dream_barter_data, 'r', lw=0.7)
    plt.xlabel('Cumulative Ingots Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()


def get_quantiles(runs, low, high):
    lows = np.zeros(runs.shape[1])
    highs = np.zeros(runs.shape[1])
    for i in range(runs.shape[1]):
        lows[i] = np.quantile(runs[:, i], low)
        highs[i] = np.quantile(runs[:, i], high)
    return lows, highs


def plot_quantiles():
    # 1 sigma bounds
    low_1sigma, high_1sigma = get_quantiles(
        barter_simulation, 0.15865, 0.84135)
    plt.fill_between(np.arange(ingots), low_1sigma,
                     high_1sigma, color='b', alpha=0.5)

    # 2 sigma bounds
    low_2sigma, high_2sigma = get_quantiles(
        barter_simulation, 0.02275, 0.97725)
    plt.fill_between(np.arange(ingots), low_2sigma,
                     high_2sigma, color='b', alpha=0.3)

    # 3 sigma bounds
    low_3sigma, high_3sigma = get_quantiles(
        barter_simulation, 0.00135, 0.99865)
    plt.fill_between(np.arange(ingots), low_3sigma,
                     high_3sigma, color='b', alpha=0.1)

    plt.plot(dream_barter_data, 'r', lw=0.7)
    plt.xlabel('Cumulative Ingots Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()


"""
prop: probability of a single success
k = numer of successes (between 0 and n)
n = number of runs
"""


def likelihood_binomial(prob, n, k):
    return st.binom.pmf(k, n, prob)


def plot_drop_probability():
    N = 1000
    likelihood_highres = np.zeros(N)
    prob_vals_highres = np.linspace(0.05, 0.3, N)
    for i in range(N):
        likelihood_highres[i] = likelihood_binomial(prob_vals_highres[i], 262, dream_barter_data[-1])
    plt.plot(prob_vals_highres, likelihood_highres)
    plt.xlabel('Ender Pearl Drop Probability')
    plt.show()

def plot_likely_drop_probability():
    N = 1000
    likelihood = np.zeros(N)
    likelihood_highres = np.zeros(N)

    prob_vals = np.linspace(0.0,1.0,N)
    prob_vals_highres = np.linspace(0.05, 0.3, N)

    for i in range(N):
        likelihood[i] = likelihood_binomial(prob_vals[i],262,dream_barter_data[-1])
        likelihood_highres[i] = likelihood_binomial(prob_vals_highres[i], 262, dream_barter_data[-1])

    cumulative = cumtrapz(likelihood,prob_vals,initial=0.0)/np.trapz(likelihood,prob_vals)

    inverse = interp1d(cumulative,prob_vals)
    samples = inverse(np.random.rand(1000))

    plt.plot(prob_vals[:500],likelihood[:500])
    plt.xlabel('Ender Drop Probability')
    plt.axvline(prob_vals_highres[np.argmax(likelihood_highres)],c='k',lw=1.5,ls='--',label='%.3f' % prob_vals_highres[np.argmax(likelihood_highres)])
    plt.axvline(np.quantile(samples,0.02275),c='r',lw=1.5,ls='--',label='95% Credible Region')
    plt.axvline(np.quantile(samples,0.97725),c='r',lw=1.5,ls='--')
    plt.axvline(0.05,label='Minecraft Drop Probability',c='g',lw=1.5,ls='--')
    plt.legend()
    plt.ylabel('Likelihood')
    plt.show()

# Plotting all runs and dream's run
plot_runs()

# Plotting the best of the runs and dream's run
plot_best_run()

# Plotting the quantiles and dream's run
plot_quantiles()

# Plotting the probability of the tweaked Ender Pearl drop rate
plot_drop_probability()

# Plotting the most likely tweaked Ender Pearl drop rate
plot_likely_drop_probability()