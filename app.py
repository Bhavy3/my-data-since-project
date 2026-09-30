# -*- coding: utf-8 -*-
"""
AI-Powered Data Analysis Tool
A Streamlit application for automated data analysis and machine learning.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
import joblib
from data_processor import DataProcessor
from ml_models import MLModels
from streamlit_option_menu import option_menu
import logging
import io
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
# Configure page
st.set_page_config(
    page_title="AI Data Analysis Tool",
    page_icon="🤖 ®️ 😈",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Hide the hamburger menu and other unnecessary elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dark theme colors */
    :root {
        --primary-color: #7c3aed;
        --bg-color: #111827;
        --secondary-bg: #1f2937;
        --text-color: #e5e7eb;
        --border-color: #374151;
    }
    
    /* Main container - full width */
    .stApp {
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: var(--bg-color);
        color: var(--text-color);
    }
    
    /* Sidebar styling */
    /* .css-1d391kg {
        background-color: var(--secondary-bg);
        padding: 2rem;
        border-right: 1px solid var(--border-color);
        width: 300px !important;
    } */
    
    /* Remove sidebar collapse button */
    /* .css-1siy2j7 {
        display: none !important;
    } */
    
    /* Main content area - full width */
    .main .block-container {
        padding: 2rem 3rem;
        background-color: var(--secondary-bg);
        border-radius: 0;
        box-shadow: none;
        margin: 0;
        max-width: 100% !important;
    }
    
    /* Remove default padding */
    .stApp > header {
        background-color: var(--bg-color);
        padding: 0;
    }
    
    .stApp > main {
        padding: 0;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-size: 2.5em !important;
        font-weight: 700 !important;
        color: var(--text-color) !important;
        margin-top: 1.5em !important;
        margin-bottom: 1em !important;
        padding-bottom: 0.5em;
        border-bottom: 2px solid var(--border-color);
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        height: 4em;
        font-size: 1.3em;
        font-weight: 600;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 12px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        margin: 1rem 0;
    }
    
    .stButton>button:hover {
        background-color: #6d28d9;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.3);
    }
    
    /* Input fields */
    .stSelectbox, .stMultiselect {
        font-size: 1.3em;
        background-color: var(--bg-color);
        border-radius: 10px;
        border: 1px solid var(--border-color);
        padding: 0.5rem;
        margin: 1rem 0;
    }
    .stTextArea>div>div>textarea {
        font-size: 1.3em;
        border-radius: 10px;
        border: 1px solid var(--border-color);
        padding: 1rem;
        background-color: var(--bg-color);
        color: var(--text-color);
        margin: 1rem 0;
    }
    
    /* Text and content */
    .stMarkdown {
        font-size: 1.3em;
        line-height: 1.8;
        color: var(--text-color);
        margin: 1.5rem 0;
    }
    
    /* DataFrames */
    .stDataFrame {
        font-size: 1.2em;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        margin: 2rem 0;
        background-color: var(--bg-color);
        width: 100% !important;
    }
    
    /* Cards and containers */
    .stMetric {
        background-color: var(--secondary-bg);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        margin: 1.5rem 0;
        border: 1px solid var(--border-color);
    }
    
    /* Progress bars */
    .stProgress > div > div {
        background-color: var(--primary-color);
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #064e3b;
        border: 1px solid #059669;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Warning messages */
    .stWarning {
        background-color: #78350f;
        border: 1px solid #d97706;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Error messages */
    .stError {
        background-color: #7f1d1d;
        border: 1px solid #dc2626;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Info messages */
    .stInfo {
        background-color: #1e3a8a;
        border: 1px solid #3b82f6;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        margin: 2rem 0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 4rem;
        white-space: pre-wrap;
        background-color: var(--bg-color);
        border-radius: 10px;
        padding: 0 2rem;
        color: var(--text-color);
        font-size: 1.2em;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-color);
        color: white;
    }
    
    /* Plotly charts */
    .js-plotly-plot {
        background-color: transparent !important;
        border-radius: 12px;
        padding: 0 !important;
        margin: 1rem 0 !important;
        width: 100% !important;
        min-height: 400px !important;
        height: auto !important;
    }
    
    /* Plotly chart containers */
    .stPlotlyChart {
        background-color: transparent !important;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
        width: 100% !important;
        min-height: 400px !important;
    }
    
    /* Plotly chart iframe */
    .js-plotly-plot .plotly {
        background-color: transparent !important;
        width: 100% !important;
        height: 400px !important;
    }
    
    /* Fix for black bars in charts */
    .stPlotlyChart > div {
        background-color: transparent !important;
        min-height: 400px !important;
    }
    
    /* File uploader */
    .stFileUploader {
        background-color: var(--secondary-bg);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        width: 100% !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: var(--secondary-bg);
        color: var(--text-color);
        font-size: 1.2em;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Remove default padding from all elements */
    .element-container {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Make all containers full width */
    .stHorizontalBlock {
        width: 100% !important;
    }
    
    /* Adjust column spacing */
    .row-widget.stHorizontalBlock {
        gap: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

def parse_prompt(prompt, columns):
    """Parse user prompt to infer task details"""
    # Convert prompt to lowercase for easier matching
    prompt = prompt.lower()
    
    # Initialize result dictionary
    result = {
        'problem_type': 'regression',  # Default to regression
        'target': None,
        'features': [],
        'task': prompt
    }
    
    # Try to identify target column
    for col in columns:
        col_lower = col.lower()
        # Check if column name appears in prompt
        if col_lower in prompt:
            # If it's the first match, assume it's the target
            if result['target'] is None:
                result['target'] = col
            else:
                result['features'].append(col)
    
    # If no target found, try to infer from common patterns
    if result['target'] is None:
        for col in columns:
            col_lower = col.lower()
            if any(word in col_lower for word in ['price', 'cost', 'amount', 'value', 'score', 'rating']):
                result['target'] = col
                break
    
    # If still no target, use the last column
    if result['target'] is None and columns:
        result['target'] = columns[-1]
    
    # Add remaining columns as features
    if result['features'] == []:
        result['features'] = [col for col in columns if col != result['target']]
    
    # Try to identify problem type
    classification_keywords = ['classify', 'category', 'type', 'group', 'label', 'predict class']
    if any(keyword in prompt for keyword in classification_keywords):
        result['problem_type'] = 'classification'
    
    return result

# Initialize session state variables if they don't exist
if 'df' not in st.session_state:
    st.session_state.df = None
if 'parsed' not in st.session_state:
    st.session_state.parsed = None
if 'target_column' not in st.session_state:
    st.session_state.target_column = None
if 'feature_columns' not in st.session_state:
    st.session_state.feature_columns = None
if 'model' not in st.session_state:
    st.session_state.model = None
if 'metrics' not in st.session_state:
    st.session_state.metrics = None
if 'task_description' not in st.session_state:
    st.session_state.task_description = None
if 'X' not in st.session_state:
    st.session_state.X = None
if 'y' not in st.session_state:
    st.session_state.y = None

def create_sidebar():
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h1 style='color: var(--primary-color); font-size: 1.8em; margin-bottom: 0.5rem;'>AI Data Analysis</h1>
            <p style='color: var(--text-color); opacity: 0.8;'>Your AI-Powered Data Science Assistant</p>
        </div>
        """, unsafe_allow_html=True)
        
        selected = option_menu(
            menu_title=None,
            options=["Home", "Data Upload", "Data Analysis", "Model Training", "Model Analysis", "Predictions"],
            icons=['house', 'cloud-upload', 'graph-up', 'cpu', 'search', 'calculator'],
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "var(--secondary-bg)"},
                "icon": {"color": "var(--text-color)", "font-size": "1.2em"},
                "nav-link": {
                    "font-size": "1.1em",
                    "text-align": "left",
                    "margin": "0.5rem 0",
                    "padding": "0.8rem 1rem",
                    "color": "var(--text-color)",
                    "border-radius": "8px",
                    "background-color": "transparent",
                },
                "nav-link-selected": {
                    "background-color": "var(--primary-color)",
                    "color": "white",
                },
            }
        )
        
        st.markdown("---")
        
        # Add back the description box with green color
        st.markdown("""
        <div style='background-color: #064e3b; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border: 1px solid #059669;'>
            <h3 style='color: #a7f3d0; font-size: 1.2em; margin-bottom: 1rem;'>About This Tool</h3>
            <p style='color: #d1fae5; margin: 0; line-height: 1.6;'>
                This AI-powered Data Science Assistant helps you:
                <br>• Analyze your data
                <br>• Train machine learning models
                <br>• Make predictions
                <br>• Understand model behavior
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.df is not None:
            st.markdown("""
            <div style='background-color: var(--bg-color); padding: 1rem; border-radius: 8px; margin-top: 1rem;'>
                <h3 style='color: var(--text-color); font-size: 1.1em; margin-bottom: 0.5rem;'>Current Dataset</h3>
                <p style='color: var(--text-color); opacity: 0.8; margin: 0;'>
                    Rows: {:,}<br>
                    Columns: {:,}
                </p>
            </div>
            """.format(
                st.session_state.df.shape[0],
                st.session_state.df.shape[1]
            ), unsafe_allow_html=True)
    
    return selected

def show_home():
    st.title("🤖 AI-Powered Data Science Assistant")
    st.markdown("""
    ### Welcome to your AI Data Science Assistant!
    
    This tool helps you perform advanced data analysis and machine learning tasks with ease.
    
    #### Features:
    - 📊 Interactive Data Analysis
    - 🤖 Automated Model Selection
    - 📈 Advanced Visualizations
    - 🔍 Model Interpretability
    - 📱 Mobile-friendly Interface
    
    Get started by uploading your dataset in the Data Upload section!
    """)
    
    # Display current dataset info if available
    if st.session_state.df is not None:
        st.success(f"""
        ✅ Dataset is loaded!
        - Rows: {st.session_state.df.shape[0]:,}
        - Columns: {st.session_state.df.shape[1]:,}
        - Memory usage: {st.session_state.df.memory_usage().sum() / 1024 / 1024:.2f} MB
        """)
    return None

def create_visualization(df, col, viz_type):
    """Helper function to create visualizations"""
    # Set default theme and layout for all charts
    default_layout = {
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'font': {'color': '#e5e7eb'},
        'xaxis': {'color': '#e5e7eb', 'gridcolor': '#374151'},
        'yaxis': {'color': '#e5e7eb', 'gridcolor': '#374151'},
        'title': {'font': {'color': '#e5e7eb'}},
        'height': 400,
        'margin': {'l': 40, 'r': 40, 't': 60, 'b': 40}
    }
    
    if viz_type == "histogram":
        fig = px.histogram(df, x=col, title=f"Distribution of {col}", marginal="box")
        fig.update_layout(**default_layout)
        return fig
    elif viz_type == "box":
        fig = px.box(df, y=col, title=f"Box Plot of {col}")
        fig.update_layout(**default_layout)
        return fig
    elif viz_type == "bar":
        value_counts = df[col].value_counts()
        fig = px.bar(x=value_counts.index, y=value_counts.values, title=f"Frequency of {col}")
        fig.update_layout(**default_layout)
        return fig
    elif viz_type == "pie":
        value_counts = df[col].value_counts()
        fig = px.pie(values=value_counts.values, names=value_counts.index, title=f"Distribution of {col}")
        fig.update_layout(**default_layout)
        return fig
    return None

def show_data_analysis():
    if st.session_state.df is None:
        st.warning("Please upload a dataset first!")
        return

    st.markdown("## 📈 Data Analysis")

    # Basic Statistics
    st.markdown("### Basic Statistics")
    st.write(st.session_state.df.describe())

    # Column Selection for Analysis
    selected_columns = st.multiselect(
        "Select columns to analyze",
        st.session_state.df.columns.tolist(),
        default=st.session_state.df.select_dtypes(include=['int64', 'float64']).columns.tolist()[:3]
    )

    # Clear previous plot containers by using a unique key for each selection
    plot_key = "_".join(selected_columns) if selected_columns else "none"
    plot_container = st.container()
    with plot_container:
        if selected_columns:
            # Distribution Plots
            st.markdown("### Distribution Analysis")
            for col in selected_columns:
                col_data = st.session_state.df[col]
                st.write(f"Column '{col}' data preview:", col_data.head())
                st.write(f"Column '{col}' data shape: {col_data.shape}")
                if col_data.empty or col_data.isnull().all():
                    st.warning(f"No valid data to plot for column '{col}'.")
                    continue
                # Only show graph containers if data is valid
                if st.session_state.df[col].dtype in ['int64', 'float64']:
                    fig_hist = create_visualization(st.session_state.df, col, "histogram")
                    fig_box = create_visualization(st.session_state.df, col, "box")
                    if fig_hist is not None or fig_box is not None:
                        col1, col2 = st.columns(2)
                        if fig_hist is not None:
                            with col1:
                                st.plotly_chart(
                                    fig_hist, 
                                    use_container_width=True, 
                                    key=f"hist_{col}_{plot_key}",
                                    config={
                                        'displayModeBar': True,
                                        'displaylogo': False,
                                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                                    }
                                )
                        if fig_box is not None:
                            with col2:
                                st.plotly_chart(
                                    fig_box, 
                                    use_container_width=True, 
                                    key=f"box_{col}_{plot_key}",
                                    config={
                                        'displayModeBar': True,
                                        'displaylogo': False,
                                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                                    }
                                )
                else:
                    fig_bar = create_visualization(st.session_state.df, col, "bar")
                    fig_pie = create_visualization(st.session_state.df, col, "pie")
                    if fig_bar is not None or fig_pie is not None:
                        col1, col2 = st.columns(2)
                        if fig_bar is not None:
                            with col1:
                                st.plotly_chart(
                                    fig_bar, 
                                    use_container_width=True, 
                                    key=f"bar_{col}_{plot_key}",
                                    config={
                                        'displayModeBar': True,
                                        'displaylogo': False,
                                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                                    }
                                )
                        if fig_pie is not None:
                            with col2:
                                st.plotly_chart(
                                    fig_pie, 
                                    use_container_width=True, 
                                    key=f"pie_{col}_{plot_key}",
                                    config={
                                        'displayModeBar': True,
                                        'displaylogo': False,
                                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                                    }
                                )
            # Correlation Analysis
            st.markdown("### Correlation Analysis")
            numeric_cols = st.session_state.df[selected_columns].select_dtypes(include=['int64', 'float64']).columns
            st.write(f"Correlation numeric columns: {list(numeric_cols)}")
            if len(numeric_cols) > 1:
                corr_matrix = st.session_state.df[numeric_cols].corr()
                st.write("Correlation matrix preview:", corr_matrix.head())
                fig = px.imshow(corr_matrix,
                              labels=dict(color="Correlation"),
                              title="Correlation Matrix")
                # Apply consistent styling
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font={'color': '#e5e7eb'},
                    height=500,
                    margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
                )
                if fig is None:
                    st.warning("No correlation matrix figure created.")
                else:
                    st.plotly_chart(
                        fig, 
                        use_container_width=True, 
                        key=f"corr_{plot_key}",
                        config={
                            'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                        }
                    )
            else:
                st.warning("Not enough numeric columns for correlation analysis.")
            # Scatter Plots
            if len(selected_columns) >= 2:
                st.markdown("### Scatter Plots")
                numeric_cols = st.session_state.df[selected_columns].select_dtypes(include=['int64', 'float64']).columns
                st.write(f"Scatter plot numeric columns: {list(numeric_cols)}")
                if len(numeric_cols) >= 2:
                    x_col = st.selectbox("Select X-axis", numeric_cols, key=f"x_{plot_key}")
                    y_col = st.selectbox("Select Y-axis", [col for col in numeric_cols if col != x_col], key=f"y_{plot_key}")
                    scatter_data = st.session_state.df[[x_col, y_col]]
                    st.write(f"Scatter plot data preview:", scatter_data.head())
                    fig = px.scatter(st.session_state.df, x=x_col, y=y_col,
                                   title=f"Scatter Plot: {x_col} vs {y_col}")
                    # Apply consistent styling
                    fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font={'color': '#e5e7eb'},
                        xaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
                        yaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
                        height=500,
                        margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
                    )
                    if fig is None:
                        st.warning("No scatter plot figure created.")
                    else:
                        st.plotly_chart(
                            fig, 
                            use_container_width=True, 
                            key=f"scatter_{plot_key}",
                            config={
                                'displayModeBar': True,
                                'displaylogo': False,
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                            }
                        )
                else:
                    st.warning("Not enough numeric columns for scatter plot.")

def show_data_upload():
    st.markdown("## 📊 Data Upload")
    
    # Create a container for the upload section
    with st.container():
        st.markdown("""
        <div style='background-color: var(--secondary-bg); padding: 2rem; border-radius: 12px; margin: 1rem 0;'>
            <h3 style='color: var(--text-color); margin-bottom: 1rem;'>Upload Your Dataset</h3>
            <p style='color: var(--text-color); opacity: 0.8;'>Supported format: CSV files</p>
        </div>
        """, unsafe_allow_html=True)
        
        # File uploader with custom styling
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=['csv'],
            help="Upload your dataset in CSV format"
        )
        
        if uploaded_file is not None:
            try:
                # Show loading spinner
                with st.spinner("Loading your dataset..."):
                    df = pd.read_csv(uploaded_file)
                    st.session_state.df = df
                
                # Success message with file info
                st.success(f"""
                ✅ Dataset loaded successfully!
                - Rows: {df.shape[0]:,}
                - Columns: {df.shape[1]:,}
                - Memory usage: {df.memory_usage().sum() / 1024 / 1024:.2f} MB
                """)
                
                # Create tabs for different data views
                tab1, tab2, tab3 = st.tabs(["📋 Data Preview", "📊 Data Info", "📈 Basic Stats"])
                
                with tab1:
                    st.markdown("### Data Preview")
                    st.dataframe(
                        df.head(),
                        use_container_width=True,
                        height=400
                    )
                
                with tab2:
                    st.markdown("### Data Information")
                    buffer = io.StringIO()
                    df.info(buf=buffer)
                    st.text(buffer.getvalue())
                
                with tab3:
                    st.markdown("### Basic Statistics")
                    st.dataframe(
                        df.describe(),
                        use_container_width=True
                    )
                
            except Exception as e:
                st.error(f"""
                ❌ Error loading file: {str(e)}
                
                Please ensure:
                - The file is a valid CSV
                - The file is not corrupted
                - The file is not too large
                """)

def show_model_training(df):
    st.markdown("## 🤖 Model Training")
    
    # Task description
    task_description = st.text_area(
        "Describe your business task (e.g., 'predict discount on hatchbacks')",
        value=st.session_state.task_description if st.session_state.task_description else "",
        height=100
    )
    
    if task_description:
        st.session_state.task_description = task_description
        
        # Parse prompt
        st.info("🔍 Parsing your prompt and inferring task...")
        parsed = parse_prompt(task_description, df.columns.tolist())
        st.session_state.parsed = parsed
        
        # Show AI inference
        st.write("**AI Inferred:**")
        st.json(parsed)
        
        # Model configuration
        st.markdown("### Model Configuration")
        col1, col2 = st.columns(2)
        
        with col1:
            # Detect problem type based on target column
            target_column = st.selectbox(
                "Target Column",
                df.columns,
                index=df.columns.get_loc(parsed['target']) if parsed['target'] in df.columns else 0
            )
            st.session_state.target_column = target_column
            
            # Automatically detect problem type
            if df[target_column].dtype in ['int64', 'float64']:
                unique_values = df[target_column].nunique()
                if unique_values <= 10:  # If less than 10 unique values, treat as classification
                    problem_type = "classification"
                else:
                    problem_type = "regression"
            else:
                problem_type = "classification"
            
            st.write(f"**Detected Problem Type:** {problem_type}")
        
        with col2:
            feature_columns = st.multiselect(
                "Feature Columns",
                [col for col in df.columns if col != target_column],
                default=[col for col in parsed['features'] if col in df.columns and col != target_column]
            )
            st.session_state.feature_columns = feature_columns
            
            model_type = st.selectbox(
                "Select Model Type",
                ["logistic", "knn", "rf", "gb", "svc", "xgboost", "lightgbm", "catboost"] if problem_type == "classification"
                else ["linear", "ridge", "lasso", "knn", "rf", "gb", "svr", "xgboost", "lightgbm", "catboost"]
            )
        
        if st.button("Train Model"):
            with st.spinner("Processing data and training model..."):
                # Data processing
                data_processor = DataProcessor()
                ml_models = MLModels()
                categorical_columns = df[feature_columns].select_dtypes(include=['object']).columns.tolist()
                
                processed_df, _ = data_processor.process_data(
                    df,
                    target_column,
                    categorical_columns=categorical_columns
                )
                
                X = processed_df[feature_columns]
                y = processed_df[target_column]
                
                # Store X and y in session state
                st.session_state.X = X
                st.session_state.y = y
                
                # Model training based on problem type
                if problem_type == "classification":
                    # For classification, ensure target is categorical
                    if y.dtype in ['int64', 'float64']:
                        y = y.astype('category')
                    model, metrics = ml_models.train_classification(X, y, model_type)
                else:
                    model, metrics = ml_models.train_regression(X, y, model_type)
                
                st.session_state.model = model
                st.session_state.metrics = metrics
                
                st.success("Model trained successfully!")
                
                # Display metrics
                st.markdown("### Model Performance")
                
                if problem_type == "classification":
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Accuracy", f"{metrics.get('accuracy', 0):.4f}")
                        st.metric("Precision", f"{metrics.get('precision', 0):.4f}")
                    with col2:
                        st.metric("Recall", f"{metrics.get('recall', 0):.4f}")
                        st.metric("F1 Score", f"{metrics.get('f1', 0):.4f}")
                    
                    # Display confusion matrix if available
                    if 'confusion_matrix' in metrics:
                        st.markdown("### Confusion Matrix")
                        fig = px.imshow(metrics['confusion_matrix'],
                                      labels=dict(x="Predicted", y="Actual", color="Count"),
                                      title="Confusion Matrix")
                        fig.update_layout(
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            font={'color': '#e5e7eb'},
                            height=400,
                            margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
                        )
                        st.plotly_chart(
                            fig, 
                            use_container_width=True,
                            config={
                                'displayModeBar': True,
                                'displaylogo': False,
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                            }
                        )
                
                else:  # Regression
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("R² Score", f"{metrics.get('r2', 0):.4f}")
                        st.metric("MAE", f"{metrics.get('mae', 0):.4f}")
                    with col2:
                        st.metric("MSE", f"{metrics.get('mse', 0):.4f}")
                        st.metric("RMSE", f"{metrics.get('rmse', 0):.4f}")
                    
                    # Display actual vs predicted plot
                    if 'y_pred' in metrics and 'y_true' in metrics:
                        st.markdown("### Actual vs Predicted")
                        # Ensure y_true and y_pred are lists/arrays
                        y_true = metrics['y_true'] if isinstance(metrics['y_true'], (list, np.ndarray, pd.Series)) else [metrics['y_true']]
                        y_pred = metrics['y_pred'] if isinstance(metrics['y_pred'], (list, np.ndarray, pd.Series)) else [metrics['y_pred']]
                        min_y = min(y_true)
                        max_y = max(y_true)
                        fig = px.scatter(x=y_true, y=y_pred,
                                       title="Actual vs Predicted Values",
                                       labels={'x': 'Actual', 'y': 'Predicted'})
                        fig.add_trace(px.line(x=[min_y, max_y], y=[min_y, max_y]).data[0])
                        fig.update_layout(
                            plot_bgcolor='rgba(0,0,0,0)',
                            paper_bgcolor='rgba(0,0,0,0)',
                            font={'color': '#e5e7eb'},
                            xaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
                            yaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
                            height=500,
                            margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
                        )
                        st.plotly_chart(
                            fig, 
                            use_container_width=True,
                            config={
                                'displayModeBar': True,
                                'displaylogo': False,
                                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                            }
                        )
                
                # Save model
                if st.button("Save Model"):
                    model_path = f"models/{model_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pkl"
                    os.makedirs("models", exist_ok=True)
                    joblib.dump(model, model_path)
                    st.success(f"Model saved to {model_path}")

def show_model_analysis(df, model, X, y):
    st.markdown("## 🔍 Model Analysis")
    
    if model is None or X is None or y is None:
        st.warning("Please train a model first!")
        return
    
    # Feature Importance
    st.markdown("### Feature Importance")
    if hasattr(model, 'feature_importances_'):
        importances = pd.DataFrame({
            'Feature': X.columns,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        
        fig = px.bar(importances, x='Feature', y='Importance',
                    title='Feature Importance')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': '#e5e7eb'},
            xaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
            yaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
            height=500,
            margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
        )
        st.plotly_chart(
            fig, 
            use_container_width=True,
            config={
                'displayModeBar': True,
                'displaylogo': False,
                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
            }
        )
    
    # SHAP Values
    st.markdown("### SHAP Values")
    try:
        import shap
        
        # Select appropriate explainer based on model type
        model_type = str(type(model)).lower()
        
        if any(tree_model in model_type for tree_model in ['randomforest', 'gradientboosting', 'xgboost', 'lightgbm', 'catboost']):
            # Tree-based models
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X)
        elif any(linear_model in model_type for linear_model in ['logisticregression', 'linearregression', 'ridge', 'lasso']):
            # Linear models - use LinearExplainer
            # For linear models, we need to use the scaled data
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            explainer = shap.LinearExplainer(model, X_scaled)
            shap_values = explainer.shap_values(X_scaled)
        elif 'svc' in model_type or 'svr' in model_type:
            # SVM models
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            explainer = shap.KernelExplainer(model.predict, X_scaled)
            shap_values = explainer.shap_values(X_scaled[:100])  # Use subset for performance
        else:
            # Fallback to KernelExplainer for other models
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            explainer = shap.KernelExplainer(model.predict, X_scaled[:50])  # Use small subset
            shap_values = explainer.shap_values(X_scaled[:20])  # Use even smaller subset for performance
        
        # Handle different shap_values formats
        if isinstance(shap_values, list):
            if len(shap_values) > 1:
                shap_values = shap_values[1]  # For binary classification, use positive class
            else:
                shap_values = shap_values[0]
        
        # Create summary plot
        fig, ax = plt.subplots(figsize=(10, 6))
        shap.summary_plot(shap_values, X, show=False, max_display=10)
        st.pyplot(fig)
        plt.clf()
        
        # Also show feature importance from SHAP
        if len(shap_values.shape) == 2:  # 2D array
            feature_importance = np.abs(shap_values).mean(axis=0)
        else:  # 1D array
            feature_importance = np.abs(shap_values)
        
        importance_df = pd.DataFrame({
            'Feature': X.columns,
            'SHAP_Importance': feature_importance
        }).sort_values('SHAP_Importance', ascending=False)
        
        fig = px.bar(importance_df.head(10), x='SHAP_Importance', y='Feature',
                    title='SHAP Feature Importance', orientation='h')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': '#e5e7eb'},
            xaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
            yaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
            height=400,
            margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
        )
        st.plotly_chart(
            fig, 
            use_container_width=True,
            config={
                'displayModeBar': True,
                'displaylogo': False,
                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
            }
        )
        
    except Exception as e:
        st.warning(f"Could not generate SHAP values: {str(e)}")
        st.info("SHAP values require the model to be compatible with TreeExplainer, LinearExplainer, or KernelExplainer. Some models may not be supported.")
    
    # Model Performance Metrics
    st.markdown("### Model Performance")
    if st.session_state.metrics:
        # Use DataFrame.from_records for metrics dict
        metrics_df = pd.DataFrame.from_records(list(st.session_state.metrics.items()), columns=['Metric', 'Value'])
        st.dataframe(metrics_df)
    
    # Prediction Analysis
    st.markdown("### Prediction Analysis")
    y_pred = model.predict(X)
    
    # Check if it's a classification model by looking at the model type
    is_classification = any(model_type in str(type(model)).lower() 
                          for model_type in ['classifier', 'classification'])
    
    if is_classification:
        # Classification metrics
        st.markdown("#### Classification Report")
        st.text(classification_report(y, y_pred))
        
        # Confusion Matrix
        cm = confusion_matrix(y, y_pred)
        fig = px.imshow(cm,
                       labels=dict(x="Predicted", y="Actual", color="Count"),
                       title="Confusion Matrix")
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': '#e5e7eb'},
            height=400,
            margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
        )
        st.plotly_chart(
            fig, 
            use_container_width=True,
            config={
                'displayModeBar': True,
                'displaylogo': False,
                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
            }
        )
    else:
        # Regression metrics
        fig = px.scatter(x=y, y=y_pred,
                        title="Actual vs Predicted Values",
                        labels={'x': 'Actual', 'y': 'Predicted'})
        fig.add_trace(px.line(x=[min(y), max(y)],
                             y=[min(y), max(y)]).data[0])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font={'color': '#e5e7eb'},
            xaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
            yaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
            height=500,
            margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
        )
        st.plotly_chart(
            fig, 
            use_container_width=True,
            config={
                'displayModeBar': True,
                'displaylogo': False,
                'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
            }
        )

def show_predictions(df, model, X):
    st.markdown("## 📱 Make Predictions")
    
    # Create input form
    st.markdown("### Input Features")
    input_data = {}
    
    for feature in X.columns:
        if df[feature].dtype in ['int64', 'float64']:
            input_data[feature] = st.number_input(
                f"Enter {feature}",
                value=float(df[feature].mean()),
                format="%.2f"
            )
        else:
            input_data[feature] = st.selectbox(
                f"Select {feature}",
                options=df[feature].unique()
            )
    
    if st.button("Make Prediction"):
        # Prepare input data
        input_df = pd.DataFrame([input_data])
        # Encode categorical columns automatically
        non_numeric_cols = input_df.select_dtypes(include=['object', 'category']).columns.tolist()
        if non_numeric_cols:
            st.info(f"Encoding categorical columns: {non_numeric_cols}")
            for col in non_numeric_cols:
                # Use pandas' get_dummies for one-hot encoding
                dummies = pd.get_dummies(input_df[col], prefix=col)
                input_df = input_df.drop(col, axis=1).join(dummies)
            # Align columns with training data (X)
            for col in X.columns:
                if col not in input_df.columns:
                    input_df[col] = 0
            input_df = input_df[X.columns]  # Ensure column order
        else:
            st.success("All input columns are numeric. Proceeding with prediction.")
        try:
            prediction = model.predict(input_df)
            # Display result
            st.markdown("### Prediction Result")
            pred_value = prediction[0]
            if isinstance(pred_value, (int, float, np.integer, np.floating)):
                st.metric("Predicted Value", f"{pred_value:.2f}")
            else:
                st.metric("Predicted Value", str(pred_value))
            # Show confidence interval
            if hasattr(model, 'predict_proba'):
                proba = model.predict_proba(input_df)
                st.markdown("### Prediction Probabilities")
                fig = px.bar(x=model.classes_, y=proba[0],
                            title="Class Probabilities")
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font={'color': '#e5e7eb'},
                    xaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
                    yaxis={'color': '#e5e7eb', 'gridcolor': '#374151'},
                    height=400,
                    margin={'l': 40, 'r': 40, 't': 60, 'b': 40}
                )
                st.plotly_chart(
                    fig, 
                    use_container_width=True,
                    config={
                        'displayModeBar': True,
                        'displaylogo': False,
                        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
                    }
                )
        except Exception as e:
            st.error(f"Prediction failed: {e}")

def main():
    # Create sidebar
    selected = create_sidebar()
    
    # Add refresh button in the sidebar
    with st.sidebar:
        st.title("🤖 AI Data Analysis Tool")
        if st.button("🔄 Refresh App"):
            st.session_state.clear()
            st.rerun()
    
    # Navigation menu
    if selected == "Home":
        show_home()
    elif selected == "Data Upload":
        show_data_upload()
    elif selected == "Data Analysis":
        show_data_analysis()
    elif selected == "Model Training":
        if st.session_state.df is not None:
            show_model_training(st.session_state.df)
        else:
            st.warning("Please upload a dataset first!")
    elif selected == "Model Analysis":
        if st.session_state.model is not None:
            show_model_analysis(st.session_state.df, st.session_state.model, 
                              st.session_state.X, st.session_state.y)
        else:
            st.warning("Please train a model first!")
    elif selected == "Predictions":
        if st.session_state.model is not None:
            show_predictions(st.session_state.df, st.session_state.model, st.session_state.X)
        else:
            st.warning("Please train a model first!")

if __name__ == "__main__":
    main()