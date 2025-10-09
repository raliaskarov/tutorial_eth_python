from math import *

class Coordinate:
  def __init__(self, deg_latitude, deg_longitude):
    self.latitude = radians(deg_latitude)
    self.longitude = radians(deg_longitude)

  def __str__(self):
    return str(self.latitude) + ", " + str(self.longitude)

  def distance(self, other):
    dlat = self.latitude - other.latitude
    dlon = self.longitude - other.longitude
    hav = sin(dlat / 2) ** 2 + cos(self.latitude) * cos(other.latitude) * sin(dlon / 2) ** 2
    return 6373 * 2 * atan2(sqrt(hav), sqrt(1 - hav))
