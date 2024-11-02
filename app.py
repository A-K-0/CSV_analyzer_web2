import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from io import StringIO

def generate_basic_eda(df):
    """Generate basic analysis on CSV files"""
    stats = {}
    
    # Basic dataset info
    stats['rows'] = len(df)
    stats['columns'] = len(df.columns)
    stats['dtypes'] = df.dtypes.value_counts().to_dict()
    
    # Missing values
    missing = df.isnull().sum()
    stats['missing'] = missing[missing > 0].to_dict()
    
    return stats

def plot_histogram(df, column):
    """Create histogram for numeric column"""
    fig = px.histogram(df, x=column, title=f'Distribution of {column}')
    return fig

def plot_boxplot(df, column):
    """Create boxplot for numeric column"""
    fig = px.box(df, y=column, title=f'Boxplot of {column}')
    return fig

def plot_lineplot(df, column):
    """Create line plot for numeric column"""
    fig = px.line(df, y=column, title=f'Line Plot of {column} Over Index')
    return fig

def plot_correlation(df):
    """Create correlation heatmap"""
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) > 1:
        corr = df[numeric_cols].corr()
        fig = px.imshow(corr, title='Correlation Matrix',
                       labels=dict(color="Correlation"),
                       color_continuous_scale='RdBu')
        return fig
    return None

def main():
    st.set_page_config(page_title="CSV Analyzer Web", layout="wide")
    
    st.title("📊 CSV Analyzer Web")
    st.markdown("""
    This app performs basic **Exploratory Data Analysis** on your CSV file.
    Upload your data to get started!
    """)
    
    # File upload
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Load data
            df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
            
            # Display basic info
            st.header("📋 Dataset Overview")
            st.write(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
            
            # Display raw data with toggle
            if st.checkbox("Show raw data"):
                st.dataframe(df)
            
            # Basic statistics
            st.header("📈 Basic Statistics")
            stats = generate_basic_eda(df)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Number of Rows", stats['rows'])
            with col2:
                st.metric("Number of Columns", stats['columns'])
            
            # Data types
            st.subheader("Data Types")
            st.write(pd.DataFrame({'Count': stats['dtypes']}).reset_index().rename(columns={'index': 'Data Type'}))
            
            # Missing values
            if stats['missing']:
                st.subheader("Missing Values")
                st.write(pd.DataFrame({'Count': stats['missing']}).reset_index().rename(columns={'index': 'Column'}))
            
            # Numeric column analysis
            st.header("📉 Numeric Column Analysis")
            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
            
            if len(numeric_cols) > 0:
                # Descriptive statistics
                st.subheader("Descriptive Statistics")
                st.write(df[numeric_cols].describe())
                
                # Column selection for visualization
                selected_col = st.selectbox("Select column for visualization:", numeric_cols)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.plotly_chart(plot_histogram(df, selected_col), use_container_width=True)
                with col2:
                    st.plotly_chart(plot_boxplot(df, selected_col), use_container_width=True)
                with col3:
                    st.plotly_chart(plot_lineplot(df, selected_col), use_container_width=True)
                
            
            # Categorical column analysis
            categorical_cols = df.select_dtypes(include=['object']).columns
            if len(categorical_cols) > 0:
                st.header("📊 Categorical Column Analysis")
                selected_cat_col = st.selectbox("Select categorical column:", categorical_cols)
                
                # Value counts
                value_counts = df[selected_cat_col].value_counts()
                fig = px.bar(x=value_counts.index, y=value_counts.values,
                           title=f'Value Counts for {selected_cat_col}')
                st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
            
    else:
        st.info("👆 Upload a CSV file to get started!")
        
        if st.button("Use Example Dataset"):
            # Generate example data
            df = pd.DataFrame(
                np.random.randn(100, 4),
                columns=['Feature_1', 'Feature_2', 'Feature_3', 'Feature_4']
            )
            df['Category'] = np.random.choice(['A', 'B', 'C'], size=100)
            
            st.session_state['data'] = df
            st.experimental_rerun()

if __name__ == "__main__":
    main()
