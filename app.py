# app.py

from flask import Flask, render_template, request
from simulation import run_simulation
import matplotlib.pyplot as plt
import io, base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    file = request.files['file']
    capacity = int(request.form['beds'])

    avg, worst, prob, overflow, avg_daily_occupancy, overflow_list = run_simulation(file, capacity)

    # ---- Occupancy Plot ----
    plt.figure()
    plt.figure()
    plt.plot(avg_daily_occupancy)
    plt.title("Daily Occupancy Trend")
    plt.xlabel("Days")
    plt.ylabel("Beds Occupied")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    occ_plot = base64.b64encode(buf.getvalue()).decode()
    plt.close()

    # ---- Overflow Plot ----
    plt.figure()
    plt.hist(overflow_list)
    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png')
    buf2.seek(0)
    over_plot = base64.b64encode(buf2.getvalue()).decode()
    plt.close()


    plt.axhline(y=capacity, linestyle='--')

    return render_template('result.html',
                           avg=avg,
                           worst=worst,
                           prob=prob,
                           overflow=overflow,
                           occ_plot=occ_plot,
                           over_plot=over_plot)

if __name__ == '__main__':
    app.run(debug=True)