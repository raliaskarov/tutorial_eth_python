
class Measurement:
    def __init__(self, date, time, coordinate, magnitude):
        self.date = date
        self.time = time
        self.coordinate = coordinate
        self.magnitude = magnitude

    def __str__(self):
        return(f"Earthquake of magnitude {self.magnitude}, "
            f"measured on {self.date} at {self.time} "
            f"position {self.coordinate}")
        

def read_measurements_csv(filename):
    """
    Reads csv with earthquake data
    Returns: dict [int, Measurement]
    """
    measurements = {}
    with open(filename) as f:
        reader = csv.DictReader(
            f,
            delimiter=';',
            quotechar='"',
            skipinitialspace=True
            )
        for row in reader:
            coord = Coordinate(float(row["lat"]),
                        float(row["lon"]))
            dt = row["date/time"]/split(" ")
            mgdt = float(row["M1"])
            m = Measurement(dt[0], dt[1], coord, mgdt)
            key = int(float(row["datanr"]))
            measurements[key] = m
        return measurements


