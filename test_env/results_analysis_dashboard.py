import streamlit as st
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

# Set the path to your results folder
RESULTS_FOLDER = "results"


def load_csv_files(folder_path):
    """Returns a list of CSV files from the specified folder."""
    return glob.glob(os.path.join(folder_path, "*.csv"))


def load_data(file_path):
    """Loads CSV file into a DataFrame."""
    return pd.read_csv(file_path)

st.set_page_config(page_title='Document Search', layout='wide')

# Streamlit App
st.title("Evaluation Results Viewer")

# Get list of CSV files
csv_files = load_csv_files(RESULTS_FOLDER)
file_names = [os.path.basename(file) for file in csv_files]

# Select a file
selected_file = st.selectbox("Choose a CSV file", file_names)

if selected_file:
    # Get the full file path
    file_path = os.path.join(RESULTS_FOLDER, selected_file)

    # Load the data
    df = load_data(file_path)



    # Plotting the bar chart based on 'id' and 'Calculated Rating'
    if 'id' in df.columns and 'Calculated Rating' in df.columns:

        # Display the average scores
        cols = st.columns(6)

        cols[0].metric(label="Average Calculated Rating", value=round(df['Calculated Rating'].mean(), 2))
        cols[1].metric(label="Average Subscore Main Points", value=round(df['Correctness Subscore Main Points'].mean(), 2))
        cols[2].metric(label="Average Subscore Accuracy", value=round(df['Correctness Subscore Accuracy'].mean(), 2))
        cols[3].metric(label="Average Subscore Relevance", value=round(df['Correctness Subscore Relevance'].mean(), 2))
        cols[4].metric(label="Average Subscore Clarity", value=round(df['Correctness Subscore Clarity'].mean(), 2))
        cols[5].metric(label="Average Subscore Math", value=round(df['Correctness Subscore Math'].mean(), 2))

        st.write("### Calculated Ratings Bar Chart")

        # Plot the bar chart
        st.bar_chart(df.set_index('id')['Calculated Rating'])


    else:
        st.warning("The selected file does not contain the required columns: 'id' and 'Calculated Rating'")

    # Display the DataFrame
    st.write("### Data Preview", df)
