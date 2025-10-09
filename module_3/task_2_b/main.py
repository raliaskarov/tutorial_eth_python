from coordinate import *
from measurement import *
import csv


def read_measurements_csv(filename):
  measurements = {}
  with open(filename) as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"', skipinitialspace=True)
    for row in reader:
      tmp_coord = Coordinate(float(row["lat"]), float(row["lon"]))
      tmp_date_time = row["date/time"].split(" ")
      tmp_magnitude = float(row["Ml"])
      tmp_meas = Measurement(tmp_date_time[0], tmp_date_time[1], tmp_coord, tmp_magnitude)
      key = int(float(row["datanr"]))
      measurements[key] = tmp_meas
  return measurements


# Output of the distance from Zurich to Brisbane

# Output for the earthquake on 22.12.2019 at 13:33

# User interface for querying earthquake data
earthquake_data = read_measurements_csv("erdbeben_ch.csv")