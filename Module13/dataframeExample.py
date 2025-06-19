import pandas as pd

data={"Name":["Alice","Bob","Charlie"],
      "Age":[25,30,32],
      "City":["New york","San Francisco","Los Angeles"]
      }

df=pd.DataFrame(data)
print(df)