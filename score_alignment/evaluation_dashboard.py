import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Define path to the folder containing CSV files
RESULT_FOLDER = 'results'


# Function to get CSV file names in the results folder
def get_csv_files(folder):
    return [file for file in os.listdir(folder) if file.endswith('.csv')]


# Function to load a CSV file as a DataFrame
def load_data(file_path):
    return pd.read_csv(file_path)


def create_buble_chart(df):
    # Count occurrences of each (Calculated Rating, Actual Rating) pair
    df_plot = df[['Calculated Rating', 'Actual Rating']].copy()
    counts = df_plot.value_counts().reset_index(name="Count")

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(counts['Calculated Rating'], counts['Actual Rating'], s=counts['Count'] * 100, alpha=0.6)
    ax.plot([0, 1], [0, 1], color='red', linestyle='--', alpha=0.6)
    delta = 0.2
    ax.plot([0, 1], [delta, 1 + delta], color='blue', linestyle='--', alpha=0.3, label="Upper Bound (+0.2)")
    ax.plot([0, 1], [-delta, 1 - delta], color='blue', linestyle='--', alpha=0.3, label="Lower Bound (-0.2)")
    ax.fill_between([0, 1], [-delta, 1 - delta], [delta, 1 + delta], color='blue', alpha=0.1, label="Error Band (±0.2)")
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)
    ax.set_xlabel("Calculated Rating")
    ax.set_ylabel("Actual Rating")
    ax.set_title("Bubble Plot (Point Size by Count)")

    return fig

def create_difference_plot(df):
    df_plot = df[['id', 'Calculated Rating', 'Actual Rating']].copy()
    df_plot['Difference'] = df_plot['Calculated Rating'] - df_plot['Actual Rating']
    df_plot['Color'] = df_plot['Color'] = np.where(df_plot['Difference'] > 0, 'blue', 'red')

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.bar(df_plot['id'], df_plot['Difference'], color=df_plot['Color'])
    plt.ylim(-1, 1)
    plt.xlabel("id")
    plt.ylabel("Difference")
    plt.title("Difference between Calculated and Actual Ratings")

    return fig



st.set_page_config(page_title='Document Search', layout='wide')


# Get list of CSV files in the folder
csv_files = get_csv_files(RESULT_FOLDER)

# Streamlit application layout
st.title("Compare CSV Result Files")

# Create two columns for side-by-side comparison
col1, col2 = st.columns(2)

# Column 1: Select and display first file
with col1:
    st.header("File 1")
    file1 = st.selectbox("Select a CSV file:", options=csv_files, key="file1")

    if file1:
        df1 = load_data(os.path.join(RESULT_FOLDER, file1))
        df1['Difference'] = df1['Calculated Rating'] - df1['Actual Rating']

        # Calculate RMSE
        rmse1 = np.sqrt(((df1['Calculated Rating'] - df1['Actual Rating']) ** 2).mean())

        # Create bubble chart
        fig1_1 = create_buble_chart(df1)

        # Create difference plot
        fig2_1 = create_difference_plot(df1)

        st.write("Data Preview:")
        st.dataframe(df1)  # Show preview of data
        st.write("RMSE:", rmse1)  # Show RMSE

        col1_1, col1_2 = st.columns(2)

        col1_1.pyplot(fig1_1)
        col1_2.pyplot(fig2_1)

# Column 2: Select and display second file
with col2:
    st.header("File 2")
    file2 = st.selectbox("Select another CSV file:", options=csv_files, key="file2")

    if file2:
        df2 = load_data(os.path.join(RESULT_FOLDER, file2))
        df2['Difference'] = df2['Calculated Rating'] - df2['Actual Rating']

        # Calculate RMSE
        rmse2 = np.sqrt(((df2['Calculated Rating'] - df2['Actual Rating']) ** 2).mean())

        # Create bubble chart
        fig1_2 = create_buble_chart(df2)

        # Create difference plot
        fig2_2 = create_difference_plot(df2)

        st.write("Data Preview:")
        st.dataframe(df2)
        st.write("RMSE:", rmse2)

        col2_1, col2_2 = st.columns(2)

        col2_1.pyplot(fig1_2)
        col2_2.pyplot(fig2_2)
