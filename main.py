import matplotlib.pyplot as plt
import numpy as np

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
        plt.plot(run, 'b', lw = 0.5)
    plt.plot(dream_barter_data, 'r', lw = 0.7)
    plt.xlabel('Cumulative Ingots Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()

def plot_best_run():
    best_run = barter_simulation[0]

    for run in barter_simulation:  
        if run[-1] > best_run[-1]:
            best_run = run

    plt.plot(best_run, 'b', lw = 0.5)
    plt.plot(dream_barter_data, 'r', lw = 0.7)
    plt.xlabel('Cumulative Ingots Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()

def get_quantiles(runs, low, high):
    lows = np.zeros(runs.shape[1])
    highs = np.zeros(runs.shape[1])
    for i in range(runs.shape[1]):
        lows[i] = np.quantile(runs[:,i],low)
        highs[i] = np.quantile(runs[:,i],high)
    return lows, highs

def plot_quantiles():
    # 1 sigma bounds
    low_1sigma, high_1sigma = get_quantiles(barter_simulation,0.15865,0.84135)
    plt.fill_between(np.arange(ingots),low_1sigma,high_1sigma,color='b',alpha=0.5)

    # 2 sigma bounds
    low_2sigma, high_2sigma = get_quantiles(barter_simulation,0.02275,0.97725)
    plt.fill_between(np.arange(ingots),low_2sigma,high_2sigma,color='b',alpha=0.3)

    # 3 sigma bounds
    low_3sigma, high_3sigma = get_quantiles(barter_simulation,0.00135,0.99865)
    plt.fill_between(np.arange(ingots),low_3sigma,high_3sigma,color='b',alpha=0.1)

    plt.plot(dream_barter_data, 'r', lw = 0.7)
    plt.xlabel('Cumulative Ingots Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()

# Plotting all runs and dream's run
plot_runs()

# Plotting the best of the runs and dream's run
plot_best_run()

# Plotting the quantiles and dream's run
plot_quantiles()