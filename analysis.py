import pandas as pd
df = pd.read_csv("Data.csv")
print("Nrows:", len(df))
print(("M_price:", df["price"].mean()))
# Print the largest sale:
print("Max_Price":", df["Price"].max())