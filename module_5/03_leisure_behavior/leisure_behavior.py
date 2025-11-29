#!/usr/bin/env python
# coding: utf-8

# In[191]:


import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas
import os
import shapely
from shapely import box, LineString, normalize, Polygon, Point
import seaborn as sns

tic = time.time()


# # Get data

# In[192]:


 #############################################
##    TASK 0 --> DATA IMPORT & DESCRIPTION   ##
 #############################################
DATA_PATH = './maps/moveandchill.gpkg'
data = geopandas.read_file(DATA_PATH)
data


# In[193]:


data.dtypes


# In[194]:


print(f"Number of sensors {len(data['sensor_eui'].unique())}")


# # Filter Tasks

# In[199]:


 #######################################
##      TASK 1 --> SIMPLE FILTERING    ##
 #######################################
df = data.copy()
df_noise =  df[df["noise"].astype(int) > 50]
print(df_noise)


# In[200]:


# filter high sit
df_high_usage = data[data['sit']>75]
df_high_usage


# In[201]:


# filter high temp
df_high_temp = data[data['temperature']>40]
df_high_temp


# In[202]:


df.info()


# # Statistics

# ## Details on noise level

# In[204]:


df['noise'].describe()


# In[205]:


# view noise dist
sns.histplot(data=df,
             x='noise',
             bins=30,
            )
plt.title("Noise level").figure.savefig('./cx_out/noise_dist.png')


# ## Density time

# In[206]:


# probability distribution by date / sensor
fig = plt.figure(figsize=(12, 6))
sns.kdeplot(
    data=data,
    x="zeitpunkt",
    hue="sensor_eui",
    common_norm=False,
    fill=True,
    alpha=0.35
)
fig.figure.savefig('./cx_out/kde1.png')


# ## Usage vs Temperature and humidity

# In[207]:


# usage vs temperature
# clean 
df = data[(data['sit'] > 0) & (data['sit'] < 100) & (data['temperature']!= -100)].copy()
# plot
fig = plt.figure(figsize=(12, 6))
plt.figure(figsize=(10,6))
sns.scatterplot(
    data=df,
    x="temperature",
    y="sit",
    hue="sensor_eui",
    alpha=0.6
)
plt.title("Usage vs temp")
fig.figure.savefig('./cx_out/use_vs_temp.png')


# In[208]:


# humidity vs usage
fig = plt.figure(figsize=(12, 6))
sns.relplot(x="humidity", y="sit", hue="sensor_eui", 
            #size="temperature",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=df)
fig.figure.savefig('./cx_out/use_vs_humid.png')


# In[209]:


df.head()


# # Time plots

# ## Detail for 3 dates

# In[210]:


 ###################################################
##    TASK 3 --> TIME-DEPENDENCY OF BENCH USAGE    ##
 ###################################################


print("Calculate usage over time...\n")
print("List of Bench IDs:")
bench = "0080E115003BE631"

hours = np.arange(0,24, 24/46)

## Select the correct bench data
df = data.copy()
df = df[df["sensor_eui"] == bench].sort_values("zeitpunkt").copy()

dates = ["2022-08-11","2022-08-13","2022-08-14", "2022-08-23"]

# plot 
fig = plt.figure(figsize=(15,9))

for date in dates:
    day = df[df["zeitpunkt"].dt.date == pd.to_datetime(date).date()]
    if len(day) == 46:
        plt.plot(hours, day["sit"].values, label=date)
plt.xlabel('Time [h]')
plt.xticks(np.arange(0,25,1))
plt.ylabel('Occupancy [%]')
plt.legend()
plt.title("Usage of bench id "+str(bench), fontsize=16)
plt.grid(True)
plt.savefig('./cx_out/usage_over_time.png')



# ## View 1 bench daily use

# In[211]:


# view sit time for one bench
sel_id = "0080E115003BC8D7"
def plot_sit_time(df, bench):
    df = data[data["sensor_eui"]==bench].copy()
    df["sit_duration_min"] = df["sit"]/100*30
    df = df.groupby(df['zeitpunkt'].dt.date)['sit_duration_min'].sum().reset_index()
    fig = plt.figure(figsize=(10,4))
    plt.bar(df['zeitpunkt'], df['sit_duration_min'])
    plt.xlabel('Date')
    plt.ylabel('Minutes')
    plt.title(f'Sit time duration for bench {sel_id}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig
fig = plot_sit_time(data, sel_id)


# ## View  daily use all benches

# In[212]:


# plot all sensors
import math
sensor_list = data['sensor_eui'].unique()
n = len(sensor_list)
cols = 4                                # 4 plots per row (adjust if needed)
rows = math.ceil(n / cols)
fig = plt.figure(figsize=(cols * 4, rows * 2))
for i, sensor in enumerate(sensor_list):
    # filter df
    df = data[data["sensor_eui"]==sensor].copy()
    df["sit_duration_min"] = df["sit"]/100*30
    df = df.groupby(df['zeitpunkt'].dt.date)['sit_duration_min'].sum().reset_index()

    # plot
    plt.subplot(rows, cols, i + 1)
    plt.bar(df['zeitpunkt'], df['sit_duration_min'])
    plt.xlabel('Date', fontsize=8)
    plt.ylabel('Minutes', fontsize=8)
    plt.title(f'Sit time duration for bench {sensor}', fontsize=8)
    plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()
fig.figure.savefig('./cx_out/sit_time_per_bench.png')


# # Geomapping

# In[214]:


##################################
##      TASK 4 --> PLOTTING     ##
##################################

df = data.copy()
# base map
mapZH = geopandas.read_file('./maps/zhkreise.shp')
mapZH.crs = "EPSG:2056" ## Density time
mapZH
ax = mapZH.plot(figsize=(12,6))
plt.axis('off')

# add benches
plot_data = geopandas.GeoSeries(df["geometry"],crs="EPSG:2056")
plot_data.plot(ax=ax, color="blue", marker="*", markersize=1)

ax.figure.savefig('./cx_out/whole.png')


# In[215]:


# --- overlays: whole / noisy / busy ---
subsets = [
    (df, "./cx_out/whole.png", "blue"),                                   # all benches
    (df[df["noise"] >= df["noise"].quantile(0.75)], "./cx_out/noisy.png", "red"),   # noisiest
    (df[df["sit"]   >= df["sit"].quantile(0.75)], "./cx_out/busy.png",  "green"),   # busiest
]

for sub, path, color in subsets:
    ax = mapZH.plot(figsize=(8,8), color="white", edgecolor="black")
    plot_data = geopandas.GeoSeries(sub["geometry"], crs="EPSG:2056").to_crs(mapZH.crs)
    plot_data.plot(ax=ax, color=color, marker="*", markersize=5)
    plt.axis('off')
    plt.title(path)
    plt.savefig(path, bbox_inches='tight')


# In[216]:




# In[217]:


### TIME CHECK
toc = time.time()
print(str(toc-tic), "s elapsed")

