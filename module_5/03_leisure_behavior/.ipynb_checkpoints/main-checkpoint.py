import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas
import os
import shapely
from shapely import box, LineString, normalize, Polygon, Point

tic = time.time()

 #############################################
##    TASK 0 --> DATA IMPORT & DESCRIPTION   ##
 #############################################


 #######################################
##      TASK 1 --> SIMPLE FILTERING    ##
 #######################################



 ###################################################
##    TASK 3 --> TIME-DEPENDENCY OF BENCH USAGE    ##
 ###################################################


print("Calculate usage over time...\n")
print("List of Bench IDs:")
bench = "0080E115003BE631"

hours = np.arange(0,24, 24/46)

## Select the correct bench data

dates = ["2022-08-11","2022-08-13","2022-08-14", "2022-08-23"]
"""
plt.figure(figsize=(15,9))
"""
for date in dates:
  pass

"""
plt.xlabel('Time [h]')
plt.xticks(np.arange(0,25,1))
plt.ylabel('Occupancy [%]')
plt.legend()
plt.title("Usage of bench id "+str(bench), fontsize=16)
plt.grid(True)
plt.savefig('./cx_out/usage_over_time.png')
"""
##################################
##      TASK 4 --> PLOTTING     ##
##################################



### TIME CHECK
toc = time.time()
print(str(toc-tic), "s elapsed")
