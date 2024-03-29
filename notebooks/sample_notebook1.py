# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 2

# %%
import sys
sys.path.append('../src')  # srcディレクトリへの相対パスを追加

# %%
from data_loader import load_iris_data
from models import train_logistic_regression
from visualizations import plot_pairplot, plot_heatmap
from utils import split_data
from evaluation import evaluate_model

# Load and preprocess data
df = load_iris_data()

# Visualize data
plot_pairplot(df)
plot_heatmap(df)

# Split data into train and test sets
X_train, X_test, y_train, y_test = split_data(df)

# Train and evaluate models
lr_model = train_logistic_regression(X_train, y_train)
lr_accuracy, lr_report = evaluate_model(lr_model, X_test, y_test)
print(f"Logistic Regression Accuracy: {lr_accuracy}")
print(f"Logistic Regression Report:\n{lr_report}")
