import pandas as pd

df = pd.read_csv("Data/labeled_sequences.csv")
print(" Sequence label counts:")
print(df["label"].value_counts())
