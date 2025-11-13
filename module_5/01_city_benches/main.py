import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas
import shapely
from shapely import box, LineString, normalize, Polygon, Point

## PART A: Initialize and analyse data
df = geopandas.read_file('./db_data/data.gpkg')
print(df)
print(df.head())
print(df.info())
cols_print_unique = ['sitzbankmodelle']
print("\n ===== UNIQUE VALUES: =====")
for c in cols_print_unique:
  print(f"{c}: {df[c].unique()}")
print("============================")



## PART B: Simple Filter
backrest = df[df["sitzbankmodelle"] == "mit Rückenlehne"]
print(backrest)

## PART C: Advanced Filter & Data Augmentation

eth = Point(2683756.785475, 1247981.202527)
x_eth = 2683756.785475
y_eth = 1247981.202527

# filter benches north of ETH
northern = df[df["geometry"].y > 1247981]
print(northern) # This print-statement is optional

# compute distance
dist = []
dt = shapely.distance(northern["geometry"], eth)
idx = dt.index
for i in idx:
  dist.append(dt[i].item())
  
# add to df
northern["Distance to ETH"] = dist
print(northern)

# calculate percentage
frac = northern.shape[0]/df.shape[0]
print("Percentage of Benches north of ETH: "+str(np.round(frac*100, 2))+"%")

## PART D: Plotting
# plot ZH 
mapZH = geopandas.read_file('./maps/zhkreise.shp')
mapZH.crs = "EPSG:2056" ## 4326: Geocode for ZH, 2056: Geocode for CH
### ======== Complete the code to create/save an image ==========
ax = mapZH.plot()
plt.axis('off')
plt.savefig('./cx_out/basemap.png')

## Step 1: Plot all benches in Zurich
#mapZH = geopandas.read_file('./maps/stadtzh.shp')
benches = geopandas.GeoSeries(df["geometry"], crs="EPSG:2056")
benches = benches.to_crs(mapZH.crs)
benches.plot(ax=ax, color="lime", markersize=6)
plt.savefig('./cx_out/stadtZH.png')

# overlay northern
map_north = geopandas.GeoSeries(northern["geometry"], crs="EPSG:2056")
map_north = map_north.to_crs(mapZH.crs)
map_north.plot(ax=ax, color="red", marker="*", markersize=1)
plt.savefig('./cx_out/combi.png')

### =============================================================


## Step 2: Combine all benches north of ETH and all city benches
##         in one image
#bigmap = mapZH.plot()
#northern.plot(ax=???, marker=???, color=???, markersize=???)
### ======== Complete the code to create/save an image ==========


### =============================================================


