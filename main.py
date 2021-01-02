import matplotlib.pyplot as plt

from importer import import_dream_data
from simulations.barter import simulate_barter

blaze_drop_chance = 0.5
ender_eye_drop_chance = 0.05

num_runs = 1000000
ingots = 262

dream_barter_data = import_dream_data("./data/dream_pearls.csv")
barter_simulation = simulate_barter(num_runs, ingots, ender_eye_drop_chance, best_run = True)

print("Data Collected!")

for run in barter_simulation:  
    plt.plot(run, 'b', lw = 0.5)

plt.plot(dream_barter_data, 'r', lw = 0.7)
plt.xlabel('Cumulative Ingots Bartered')
plt.ylabel('Ender Pearls')
plt.show()
