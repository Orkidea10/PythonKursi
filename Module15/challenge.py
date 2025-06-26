import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("weather_tokyo_data.csv")

avg_temp=df.groupby("year")['temperature'].mean()
print(avg_temp)
