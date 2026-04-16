# Hospital Bed Occupancy Forecasting (Monte Carlo Simulation)

## Overview

This project models and predicts hospital bed occupancy using probabilistic simulation. It uses historical admission and discharge data to estimate future occupancy trends, identify potential overflow situations, and support capacity planning decisions.

The system is implemented in two forms:

* **CLI (Command-Line Tool):** Runs simulations and displays graphs locally
* **Web Application:** Allows users to upload data and visualize results interactively

---

## Problem

Hospitals have limited bed capacity. Due to uncertainty in patient arrivals and discharges, it is difficult to predict whether demand will exceed available resources.

This project answers:

* How will occupancy evolve over time?
* What is the risk of exceeding capacity?
* When are critical overload periods likely?

---

## Approach

### Data

Input is a CSV file with daily records:

```csv
admissions,discharges
12,8
15,10
...
```

### Simulation Logic

Occupancy is updated daily as:

[
\text{Occupancy} = \text{Previous Occupancy} + \text{Admissions} - \text{Discharges}
]

### Monte Carlo Concept

Instead of running the model once, the simulation can:

* Randomly sample from historical data
* Run multiple iterations
* Generate a distribution of possible outcomes

This helps estimate probabilities rather than a single deterministic result.

---

## Outputs

### Metrics

* Average Occupancy
* Peak (Worst Case) Occupancy
* Overflow Probability (Occupancy > Capacity)
* Total Overflow (excess patients)

### Visualizations

1. **Occupancy vs Time**

   * Shows daily bed usage
   * Includes capacity line (150 beds)

2. **Overflow vs Time**

   * Shows number of patients exceeding capacity
   * Highlights critical days

---

## Project Structure

```
project/
│
├── cli.py              # Run simulation + plots
├── app.py              # Flask web application
│
├── data/
│   └── sample.csv      # Input dataset
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/             # Generated plots
```

---

## How to Run

### 1. CLI Simulation

Run from project folder:

```bash
python cli.py
```

Outputs:

* Printed statistics
* Graphs (occupancy and overflow)

---

### 2. Web Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

Upload a CSV file to view results.

---

## Requirements

Install dependencies:

```bash
pip install pandas matplotlib flask
```

---

## Applications

* Hospital capacity planning
* Resource allocation
* Risk assessment under uncertainty
* Operational decision support

---

## Limitations

* Assumes historical data reflects future trends
* Does not model seasonality or external events
* Simplifies patient flow dynamics

---

## Future Improvements

* Integrate time-series forecasting models
* Add real-time data support
* Extend to multi-hospital systems
* Improve UI and analytics

---

## Summary

This project demonstrates how probabilistic simulation can be used to model uncertain real-world systems. By combining simulation with visualization, it provides a practical tool for analyzing hospital capacity and planning for demand variability.
