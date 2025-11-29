import pandas as pd
import requests
from collections import defaultdict


print("Part A: Import and inspect the data")
print("===================================\n")

login = "max"
pwd = "test1234"
payload = {'user': 'max', 'pwd': 'test1234'}
#response = requests.get("https://data.demo-uni.ch/resource/grades.json", params=payload) # modify the given GET-request by adding login parameters to the response
response = requests.get("https://data.demo-uni.ch/resource/grades.json?user=max&pwd=test1234")
print(response)
# pull the data from the response
grades_data_dict = response.json()
print(grades_data_dict.keys())

# convert dictionary to dataframe
df = pd.DataFrame(grades_data_dict)
print(df.head())
print("=======================================================")
print(df.info())
print("=======================================================")
print(df.describe())
# inspect imported data


print("")
print("Part B: Analyze the data")
print("========================\n")

# check nones
print(f"Null grades: {df[df["grade"].isna()].shape[0]}")

# count grades
n_grades = df.shape[0]
avg_grade = sum(df["grade"])/n_grades
max_grade = df["grade"].max()
df_max = df[df["grade"]==max_grade]
print(f"Number of grades: {n_grades}")
print(f"Average grade: {avg_grade:.2f}")
print(f"max_grade is: {max_grade} for following students")
#print(df_max)
for idx, _ in enumerate(df_max):
  name = df_max.iloc[idx]["name"]
  course = df_max.iloc[idx]["course"]
  grade = df_max.iloc[idx]["grade"]
  print(f" - {name} for {course} (grade {grade})")
# Extension: get student with highest grade (use grouping function)