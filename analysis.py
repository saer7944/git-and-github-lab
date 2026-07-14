import pandas as pd
df = pd.read_csv("Data.csv")
print("Number of transactions" , len(df))
print(("Mean transactionprice:", df["price"].mean()))
# Print the largest sale:
print("Max_Price":", df["Price"].max())