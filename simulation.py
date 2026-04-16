# simulation.py

import pandas as pd
import numpy as np

def run_simulation(file, capacity, days=60, simulations=1000):
    df = pd.read_csv(file)

    arrivals = df['admissions'].values
    discharges = df['discharges'].values

    occupancy_results = []
    overflow_results = []

    for _ in range(simulations):
        beds = 0
        overflow = 0

        daily_occupancy = []

        for i in range(len(arrivals)):
            beds += arrivals[i]
            beds -= discharges[i]

            if beds > capacity:
                overflow += beds - capacity
                beds = capacity
            daily_occupancy.append(beds)

        occupancy_results.append(daily_occupancy)
        overflow_results.append(overflow)

    avg = np.mean(occupancy_results)
    worst = np.max(occupancy_results)
    prob = np.mean(np.array(overflow_results) > 0)
    total_overflow = np.sum(overflow_results)
    avg_daily_occupancy = np.mean(occupancy_results, axis=0)

    return avg, worst, prob, total_overflow, avg_daily_occupancy, overflow_results