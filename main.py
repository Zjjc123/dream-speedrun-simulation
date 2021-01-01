import numpy as np
import matplotlib.pyplot as plt
import random
import csv

blaze_drop_chance = 0.5
ender_eye_drop_chance = 0.05

dream_barter = []

def simulate_barter(num_runs, ingots, ender_eye_drop_chance, comparison = None):
    runs = []
    for x in range(num_runs):
        run = [0] * ingots
        for y in range(ingots):
            success = 0
            if (random.random() < ender_eye_drop_chance):
                success = 1
            if (y >= 1):
                run[y] = run[y - 1] + success
            else:
                run[y] = success
        plt.plot(run, 'b', lw = 0.5)

    if (comparison is not None):
        plt.plot(comparison, 'r', lw = 0.7)

    plt.xlabel('Cumulative Ingots Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()

def import_dream_data(path):
    data = []
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        previous = 0
        for row in reader:
            for trades in range(int(row[0])):
                data.append(int(row[1]) + previous)
            previous = data[-1]
    return data

num_runs = 1000
ingots = 262

dream_barter_data = import_dream_data("./data/dream_pearls.csv")
simulate_barter(num_runs, ingots, ender_eye_drop_chance, dream_barter_data)
