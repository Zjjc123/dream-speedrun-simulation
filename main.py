import numpy as np
import matplotlib.pyplot as plt
import random

blaze_drop_chance = 0.5
ender_eye_drop_chance = 0.05

dream_barter = []

def simulate_barter(num_runs, ingots, ender_eye_drop_chance):
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
        plt.plot(run)
    plt.xlabel('Cumulative Ingot Bartered')
    plt.ylabel('Ender Pearls')
    plt.show()

num_runs = 1000
ingots = 262
simulate_barter(num_runs, ingots, ender_eye_drop_chance)
