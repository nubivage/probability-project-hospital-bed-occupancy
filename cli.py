# cli.py

from simulation import run_simulation

file = "data/sample.csv"
capacity = 100

avg, worst, prob, overflow, occ, over = run_simulation(file, capacity)

print("Average Occupancy:", avg)
print("Worst Case:", worst)
print("Overflow Probability:", prob)
print("Total Overflow:", overflow)
