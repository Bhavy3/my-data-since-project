import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score, mean_squared_error

@st.cache_data(ttl=3600)  # Cache results for 1 hour
def compute_model_metrics(model, X_test, y_test):
    """Compute metrics for a single model efficiently"""
    try:
        y_pred = model.predict(X_test)
        acc = model.score(X_test, y_test) if hasattr(model, 'score') else None
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        return {'Score': acc, 'RMSE': rmse}
    except Exception as e:
        return {'Score': 'Error', 'RMSE': 'Error'}

def compare_models(models: dict, X_test, y_test):
    st.title("🧮 Model Compare Panel")
    
    # Convert to efficient dtypes
    if X_test.dtype == 'float64':
        X_test = X_test.astype('float32')
    if hasattr(y_test, 'dtype') and y_test.dtype == 'int64':
        y_test = y_test.astype('int32')
    
    # Compute metrics in parallel using list comprehension
    results = [
        {'Model': name, **compute_model_metrics(model, X_test, y_test)}
        for name, model in models.items()
    ]
    st.dataframe(pd.DataFrame(results))

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    data = load_iris()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = X[:100], X[100:], y[:100], y[100:]
    models = {
        'LogisticRegression': LogisticRegression(max_iter=200).fit(X_train, y_train),
        'DecisionTree': DecisionTreeClassifier().fit(X_train, y_train)
    }
    compare_models(models, X_test, y_test) 