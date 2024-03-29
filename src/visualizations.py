import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_pairplot(df):
    sns.pairplot(df, hue='target_names')
    plt.show()

def plot_heatmap(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm')
    plt.show()