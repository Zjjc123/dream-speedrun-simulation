import random

def simulate_barter(num_runs, ingots, ender_eye_drop_chance, best_run = False):
    runs = [[]]
    best_total = 0
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
        if (best_run):
            if (run[-1] > best_total): 
                runs[0] = run
                best_total = run[-1]
        else:
            runs.append(run)
    return runs