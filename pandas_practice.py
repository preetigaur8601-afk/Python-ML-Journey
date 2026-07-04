import pandas as pd
import numpy as np

data = {
    "name": ["Bhoomi", "Priya", "Rahul", "Anjali"],
    "branch": ["AIML", "CS", "AIML", "CS"],
    "marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)
print(df)

# Filtering
print(df[df["marks"] > 80])

# GroupBy
print(df.groupby("branch")["marks"].mean())

# Null values
data2 = {
    "name": ["Bhoomi", "Priya", "Rahul", "Anjali"],
    "marks": [85, np.nan, 78, np.nan]
}
df2 = pd.DataFrame(data2)
df2["marks"] = df2["marks"].fillna(df2["marks"].mean())
print(df2)
