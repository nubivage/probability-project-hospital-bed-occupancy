# probability-project-hospital-bed-occupancy
---

# 📊 Hospital Bed Occupancy Simulation & Forecasting

A simulation-driven decision support system for analyzing hospital bed utilization under uncertainty. This project combines **stochastic modeling**, **time-series aggregation**, and a **web interface** to evaluate occupancy dynamics and overflow risk.

---

## 🔍 Overview

Efficient hospital capacity planning requires understanding variability in patient flow. This project models:

* Daily **admissions** (inflow)
* Daily **discharges** (outflow)
* Finite **bed capacity constraints**

Using repeated simulations, the system estimates:

* Expected occupancy levels
* Worst-case utilization
* Probability and magnitude of overflow
* Temporal evolution of bed usage (time-series)

---

## 🧠 Core Methodology

### 1. Discrete-Time System Model

We model hospital occupancy as a discrete-time process:

[
O_t = \min\left(C,; O_{t-1} + A_t - D_t \right)
]

Where:

* (O_t): occupancy at time (t)
* (A_t): admissions
* (D_t): discharges
* (C): bed capacity

Overflow occurs when:
[
O_{t-1} + A_t - D_t > C
]

---

### 2. Monte Carlo Simulation

To capture variability and uncertainty:

* The system is simulated over multiple runs (typically (N = 1000))
* Each run produces a full occupancy trajectory
* Aggregation yields statistical estimates

Outputs:

* Mean occupancy
* Maximum occupancy (worst-case)
* Overflow probability:
  [
  P(\text{overflow}) = \frac{\text{# runs with overflow}}{N}
  ]
* Total overflow volume

---

### 3. Time-Series Aggregation

Instead of static distributions, the model computes:

[
\bar{O}*t = \frac{1}{N} \sum*{i=1}^{N} O_t^{(i)}
]

This produces a **time-series curve** representing expected occupancy over time.

---

## ⚙️ Project Structure

```plaintext
hospital_project/
│
├── app.py              # Flask web application (UI + visualization)
├── simulation.py       # Core stochastic simulation engine
├── cli.py              # Command-line interface for quick execution
│
├── templates/          # HTML templates
│   ├── index.html
│   └── result.html
│
├── static/             # Optional CSS / assets
│
└── data/
    └── sample.csv      # Input dataset
```

---

## 📁 Input Data Format

CSV file with two columns:

```csv
admissions,discharges
12,8
15,10
...
```

Constraints:

* One row = one day
* Columns must be named exactly:

  * `admissions`
  * `discharges`

---

## 🚀 Usage

### 1. Run Web Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

Features:

* Upload dataset
* Specify bed capacity
* View:

  * Key metrics
  * Time-series occupancy plot

---

### 2. Run Simulation via CLI

```bash
python cli.py
```

Outputs:

* Average occupancy
* Worst-case occupancy
* Overflow probability
* Total overflow

Optional: enable plotting for quick visualization.

---

## 📈 Outputs

### Quantitative Metrics

* **Average Occupancy**
* **Worst-case Occupancy**
* **Overflow Probability**
* **Total Overflow Volume**

### Visualization

* **Time-Series Occupancy Curve**

  * Highlights demand trends
  * Reveals capacity stress periods

---

## 🧪 Assumptions & Limitations

* Deterministic input sequences (no stochastic arrival modeling yet)
* No patient-level heterogeneity (length-of-stay not explicitly modeled)
* Capacity is static
* No prioritization or triage logic

---

## 🔧 Potential Extensions

This framework is intentionally modular. Future improvements include:

### 1. Statistical Modeling

* Poisson / Non-homogeneous Poisson arrivals
* Survival analysis for discharge modeling
* Markov or semi-Markov occupancy transitions

### 2. Forecasting

* Time-series models (ARIMA, Prophet)
* Seasonal trend decomposition
* Real-time adaptive prediction

### 3. Decision Optimization

* Capacity planning under constraints
* Cost vs overflow trade-off analysis
* Scenario-based simulation (surge events)

### 4. System Design

* REST API integration
* Dashboard visualization
* Multi-hospital network modeling

---

## 🧩 Design Philosophy

The system follows **separation of concerns**:

* `simulation.py` → computational core
* `app.py` → presentation layer
* `cli.py` → lightweight interface

This enables:

* Reusability
* Testability
* Scalability

---

## 📌 Summary

This project demonstrates how **probabilistic simulation + time-series analysis** can transform raw hospital flow data into actionable insights for capacity planning.

It bridges:

* Statistical modeling
* Systems simulation
* Practical decision support

---

If you want, I can next:

* make this README look like a **top-tier GitHub project (badges, visuals, diagrams)**
* or add a **methodology section with citations like a research paper**
