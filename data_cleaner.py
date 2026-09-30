import pandas as pd
import numpy as np

def handle_nulls(df: pd.DataFrame, strategy='mean'):
    if strategy == 'mean':
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == 'median':
        return df.fillna(df.median(numeric_only=True))
    elif strategy == 'drop':
        return df.dropna()
    else:
        return df

def remove_duplicates(df: pd.DataFrame):
    return df.drop_duplicates()

def handle_outliers(df: pd.DataFrame, z_thresh=3):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    z_scores = np.abs((df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std())
    mask = (z_scores < z_thresh).all(axis=1)
    return df[mask]

if __name__ == "__main__":
    df = pd.DataFrame({
        'A': [1, 2, 2, 100, np.nan],
        'B': [5, 5, 5, 5, 5],
        'C': [1, 2, 3, 4, 5]
                        })
    print("Original:\n", df)
    print("No nulls:\n", handle_nulls(df))
    print("No duplicates:\n", remove_duplicates(df))
    print("No outliers:\n", handle_outliers(df)) 