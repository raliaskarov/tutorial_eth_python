import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

## ===============  SKELETON FOR PART C  =================
class Pingu:
  def __init__(self, species, island, clength, cdepth, flength, bmi, sex):
    self.species = species
    self.island = island
    self.clength = clength
    self.cdepth = cdepth
    self.flength = flength
    self.bmi = bmi
    self.sex = sex
  
  def computeArea(self):
    return self.clength * self.cdepth
    
## =======================================================

## Part A: Initialize Data
df_size = pd.read_csv('./pingu/penguins_size.csv')

print(df_size.info())
print(df_size.head())
print(df_size.describe())

## Part B.1: Counter with bar plot
bar1 = df_size['species'].value_counts().plot(kind='bar')
bar1.figure.savefig('./cx_out/bar1.png')

## Part B.2: Investigate different facet grids for species and sex. 
##           Which is better suited?

rp1 = sns.FacetGrid(df_size, hue="species").map(plt.scatter, "culmen_length_mm", "flipper_length_mm").add_legend()
rp1.figure.savefig('./cx_out/fg1.png')

rp2 = sns.FacetGrid(df_size, hue="sex").map(plt.scatter, "culmen_length_mm", "flipper_length_mm").add_legend()
rp2.figure.savefig('./cx_out/fg2.png')


## Part B.3: Investigate different pairplots for species and sex. 
##           Which is better suited?

pair1 = sns.pairplot(df_size, hue="species", diag_kind='hist')
pair1.figure.savefig('./cx_out/pair1.png')

pair2 = sns.pairplot(df_size, hue="sex", diag_kind='hist')
pair2.figure.savefig('./cx_out/pair2.png')


### Part C: Compute Culmen surface using the Pingu-class
##          Attributes: species,island,culmen_length_mm,culmen_depth_mm,
##                      flipper_length_mm,body_mass_g,sex
c_area = []

for i in range(df_size.shape[0]):
  curr_pingu = Pingu(df_size.loc[i,["species"]], df_size.loc[i,["island"]], df_size.loc[i,["culmen_length_mm"]].item(), df_size.loc[i,["culmen_depth_mm"]].item(), df_size.loc[i,["flipper_length_mm"]], df_size.loc[i,["body_mass_g"]],df_size.loc[i,["sex"]])
  curr_area = curr_pingu.computeArea().item()
  c_area.append(curr_area)

print(c_area)
df_size['culmen_area_mm'] = c_area
print(df_size)

df2 = df_size.loc[:, ["culmen_length_mm", "culmen_depth_mm", "culmen_area_mm", "species"]]
print(df2)

pair_new = sns.pairplot(df2, hue="species", diag_kind='hist')
pair_new.figure.savefig('./cx_out/pair_new.png')
print(df2.describe())