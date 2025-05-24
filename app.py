from flask import Flask, render_template, request, redirect
from utils import load_data, save_data, haversine

app = Flask(__name__)

@app.route("/")
def home():
    data = load_data()
    summary = {}
    for emp_id, *_ in data:
        summary[emp_id] = summary.get(emp_id, 0) + 1
    return render_template("home.html", summary=summary)

@app.route("/add", methods=["GET", "POST"])
def add_checkin():
    if request.method == "POST":
        emp_id = request.form["emp_id"]
        time_str = request.form["time_str"]
        lat = float(request.form["lat"])
        lon = float(request.form["lon"])
        data = load_data()
        if not any(eid == emp_id and ts.split()[0] == time_str.split()[0] for eid, ts, _ in data):
            data.append([emp_id, time_str, [lat, lon]])
            save_data(data)
        return redirect("/")
    return render_template("add.html")

@app.route("/all")
def all_checkins():
    return render_template("all.html", data=load_data())

@app.route("/employee/<emp_id>")
def employee_view(emp_id):
    data = [rec for rec in load_data() if rec[0] == emp_id]
    return render_template("employee.html", emp_id=emp_id, records=data)

@app.route("/nearby", methods=["GET", "POST"])
def nearby():
    results = []
    if request.method == "POST":
        lat = float(request.form["lat"])
        lon = float(request.form["lon"])
        radius = float(request.form["radius"])
        for emp_id, time_str, loc in load_data():
            dist = haversine(lat, lon, loc[0], loc[1])
            if dist <= radius:
                results.append((emp_id, time_str, loc, round(dist, 2)))
    return render_template("nearby.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)