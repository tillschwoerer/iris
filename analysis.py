import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

df.head()
df.describe()
df.tail()

# EDA
df.species.value_counts()
df.groupby('species').sepal_length.mean()

# Add further statistics
df.groupby('species').sepal_length.median()
df[["sepal_length", "sepal_width"]].mean()

# Here some visualizations
sns.scatterplot(
    data=df,
    x="sepal_length",
    y="sepal_width")

sns.scatterplot(
    data=df,
    x="petal_length",
    y="petal_width")
