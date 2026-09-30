# Smoke test for the project - synthetic data
import sys
import os
sys.path.append(r"c:\Users\IQ\OneDrive\Documents\padas 1\newai")

import pandas as pd
import numpy as np
from data_processor import DataProcessor

print('Creating synthetic dataset...')
np.random.seed(42)
df = pd.DataFrame({
    'num1': np.random.randn(100),
    'num2': np.random.randn(100) * 10,
    'cat1': np.random.choice(['A','B','C'], size=100),
    'target': np.random.choice([0,1], size=100)
})

print('Initializing DataProcessor...')
proc = DataProcessor()

print('Processing data...')
df_processed, problem = proc.process_data(df, 'target', categorical_columns=['cat1'])
print('Processed shape:', df_processed.shape)
print('Problem type detected:', problem)

print('Training model...')
model, metrics = proc.train_model(df_processed, 'target', categorical_columns=['cat1'], model_type='rf')
print('Trained model:', type(model))
print('Metrics:', metrics)

print('Making a prediction on first row...')
X = df_processed.drop('target', axis=1)
pred = proc.predict(X.iloc[[0]], 'rf_classification')
print('Prediction:', pred)

print('Smoke test completed successfully.')
