import pandas as pd
import matplotlib.pyplot as plt

#getting data from file
df=pd.read_csv("avgIQpercountry.csv")
#filtering the data based on avg IQ
filtered_DF=df[df["Average IQ"]>=100]
#sorting data
filtered_DF=filtered_DF.sort_values(by="Average IQ", ascending=False)
#test the data
print(filtered_DF)
#krijimi i figures ku do te shfaqen te dhenat
plt.figure(figsize=(14,8))
#grafikat si shtylla ku definohet qka eshte ne x e qka ne y
bars=plt.bar(filtered_DF["Country"],filtered_DF["Average IQ"], color="skyblue")

#make up for the plot
plt.title("Average IQ by country (IQ >=100 ",fontsize=16)
plt.xlabel("Country",fontsize=14)
plt.ylabel("Average IQ",fontsize=14)

plt.bar_label(bars,fmt="%.2f", fontsize=10,color="black")

plt.tight_layout()

#SHFAQEN TE DHENAT
plt.show()
