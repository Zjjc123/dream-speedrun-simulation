import random
import numpy as np

def simulate_barter(num_runs, ingots, ender_eye_drop_chance):
    runs = np.zeros((num_runs,ingots))
    for x in range(num_runs):
        for y in range(ingots):
            success = 0
            if (random.random() < ender_eye_drop_chance):
                success = 1
            if (y >= 1):
                runs[x][y] = runs[x][y-1] + success
            else:
                runs[x][y] = success
    return runs
    