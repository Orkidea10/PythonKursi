import pandas as pd

produktet=["apples",'bananas',"oranges",'grapes',"pineapples"]
sales=[150,200,180,90,60]

sales_perProducts=pd.Series(sales,index=produktet)
print(sales_perProducts)

#shitja e rrushit
print(sales_perProducts['grapes'])

best_selling_product=sales_perProducts.idxmax()
print(best_selling_product)
