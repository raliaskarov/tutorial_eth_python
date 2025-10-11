from coordinate import *
from measurement import *
import csv
import matplotlib.pyplot as plt

def read_measurements_csv(filename):
  measurements = {}
  with open(filename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"', skipinitialspace=True)
    for row in reader:
      tmp_coord = Coordinate(float(row["lat"]), float(row["lon"]))
      tmp_date_time = row["date/time"].split(" ")
      magnitude = float(row["Ml"])
      tmp_meas = Measurement(tmp_date_time[0], tmp_date_time[1], tmp_coord, magnitude)
      key = int(float(row["datanr"]))
      measurements[key] = tmp_meas
  return measurements


# Output of the distance from Zurich to Brisbane
zurich = Coordinate(47.36667, 8.55)
brisbane = Coordinate(-27.46794, 153.02809)
print(zurich)
print(int(zurich.distance(brisbane)), "km")

# Output for the earthquake on 22.12.2019 at 13:33

# User interface for querying earthquake data
earthquake_data = read_measurements_csv("erdbeben_ch.csv")
print(earthquake_data[30275902])
print()
print("Coordinate: ", earthquake_data[30275902].coordinate)
print()

# demo access series

dates = [m.date for m in earthquake_data.values()]
magnitudes = [m.magnitude for m in earthquake_data.values()]
print(f"\nSample dates series: {dates[:10]}")
print(f"\nSame magnitudes series: {magnitudes[:10]}")

fig, ax = plt.subplots(figsize = (6, 4))

x = list(range(len(dates)))
bars = ax.bar(x = x,
              height = magnitudes,
             color="blue")

ax.set(title=f"Earthquakes",
       xlabel = "Date",
       ylabel = "Magnitude",
      )


step = len(dates) // 20 #20 labels on chart

print(f"Showing labels every {step} record of total dataset of {len(dates)} records")
tick_positions = list(range(0, len(dates), step))
tick_labels = [dates[i] for i in tick_positions]
ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels, rotation=90, fontsize=6)

fig.tight_layout()
chart_filename = "eathquakes.png"
plt.savefig(chart_filename)
print(f"Saved chart to {chart_filename}")
plt.show()