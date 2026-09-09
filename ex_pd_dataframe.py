import pandas as pd

df = {"Name": ["Alice", "Bob", "Charlie", "David"],
      "Age": [25, 30, 35, 40],
      "City": ["New York", "Los Angeles", "Chicago", "Houston"] }
df = pd.DataFrame(df)

print(df)