import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

my_dataset=pd.read_csv("avgIQpercountry.csv")

print(my_dataset.info())

plt.figure(figsize=(10,6))
sns.histplot(my_dataset["Average IQ"])
plt.title("Histogram of Average IQ")
plt.xlabel("Average Iq")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()