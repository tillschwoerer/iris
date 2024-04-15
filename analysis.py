import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

df.head()
df.describe()
df.tail()

# EDA
df.species.value_counts()
df.groupby('species').sepal_length.mean()

# Visualizations
sns.scatterplot(
    data=df,
    x="sepal_length",
    y="sepal_width")
