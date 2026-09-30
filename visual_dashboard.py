import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data(ttl=3600)  # Cache data for 1 hour
def prepare_filtered_data(df: pd.DataFrame, filter_cols, filter_values):
    """Efficiently filter dataframe"""
    filtered_df = df.copy()
    for col, values in zip(filter_cols, filter_values):
        filtered_df = filtered_df[filtered_df[col].isin(values)]
    return filtered_df

def show_dashboard(df: pd.DataFrame):
    st.title("📊 Visual Dashboard")
    st.write("Select columns to visualize and filter your data:")
    if df.empty:
        st.warning("No data available.")
        return
    
    # Optimize memory usage
    df = df.copy()
    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = df[col].astype('float32')
    
    columns = df.columns.tolist()
    filter_col = st.multiselect("Filter columns", columns)
    
    filter_values = []
    for col in filter_col:
        # Get unique values efficiently
        unique_vals = df[col].unique()
        if len(unique_vals) > 100:  # Sample for large datasets
            unique_vals = unique_vals[:100]
        selected = st.multiselect(f"Values for {col}", unique_vals, default=list(unique_vals))
        filter_values.append(selected)
    
    # Use cached function for filtering
    filtered_df = prepare_filtered_data(df, filter_col, filter_values)
    
    # Show sample of filtered data
    st.write("Filtered Data Sample:", filtered_df.head())
    chart_type = st.selectbox("Chart type", ["Bar", "Line", "Area", "Histogram"])
    x_col = st.selectbox("X axis", columns)
    y_col = st.selectbox("Y axis", columns)
    if chart_type == "Bar":
        st.bar_chart(filtered_df[[x_col, y_col]].set_index(x_col))
    elif chart_type == "Line":
        st.line_chart(filtered_df[[x_col, y_col]].set_index(x_col))
    elif chart_type == "Area":
        st.area_chart(filtered_df[[x_col, y_col]].set_index(x_col))
    elif chart_type == "Histogram":
        st.write(f"Histogram data: {filtered_df[y_col].describe()}")
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.hist(filtered_df[y_col], bins=30)
        ax.set_title(f"Histogram of {y_col}")
        plt.tight_layout()
        st.write("Displaying histogram plot...")
        st.pyplot(fig)
        plt.close(fig)

if __name__ == "__main__":
    st.set_page_config(page_title="Visual Dashboard", layout="wide")
    st.sidebar.title("Demo Data")
    uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        show_dashboard(df)
    else:
        st.info("Upload a CSV file to get started.") 